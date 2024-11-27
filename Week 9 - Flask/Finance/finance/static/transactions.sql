CREATE TABLE transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    symbol TEXT,
    shares INTEGER,
    price REAL,
    transacted TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(user_id) REFERENCES users(id)
);

CREATE UNIQUE INDEX idx_user_symbol ON transactions (user_id, symbol);
CREATE INDEX idx_user_id ON transactions (user_id);