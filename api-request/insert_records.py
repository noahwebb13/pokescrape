from api_request import fetch_data, mock_fetch_data
import psycopg2

# test 
# result = mock_fetch_data()
# print(result)

def connect_to_db():
    print("Connecting to the PostgreSQL database...")
    try:
        conn = psycopg2.connect(
            host='db',
            # port=5000,
            port=5432,
            dbname='db',
            user='db_user',
            password='db_password'
        )
        print(f"Connection successful: {conn}")
        return conn
    except psycopg2.Error as e: 
        print(f"Database connection failed {e}")
        raise


# connect_to_db()

def create_table(conn):
    print("Creating table if not exists...")
    try:
        cursor = conn.cursor()
        cursor.execute("""
        CREATE SCHEMA IF NOT EXISTS dev;

        -- COMMENT: May need to drop the table for fixing errors
        -- DROP TABLE IF EXISTS dev.raw_weather_data;
        
        CREATE TABLE IF NOT EXISTS dev.raw_weather_data (
            id SERIAL PRIMARY KEY,
            city TEXT, 
            temperature FLOAT,
            weather_descriptions TEXT, 
            wind_speed FLOAT,
            time TIMESTAMP,
            inserted_at TIMESTAMP DEFAULT NOW(),
            utc_offset TEXT
        );
        """)
        conn.commit()
        print(f"Table was created.")

    except psycopg2.Error as e:
        print(f"Failed to create table {e}")
        raise


def insert_records(conn, data): 
    print(f"Inserting weather data into the database...")
    try:
        weather = data['current']
        location = data['location']

        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_weather_data (
                city, 
                temperature, 
                weather_descriptions, 
                wind_speed, 
                time, 
                inserted_at,
                utc_offset
            ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """, (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        conn.commit()
        print(f"Data succesfully inserted.")
        
    except psycopg2.Error as e:
        print(f"Error inserting data into the database: {e}")
        raise

def main():
    try: 
        data = fetch_data() # production 
        # data = mock_fetch_data() # testing
        conn = connect_to_db()
        create_table(conn)
        insert_records(conn, data)
    except Exception as e:
        print(f"An error occured during execution: {e}")
        raise
    finally:
        if 'conn' in locals():
            conn.close()
            print("Database connection closed.")

# main()
if __name__ == "__main__":
    main()