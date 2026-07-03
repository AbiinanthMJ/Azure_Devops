from database import get_connection

def test_connection():
    try:
        conn = get_connection()

        print("Connected to Azure SQL Database!")

        conn.close()

    except Exception as e:
        print("Connection Failed!")
        print(e)

if __name__ == "__main__":
    test_connection()