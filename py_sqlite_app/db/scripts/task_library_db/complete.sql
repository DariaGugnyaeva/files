-- Я по айдишнику книги определяю наличие

UPDATE library
SET status = TRUE
WHERE id = ?;
