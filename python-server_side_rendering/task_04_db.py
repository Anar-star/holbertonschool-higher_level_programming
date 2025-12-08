#!/usr/bin/env python3
import sqlite3
from flask import Flask, request, render_template
import json
import csv

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to our website"

@app.route('/products')
def products():
    source = request.args.get('source')
    error = ""
    data = []
    if str(source) == 'json':
        try:
            with open('./products.json', 'r') as p_json:
                data = json.load(p_json)
        except FileNotFoundError:
                print("JSON file Not Found")

    elif str(source) == 'csv':
        data = []
        try:
            with open('./products.csv', 'r') as p_csv:
                data_csv = csv.DictReader(p_csv)
                for i in data_csv:
                    data.append(i)
        except FileNotFoundError:
                print("CSV file Not Found")
    elif source == 'sql':
        try:
            conn = sqlite3.connect('products.db')
            curr = conn.cursor()

            curr.execute('''SELECT * FROM Products''')
            rows = curr.fetchall()
            table_heads = [description[0] for description in curr.description]
            data = [dict(zip(table_heads, row)) for row in rows]
            print(data)
        except Exception as e:
            print("Connection could not establish")
            print(e)

    else:
        return('Wrong source')

    try:
        id = request.args.get('id')
        sel_data = None
        for i in data:
            if int(i.get('id')) == int(id):
                sel_data = i
                break
        if (sel_data is None):
            error = "Product not found"
        else:
            data = [sel_data]
    except Exception:
        pass
    return render_template('product_display.html', products=data, error=error)




def create_database():


    conn = sqlite3.connect('products.db')


    cursor = conn.cursor()


    cursor.execute('''


        CREATE TABLE IF NOT EXISTS Products (


            id INTEGER PRIMARY KEY,


            name TEXT NOT NULL,


            category TEXT NOT NULL,


            price REAL NOT NULL


        )


    ''')





    cursor.execute("DELETE FROM Products")





    cursor.execute('''


        INSERT INTO Products (id, name, category, price)


        VALUES


        (1, 'Laptop', 'Electronics', 799.99),


        (2, 'Coffee Mug', 'Home Goods', 15.99)


    ''')





    conn.commit()


    conn.close()





if __name__ == '__main__':
    #create_database()
    app.run(debug=True, port=5000)
