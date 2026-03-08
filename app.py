import sqlite3
from flask import Flask, request, g, render_template, jsonify
import traceback

app = Flask(__name__)

def get_db():
    if 'db' not in g:
        try:
            g.db = sqlite3.connect('database.db')
            g.db.row_factory = sqlite3.Row
        except Exception as e:
            print(f"Database connection error: {e}")
            return None
    return g.db

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        
        db = get_db()   
        cursor = db.cursor()
        try:
            cursor.execute(query)
            user = cursor.fetchone()
            
            if user:
                return render_template('login_success.html', user=user, query=query)
            else:
                error = "Invalid credentials"
        except Exception as e:
            error = str(e)
            
    return render_template('login.html', error=error)

@app.route('/products')
def products():
    category = request.args.get('category', 'Electronics')
    query = f"SELECT * FROM products WHERE category = '{category}'"
    
    db = get_db()
    cursor = db.cursor()
    products = []
    error = None
    
    try:
        cursor.execute(query)
        products = cursor.fetchall()
    except Exception as e:
        full_traceback = traceback.format_exc().splitlines()
        error = full_traceback
        
    return render_template('products.html', products=products, category=category, error=error, query=query)
@app.route('/check_user')
def check_user():
    return render_template('lookup.html')

@app.route('/api/check_user', methods=['POST'])
def api_check_user():
    username = request.form.get('username')
    query = f"SELECT id FROM users WHERE username = '{username}'"
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        cursor.execute(query)
        user = cursor.fetchone()
        if user:
            return jsonify({"exists": True, "message": "User exists!"})
        else:
            return jsonify({"exists": False, "message": "User not found."})
    except Exception as e:
        full_traceback = traceback.format_exc().splitlines()
        return jsonify({"exists": False, "message": full_traceback})

if __name__ == '__main__':
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True)


