from connect import get_connection


def search_pattern():
    pattern = input("Enter pattern to search: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM search_phonebook(%s);", (pattern,))
    rows = cur.fetchall()

    if rows:
        print("\nMatched records:")
        for row in rows:
            print(row)
    else:
        print("No matches found.")

    cur.close()
    conn.close()


def insert_or_update():
    name = input("Enter username: ")
    phone = input("Enter phone: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL insert_user(%s, %s);", (name, phone))
    conn.commit()

    print("User inserted or updated successfully.")

    cur.close()
    conn.close()


def insert_many():
    n = int(input("How many users do you want to add? "))

    names = []
    phones = []

    for i in range(n):
        print(f"\nUser {i+1}")
        name = input("Enter username: ")
        phone = input("Enter phone: ")
        names.append(name)
        phones.append(phone)

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        DO $$
        DECLARE
            wrong_data TEXT[] := '{}';
        BEGIN
            CALL insert_many_users(%s, %s, wrong_data);
            RAISE NOTICE 'Incorrect data: %', wrong_data;
        END $$;
    """, (names, phones))

    conn.commit()
    print("Batch insert completed. Check NOTICE for incorrect data.")

    cur.close()
    conn.close()


def show_paginated():
    limit = int(input("Enter limit: "))
    offset = int(input("Enter offset: "))

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM get_phonebook_paginated(%s, %s);", (limit, offset))
    rows = cur.fetchall()

    if rows:
        print("\nPaginated records:")
        for row in rows:
            print(row)
    else:
        print("No records found.")

    cur.close()
    conn.close()


def delete_user():
    value = input("Enter username or phone to delete: ")

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("CALL delete_by_username_or_phone(%s);", (value,))
    conn.commit()

    print("Delete operation completed.")

    cur.close()
    conn.close()


def main():
    while True:
        print("\n--- PHONEBOOK MENU ---")
        print("1. Search by pattern")
        print("2. Insert user")
        print("3. Insert many users")
        print("4. Show paginated data")
        print("5. Delete by username or phone")
        print("0. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            search_pattern()
        elif choice == "2":
            insert_or_update()
        elif choice == "3":
            insert_many()
        elif choice == "4":
            show_paginated()
        elif choice == "5":
            delete_user()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()