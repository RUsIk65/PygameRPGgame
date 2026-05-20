import sqlite3

conn = sqlite3.connect("database/entity.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON;")

cursor.executescript("""
CREATE TABLE IF NOT EXISTS nps (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    image TEXT
);
CREATE TABLE IF NOT EXISTS enemy (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    hp INTEGER NOT NULL,
    defense INTEGER NOT NULL,
    attack INTEGER NOT NULL,
    speed INTEGER NOT NULL,
    radar_range INTEGER NOT NULL,
    image TEXT
);
""")
