from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json(file_path='products.json'):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv(file_path='products.csv'):
    products = []
    try:
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    product = {
                        'id': int(row['id']),
                        'name': row['name'],
                        'category': row['category'],
                        'price': float(row['price'])
                    }
                    products.append(product)
                except (ValueError, KeyError):
                    continue
    except Exception:
        pass
    return products

def read_sqlite(db_path='products.db'):
    products = []
    try:
        conn = sqlite3.connect(db_path)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
            })
        conn.close()
    except Exception:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    id_param = request.args.get('id')
    error = None
    products = []

    if source == 'json':
        products = read_json()
    elif source == 'csv':
        products = read_csv()
    elif source == 'sql':
        products = read_sqlite()
    else:
        error = "Wrong source"

    if not error and id_param:
        try:
            id_val = int(id_param)
            filtered = [p for p in products if p.get('id') == id_val]
            if not filtered:
                error = "Product not found"
            else:
                products = filtered
        except ValueError:
            error = "Invalid id parameter"

    return render_template('product_display.html', products=products, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

