import sqlite3
import re
from flask import Flask, request, g, render_template, redirect, url_for, jsonify

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
        # Kiểm tra xem username và password có chứa các ký tự đặc biệt của SQL Injection không
        is_username_valid = re.match(r"^[a-zA-Z0-9_]+$", username)
        is_password_valid = re.match(r"^[a-zA-Z0-9_@$!%*?&]+$", password)

        if not is_username_valid or not is_password_valid:
            error = "Thông tin nhập vào không hợp lệ"
            return render_template('login.html', error=error)

        # Sử dụng dấu ? làm placeholder để bảo vệ an toàn
        query = "SELECT * FROM users WHERE username = ? AND password = ?"
        
        db = get_db()   
        cursor = db.cursor()
        try:
            # Truyền tham số dưới dạng một tuple an toàn
            cursor.execute(query, (username, password))
            user = cursor.fetchone()
            
            if user:
                return render_template('login_success.html', user=user, query=query)
            else:
                error = "Tên đăng nhập hoặc mật khẩu không chính xác."
        except Exception as e:
            error = "Đã xảy ra lỗi hệ thống."
            
    return render_template('login.html', error=error)

@app.route('/products')
def products():
    category = request.args.get('category', 'Electronics')
    #Sử dụng dấu ? làm placeholder cho tham số danh mục
    query = "SELECT * FROM products WHERE category = ?"
    
    db = get_db()
    cursor = db.cursor()
    products = []
    error = None
    
    try:
        # Truyền tham số dưới dạng tuple an toàn (category,)
        cursor.execute(query, (category,))
        products = cursor.fetchall()
    except Exception as e:
        # Ẩn thông báo lỗi SQL chi tiết để tránh rò rỉ cấu trúc
        error = "Đã xảy ra lỗi khi tải danh sách sản phẩm."
        
    return render_template('products.html', products=products, category=category, error=error)
@app.route('/check_user')
def check_user():
    return render_template('lookup.html')

@app.route('/api/check_user', methods=['POST'])
def api_check_user():
    username = request.form.get('username')
    query = "SELECT id FROM users WHERE username = ?"
    
    db = get_db()
    cursor = db.cursor()
    
    try:
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        if user:
            return jsonify({"exists": True, "message": "User exists!"})
        else:
            return jsonify({"exists": False, "message": "User not found."})
    except:
        return jsonify({"exists": False, "message": "User not found (or error)."})

if __name__ == '__main__':
    print("Running on http://127.0.0.1:5000")
    app.run(debug=True)
