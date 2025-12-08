#!/usr/bin/env python3
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
    products = []
    print(source)
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
    else:
        return('Wrong source')

    try:
        id = request.args.get('id')
        sel_data = None
        for i in data:
            print(i.get('id'))
            print(id)
            if int(i.get('id')) == int(id):
                sel_data = i
                break
        if (sel_data is None):
            error = "Product not found"
        else:
            data = [sel_data]
    except Exception:
        pass
    print(request.args.get('salam'))
    print(data)
    return render_template('product_display.html', products=data, error=error)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5000)

