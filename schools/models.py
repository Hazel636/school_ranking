import psycopg2

def create_schools_table():
    conn = psycopg2.connect(
        dbname="ranking",
        user="postgres",
        password="520555",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS schools (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255),
        level VARCHAR(255),
        city VARCHAR(255),
        province VARCHAR(255),
        address VARCHAR(255),
        rating_f FLOAT,
        ranking_f VARCHAR(50),
        link VARCHAR(255)
    )
    """)
    conn.commit()

    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_schools_table()