# menu_item.py
import psycopg2

class MenuItem:
    def __init__(self, item_name, item_price):
        self.item_name = item_name
        self.item_price = item_price

    def save(self):
        try:
            connection = psycopg2.connect(
                dbname="your_database_name",
                user="your_username",
                password="your_password",
                host="localhost"
            )
            cursor = connection.cursor()

            cursor.execute("INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                           (self.item_name, self.item_price))
            connection.commit()

            print("Item saved successfully.")

        except psycopg2.Error as e:
            print("Error while saving item:", e)

        finally:
            if connection:
                cursor.close()
                connection.close()

    @staticmethod
    def delete(item_name):
        try:
            connection = psycopg2.connect(
                dbname="your_database_name",
                user="your_username",
                password="your_password",
                host="localhost"
            )
            cursor = connection.cursor()

            cursor.execute("DELETE FROM Menu_Items WHERE item_name = %s", (item_name,))
            connection.commit()

            print("Item deleted successfully.")

        except psycopg2.Error as e:
            print("Error while deleting item:", e)

        finally:
            if connection:
                cursor.close()
                connection.close()

    @staticmethod
    def update(item_name, new_item_name, new_item_price):
        try:
            connection = psycopg2.connect(
                dbname="your_database_name",
                user="your_username",
                password="your_password",
                host="localhost"
            )
            cursor = connection.cursor()

            cursor.execute("UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                           (new_item_name, new_item_price, item_name))
            connection.commit()

            print("Item updated successfully.")

        except psycopg2.Error as e:
            print("Error while updating item:", e)

        finally:
            if connection:
                cursor.close()
                connection.close()
