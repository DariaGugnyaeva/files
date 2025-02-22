CREATE TABLE IF NOT EXISTS readers (
    id INTEGER PRIMARY KEY,
    ID_book INTEGER NOT NULL,
    num_reader_card INTEGER NOT NULL,
    FOREIGN KEY (ID_book)
        REFERENCES library(id) ON UPDATE CASCADE
    FOREIGN KEY (num_reader_card)
        REFERENCES visitors(id) ON UPDATE CASCADE
);
