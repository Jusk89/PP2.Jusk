import csv
import json
from connect import get_connection


def run_sql_file(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        cur.execute(file.read())

    conn.commit()
    cur.close()
    conn.close()

    print(f"{filename} executed successfully.")


def get_group_id(cur, group_name):
    cur.execute("SELECT id FROM groups WHERE name = %s;", (group_name,))
    group = cur.fetchone()

    if group:
        return group[0]

    cur.execute(
        "INSERT INTO groups(name) VALUES(%s) RETURNING id;",
        (group_name,)
    )
    return cur.fetchone()[0]


def add_contact():
    name = input("Name: ")
    email = input("Email: ")
    birthday = input("Birthday YYYY-MM-DD: ")
    group_name = input("Group: ")

    conn = get_connection()
    cur = conn.cursor()

    group_id = get_group_id(cur, group_name)

    cur.execute("""
        INSERT INTO contacts(name, email, birthday, group_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id;
    """, (name, email, birthday, group_id))

    contact_id = cur.fetchone()[0]

    while True:
        phone = input("Phone number (empty to stop): ")

        if phone == "":
            break

        phone_type = input("Type home/work/mobile: ")

        cur.execute("""
            INSERT INTO phones(contact_id, phone, type)
            VALUES (%s, %s, %s);
        """, (contact_id, phone, phone_type))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact added.")


def add_phone_to_contact():
    name = input("Contact name: ")
    phone = input("New phone: ")
    phone_type = input("Type home/work/mobile: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL add_phone(%s, %s, %s);",
        (name, phone, phone_type)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Phone added.")


def move_contact_to_group():
    name = input("Contact name: ")
    group = input("New group: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        "CALL move_to_group(%s, %s);",
        (name, group)
    )

    conn.commit()
    cur.close()
    conn.close()

    print("Contact moved to group.")


def show_contacts():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            c.id,
            c.name,
            c.email,
            c.birthday,
            g.name,
            p.phone,
            p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        ORDER BY c.id;
    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def search_contacts():
    query = input("Search text: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_contacts(%s);", (query,))
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def filter_by_group():
    group = input("Group name: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id
        WHERE g.name = %s
        ORDER BY c.name;
    """, (group,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def search_by_email():
    email = input("Email search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        WHERE c.email ILIKE %s;
    """, (f"%{email}%",))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def sort_contacts():
    print("1 - Sort by name")
    print("2 - Sort by birthday")
    print("3 - Sort by date added")

    choice = input("Choose: ")

    if choice == "1":
        order = "c.name"
    elif choice == "2":
        order = "c.birthday"
    elif choice == "3":
        order = "c.created_at"
    else:
        print("Invalid choice.")
        return

    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"""
        SELECT c.name, c.email, c.birthday, g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        ORDER BY {order};
    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


def paginated_contacts():
    page = 0
    limit = 5

    while True:
        offset = page * limit

        conn = get_connection()
        cur = conn.cursor()

        cur.execute("""
            SELECT c.name, c.email, c.birthday, g.name
            FROM contacts c
            LEFT JOIN groups g ON c.group_id = g.id
            ORDER BY c.id
            LIMIT %s OFFSET %s;
        """, (limit, offset))

        rows = cur.fetchall()

        print(f"\nPage {page + 1}")

        if rows:
            for row in rows:
                print(row)
        else:
            print("No contacts on this page.")

        cur.close()
        conn.close()

        command = input("next / prev / quit: ")

        if command == "next":
            page += 1
        elif command == "prev":
            page = max(0, page - 1)
        elif command == "quit":
            break


def import_from_csv():
    filename = input("CSV filename: ")

    conn = get_connection()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            group_id = get_group_id(cur, row["group"])

            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES (%s, %s, %s, %s)
                RETURNING id;
            """, (
                row["name"],
                row["email"],
                row["birthday"],
                group_id
            ))

            contact_id = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s, %s, %s);
            """, (
                contact_id,
                row["phone"],
                row["type"]
            ))

    conn.commit()
    cur.close()
    conn.close()

    print("CSV imported.")


def export_to_json():
    filename = input("JSON filename: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT 
            c.id,
            c.name,
            c.email,
            c.birthday,
            g.name
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        ORDER BY c.id;
    """)

    contacts = cur.fetchall()

    result = []

    for contact in contacts:
        contact_id = contact[0]

        cur.execute("""
            SELECT phone, type
            FROM phones
            WHERE contact_id = %s;
        """, (contact_id,))

        phones = cur.fetchall()

        result.append({
            "name": contact[1],
            "email": contact[2],
            "birthday": str(contact[3]),
            "group": contact[4],
            "phones": [
                {
                    "phone": p[0],
                    "type": p[1]
                }
                for p in phones
            ]
        })

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(result, file, indent=4)

    cur.close()
    conn.close()

    print("Exported to JSON.")


def import_from_json():
    filename = input("JSON filename: ")

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)

    conn = get_connection()
    cur = conn.cursor()

    for item in data:
        cur.execute(
            "SELECT id FROM contacts WHERE name = %s;",
            (item["name"],)
        )

        existing = cur.fetchone()

        if existing:
            print(f"Contact {item['name']} already exists.")
            choice = input("skip or overwrite? ")

            if choice == "skip":
                continue

            if choice == "overwrite":
                cur.execute(
                    "DELETE FROM contacts WHERE name = %s;",
                    (item["name"],)
                )

        group_id = get_group_id(cur, item["group"])

        cur.execute("""
            INSERT INTO contacts(name, email, birthday, group_id)
            VALUES (%s, %s, %s, %s)
            RETURNING id;
        """, (
            item["name"],
            item["email"],
            item["birthday"],
            group_id
        ))

        contact_id = cur.fetchone()[0]

        for phone in item["phones"]:
            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s, %s, %s);
            """, (
                contact_id,
                phone["phone"],
                phone["type"]
            ))

    conn.commit()
    cur.close()
    conn.close()

    print("JSON imported.")


def delete_contact():
    name = input("Contact name to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("DELETE FROM contacts WHERE name = %s;", (name,))

    conn.commit()
    cur.close()
    conn.close()

    print("Contact deleted.")


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Create tables")
        print("2. Create procedures")
        print("3. Add contact")
        print("4. Add phone to contact")
        print("5. Move contact to group")
        print("6. Show all contacts")
        print("7. Search contacts")
        print("8. Filter by group")
        print("9. Search by email")
        print("10. Sort contacts")
        print("11. Pagination")
        print("12. Import from CSV")
        print("13. Export to JSON")
        print("14. Import from JSON")
        print("15. Delete contact")
        print("16. Exit")

        choice = input("Choose: ")

        if choice == "1":
            run_sql_file("schema.sql")
        elif choice == "2":
            run_sql_file("procedures.sql")
        elif choice == "3":
            add_contact()
        elif choice == "4":
            add_phone_to_contact()
        elif choice == "5":
            move_contact_to_group()
        elif choice == "6":
            show_contacts()
        elif choice == "7":
            search_contacts()
        elif choice == "8":
            filter_by_group()
        elif choice == "9":
            search_by_email()
        elif choice == "10":
            sort_contacts()
        elif choice == "11":
            paginated_contacts()
        elif choice == "12":
            import_from_csv()
        elif choice == "13":
            export_to_json()
        elif choice == "14":
            import_from_json()
        elif choice == "15":
            delete_contact()
        elif choice == "16":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu()