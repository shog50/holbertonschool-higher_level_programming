from flask import Flask, render_template, request
import json
import csv

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

