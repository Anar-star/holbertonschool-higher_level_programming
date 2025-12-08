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

    if source == 'json':
        try:
            with open('./products.json', 'r') as p_json:
                data = json.load(p_json)
        except FileNotFoundError:
                print("JSON file Not Found")

    elif source == 'csv':
        data = []
        try:
            with open('./products.csv', 'r') as p_csv:
                data_csv = csv.DictReader(p_csv)
                for i in data_csv:
                    data.append(data_csv)
        except FileNotFoundError:
                print("CSV file Not Found")

    try:
        id = request.args.get('id')
        sel_data = []
        for i in data:
            if i.get('id') == id:
                sel_data = i
                break
        if len(sel_data) == 0:
            error = "Product not found"
        else:
            data = sel_data
    except Exception:
        pass

    else:
        return('Wrong source')

    return render_template('product_display.html', products=data, error=error)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

