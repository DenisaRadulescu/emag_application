import json
import psycopg2 as ps


def read_config(path: str = "config.json"):
    with open(path, "r") as f:
        config = json.loads(f.read())

    return config


def read_admins(config: dict, table: str = "emag.emag_admin"):

    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            spl_query = f"select * from {table}"
            cursor.execute(spl_query)
            users = cursor.fetchone()
            return users


def read_products(config: dict, table: str= "emag.products"):
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = f"select name, store, price from {table}"
            cursor.execute(sql_query)
            products = cursor.fetchall()
            columns = [desc[0] for desc in cursor.description]
            products_list = []
            for item in products:
                products_list.append(dict(zip(columns, item)))

            return products_list


def add_product(config: dict, name: str, store: str, price: float, table: str = "emag.products"):
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = f"INSERT INTO {table} (name, store, price) VALUES (%s, %s, %s) RETURNING *"
            cursor.execute(sql_query, (name, store, price))
            new_product = cursor.fetchone()
            conn.commit()
            columns = [desc[0] for desc in cursor.description]
            return dict(zip(columns, new_product))


def delete_product(config: dict, name: str, table: str = "emag.products"):
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = f"DELETE FROM {table} WHERE name = %s"
            cursor.execute(sql_query, (name,))
            conn.commit()
            return cursor.rowcount


def update_product_price(config: dict, name: str, new_price: float, table: str = "emag.products"):
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = f"UPDATE {table} SET price = %s WHERE name = %s"
            cursor.execute(sql_query, (new_price, name))
            conn.commit()
            return cursor.rowcount


def get_most_expensive_product(config: dict, table: str = "emag.products"):
    with ps.connect(**config) as conn:
        with conn.cursor() as cursor:
            sql_query = f"SELECT name FROM {table} ORDER BY price DESC LIMIT 1"
            cursor.execute(sql_query)
            most_expensive_product = cursor.fetchone()
            if most_expensive_product:
                return most_expensive_product[0]
            else:
                return None

if __name__ == '__main__':
    config = read_config()
    admins = read_admins(config)
    products = read_products(config)
    new_product = add_product(config, name="cutit", store="flanco", price= 20)