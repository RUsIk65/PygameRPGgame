import sqlite3

conn = sqlite3.connect("database/items.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.executescript("""
CREATE TABLE IF NOT EXISTS entity (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    cost INTEGER NOT NULL,
    rareness TEXT NOT NULL,
    required_level INTEGER NOT NULL,
    image TEXT
);

CREATE TABLE IF NOT EXISTS weapon (
    id INTEGER PRIMARY KEY,
    damage INTEGER NOT NULL,
    FOREIGN KEY (id) REFERENCES entity(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS armor (
    id INTEGER PRIMARY KEY,
    defense INTEGER NOT NULL,
    FOREIGN KEY (id) REFERENCES entity(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS potion (
    id INTEGER PRIMARY KEY,
    mana_restore INTEGER NOT NULL,
    FOREIGN KEY (id) REFERENCES entity(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS backpack (
    id INTEGER PRIMARY KEY,
    capacity INTEGER NOT NULL,
    FOREIGN KEY (id) REFERENCES entity(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS food (
    id INTEGER PRIMARY KEY,
    health_restore INTEGER NOT NULL,
    FOREIGN KEY (id) REFERENCES entity(id) ON DELETE CASCADE
);
""")

conn.commit()
conn.close()
