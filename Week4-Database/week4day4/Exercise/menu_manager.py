# menu_manager.py
import psycopg2

class MenuManager:
    @classmethod
    def get_by_name(cls, item_name):
        try:
            connection = psycopg2.connect(
                dbname="your_database_name",
                user="your_username",
                password="12345678",
                host="localhost"
            )
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Menu_Items WHERE item_name = %s", (item_name,))
            item = cursor.fetchone()

            if item:
                return item
            else:
                return None

        except psycopg2.Error as e:
            print("Error while getting item by name:", e)

        finally:
            if connection:
                cursor.close()
                connection.close()

    @classmethod
    def all_items(cls):
        try:
            connection = psycopg2.connect(
                dbname="your_database_name",
                user="your_username",
                password="your_password",
                host="localhost"
            )
            cursor = connection.cursor()

            cursor.execute("SELECT * FROM Menu_Items")
            items = cursor.fetchall()

            return items

        except psycopg2.Error as e:
            print("Error while getting all items:", e)

        finally:
            if connection:
                cursor.close()
                connection.close()
