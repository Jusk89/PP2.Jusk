-- 2. Procedure: insert new user, or update phone if exists
CREATE OR REPLACE PROCEDURE insert_or_update_user(user_name TEXT, user_phone TEXT)
AS $$
BEGIN
    IF EXISTS (SELECT 1 FROM phonebook WHERE username = user_name) THEN
        UPDATE phonebook
        SET phone = user_phone
        WHERE username = user_name;
    ELSE
        INSERT INTO phonebook(username, phone)
        VALUES (user_name, user_phone);
    END IF;
END;
$$ LANGUAGE plpgsql;


-- 3. Procedure: insert many users, validate phones
CREATE OR REPLACE PROCEDURE insert_many_users(
    IN user_names TEXT[],
    IN user_phones TEXT[],
    INOUT incorrect_data TEXT[] DEFAULT '{}'
)
AS $$
DECLARE
    i INT;
BEGIN
    IF array_length(user_names, 1) IS DISTINCT FROM array_length(user_phones, 1) THEN
        RAISE EXCEPTION 'Arrays must have the same length';
    END IF;

    FOR i IN 1..array_length(user_names, 1) LOOP
        -- пример простой проверки: телефон должен состоять только из цифр
        -- и иметь длину от 10 до 15
        IF user_phones[i] ~ '^[0-9]{10,15}$' THEN
            IF EXISTS (SELECT 1 FROM phonebook WHERE username = user_names[i]) THEN
                UPDATE phonebook
                SET phone = user_phones[i]
                WHERE username = user_names[i];
            ELSE
                INSERT INTO phonebook(username, phone)
                VALUES (user_names[i], user_phones[i]);
            END IF;
        ELSE
            incorrect_data := array_append(
                incorrect_data,
                user_names[i] || ': ' || user_phones[i]
            );
        END IF;
    END LOOP;
END;
$$ LANGUAGE plpgsql;


-- 5. Procedure: delete by username or phone
CREATE OR REPLACE PROCEDURE delete_by_username_or_phone(value_text TEXT)
AS $$
BEGIN
    DELETE FROM phonebook
    WHERE username = value_text
       OR phone = value_text;
END;
$$ LANGUAGE plpgsql;