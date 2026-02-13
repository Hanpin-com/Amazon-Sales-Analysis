import sqlite3
import pandas as pd

def initialize_database():
    df = pd.read_csv("data/Amazon.csv")

    conn = sqlite3.connect("amazon.db")

    df.to_sql("sales", conn, if_exists="replace", index=False)

    conn.execute("CREATE INDEX IF NOT EXISTS idx_category ON sales(category);")

    conn.commit()
    conn.close()

    print("Database initialized.")

if __name__ == "__main__":
    initialize_database()
