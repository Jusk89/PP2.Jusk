import csv
from connect import get_connection


def create_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS phonebook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100) NOT NULL,
            phone VARCHAR(20) NOT NULL UNIQUE
        );
    """)

    conn.commit()
    cur.close()
    conn.close()
    print("Table 'phonebook' is ready.")


def insert_from_csv(filename):
    conn = get_connection()
    cur = conn.cursor()

    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            name = row["name"]
            phone = row["phone"]

            try:
                cur.execute("""
                    INSERT INTO phonebook (name, phone)
                    VALUES (%s, %s)
                    ON CONFLICT (phone) DO NOTHING;
                """, (name, phone))
            except Exception as e:
                print(f"Error inserting {name}: {e}")

    conn.commit()
    cur.close()
    conn.close()
    print("Contacts inserted from CSV.")


def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO phonebook (name, phone)
            VALUES (%s, %s);
        """, (name, phone))
        conn.commit()
        print("Contact added successfully.")
    except Exception as e:
        print("Error:", e)
        conn.rollback()

    cur.close()
    conn.close()


def update_contact():
    search_value = input("Enter current name or phone of contact: ")
    new_name = input("Enter new name (leave empty if not changing): ")
    new_phone = input("Enter new phone (leave empty if not changing): ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        if new_name and new_phone:
            cur.execute("""
                UPDATE phonebook
                SET name = %s, phone = %s
                WHERE name = %s OR phone = %s;
            """, (new_name, new_phone, search_value, search_value))

        elif new_name:
            cur.execute("""
                UPDATE phonebook
                SET name = %s
                WHERE name = %s OR phone = %s;
            """, (new_name, search_value, search_value))

        elif new_phone:
            cur.execute("""
                UPDATE phonebook
                SET phone = %s
                WHERE name = %s OR phone = %s;
            """, (new_phone, search_value, search_value))

        else:
            print("Nothing to update.")
            cur.close()
            conn.close()
            return

        conn.commit()
        print("Contact updated successfully.")

    except Exception as e:
        print("Error:", e)
        conn.rollback()

    cur.close()
    conn.close()


def query_contacts():
    print("\nSearch options:")
    print("1 - Show all contacts")
    print("2 - Search by name")
    print("3 - Search by phone prefix")

    choice = input("Choose option: ")

    conn = get_connection()
    cur = conn.cursor()

    if choice == "1":
        cur.execute("SELECT * FROM phonebook ORDER BY id;")

    elif choice == "2":
        name = input("Enter name to search: ")
        cur.execute("""
            SELECT * FROM phonebook
            WHERE name ILIKE %s
            ORDER BY id;
        """, (f"%{name}%",))

    elif choice == "3":
        prefix = input("Enter phone prefix: ")
        cur.execute("""
            SELECT * FROM phonebook
            WHERE phone LIKE %s
            ORDER BY id;
        """, (f"{prefix}%",))

    else:
        print("Invalid option.")
        cur.close()
        conn.close()
        return

    rows = cur.fetchall()

    if rows:
        print("\nContacts:")
        for row in rows:
            print(row)
    else:
        print("No contacts found.")

    cur.close()
    conn.close()


def delete_contact():
    value = input("Enter username or phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    try:
        cur.execute("""
            DELETE FROM phonebook
            WHERE name = %s OR phone = %s;
        """, (value, value))

        conn.commit()

        if cur.rowcount > 0:
            print("Contact deleted successfully.")
        else:
            print("No such contact found.")

    except Exception as e:
        print("Error:", e)
        conn.rollback()

    cur.close()
    conn.close()


def menu():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Create table")
        print("2. Insert contacts from CSV")
        print("3. Insert contact from console")
        print("4. Update contact")
        print("5. Query contacts")
        print("6. Delete contact")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            create_table()
        elif choice == "2":
            insert_from_csv("contacts.csv")
        elif choice == "3":
            insert_from_console()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            query_contacts()
        elif choice == "6":
            delete_contact()
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()