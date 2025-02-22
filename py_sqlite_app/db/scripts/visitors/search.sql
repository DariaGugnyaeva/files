SELECT
    id,
    name,
    surname,
    patr_name,
    num_reader_card
FROM visitors
WHERE (name LIKE '%' || ? || '%') OR (surname LIKE '%' || ? || '%') OR (num_reader_card = ?);
