from flask import Flask, render_template, request, url_for, redirect

import emag_db

app = Flask(__name__)

config = emag_db.read_config()
user_id, username, password = emag_db.read_admins(config)

users = {
    username: password
}


@app.route("/")
def first_function():
    print(" S-a rulat cand apasam pe link")
    return render_template("login.html")


@app.route("/test")
def second_function():
    print(" S-a rulat cand apasam pe link")
    return render_template("test.html")


@app.route("/login", methods=["POST"])
def web_login():
    user = request.form['username']
    passwrd = request.form['password']

    if user in users.keys():
        if passwrd == users[user]:
            data = emag_db.read_products(config)
            return render_template("home.html", data=data)

    return render_template("login.html")


# @app.route("/add_products", methods=['POST', 'PUT'])
# def add_products():
#     try:
#         product_name = request.form['product_name']
#         store = request.form['store']
#         price = request.form['price']
#
#         query = (f"INSERT into emag.products(name, store, price) "
#                  f"values ('{product_name}', '{store}, '{price}')")
#         emag_db.execute_query(sql_query=query, config=config)
#         data = emag_db.execute_query.read_products(config=config)
#         return render_template('home.html', data=data)
#     except Exception as e:
#         return {f"Error in in adding the product, {e}"}
#

@app.route("/add_products", methods=['POST', 'PUT'])
def add_products():
    try:
        product_name = request.form['product_name']
        store = request.form['store']
        price = float(request.form['price'])

        new_product = emag_db.add_product(config, product_name, store, price)
        data = emag_db.read_products(config)
        return render_template('home.html', data=data)
    except Exception as e:
        return f"Error in adding the product: {e}"


if __name__ == '__main__':
    app.run()
