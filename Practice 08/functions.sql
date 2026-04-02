-- 1. Function: search by pattern
CREATE OR REPLACE FUNCTION search_phonebook(pattern_text TEXT)
RETURNS TABLE (
    id INT,
    username VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.username, p.phone
    FROM phonebook p
    WHERE p.username ILIKE '%' || pattern_text || '%'
       OR p.phone ILIKE '%' || pattern_text || '%';
END;
$$ LANGUAGE plpgsql;


-- 4. Function: pagination with LIMIT and OFFSET
CREATE OR REPLACE FUNCTION get_phonebook_paginated(lim INT, offs INT)
RETURNS TABLE (
    id INT,
    username VARCHAR,
    phone VARCHAR
)
AS $$
BEGIN
    RETURN QUERY
    SELECT p.id, p.username, p.phone
    FROM phonebook p
    ORDER BY p.id
    LIMIT lim OFFSET offs;
END;
$$ LANGUAGE plpgsql;