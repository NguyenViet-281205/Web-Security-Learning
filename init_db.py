from app import app, get_db

def init_db():
    with app.app_context():
        db = get_db()
        if not db:
            return
        cursor = db.cursor()
        cursor.execute("DROP TABLE IF EXISTS users")
        cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, password TEXT, is_admin INTEGER DEFAULT 0)")
        cursor.execute("INSERT INTO users (username, password, is_admin) VALUES ('jdoe', 'password123', 0)")
        cursor.execute("INSERT INTO users (username, password, is_admin) VALUES ('administrator', 'complex_password_123', 1)")
        cursor.execute("DROP TABLE IF EXISTS products")
        cursor.execute("CREATE TABLE products (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, category TEXT, description TEXT, price REAL, production_year INTEGER, material TEXT, stock_quantity INTEGER, manufacturer TEXT, warranty_months INTEGER)")
        products = [
            ('LG Monitor V2', 'Electronics', 'High quality monitor for your daily needs.', 49.99, 2022, 'Steel', 100, 'LG', 24),
            ('Zara Sweater Max', 'Clothing', 'High quality sweater for your daily needs.', 199.99, 2021, 'Wool', 10, 'Zara', 1),
            ('The Dark Programming Guide by Avery', 'Books', 'High quality programming guide for your daily needs.', 299.99, 2022, 'Recycled Paper', 200, 'Avery', 0),
            ('Dyson Pressure Cooker Lite', 'Home', 'High quality pressure cooker for your daily needs.', 199.99, 2021, 'Wood', 1000, 'Dyson', 24),
            ('Hasbro Remote Car Pro', 'Toys', 'High quality remote car for your daily needs.', 19.99, 2024, 'Plastic', 10, 'Hasbro', 0),
            ('Asus Laptop V2', 'Electronics', 'High quality laptop for your daily needs.', 149.99, 2020, 'Aluminum', 50, 'Asus', 24),
            ('Nike Jacket Plus', 'Clothing', 'High quality jacket for your daily needs.', 99.99, 2023, 'Leather', 500, 'Nike', 1),
            ('The Great Cookbook by Avery', 'Books', 'High quality cookbook for your daily needs.', 999.99, 2024, 'Paper', 50, 'Avery', 1),
            ('Bosch Air Purifier Lite', 'Home', 'High quality air purifier for your daily needs.', 999.99, 2022, 'Wood', 500, 'Bosch', 12),
            ('Lego Building Blocks Lite', 'Toys', 'High quality building blocks for your daily needs.', 199.99, 2021, 'Wood', 10, 'Lego', 1),
            ('Apple Inc. Laptop Classic', 'Electronics', 'High quality laptop for your daily needs.', 199.99, 2023, 'Steel', 500, 'Apple Inc.', 0),
            ('Zara T-Shirt V2', 'Clothing', 'High quality t-shirt for your daily needs.', 199.99, 2023, 'Denim', 200, 'Zara', 0),
            ('The Dark Programming Guide by Avery', 'Books', 'High quality programming guide for your daily needs.', 99.99, 2021, 'Hardcover', 50, 'Avery', 1),
            ('Instant Brands Pressure Cooker Classic', 'Home', 'High quality pressure cooker for your daily needs.', 299.99, 2022, 'Plastic', 500, 'Instant Brands', 6),
            ('Hasbro Doll Lite', 'Toys', 'High quality doll for your daily needs.', 19.99, 2022, 'Rubber', 10, 'Hasbro', 1),
            ('LG Camera X', 'Electronics', 'High quality camera for your daily needs.', 199.99, 2023, 'Glass', 50, 'LG', 12),
            ('Levi Strauss & Co. Sweater Classic', 'Clothing', 'High quality sweater for your daily needs.', 49.99, 2023, 'Wool', 500, 'Levi Strauss & Co.', 0),
            ('The Silent Programming Guide by Penguin', 'Books', 'High quality programming guide for your daily needs.', 199.99, 2020, 'Hardcover', 10, 'Penguin', 1),
            ('Dyson Pressure Cooker Lite', 'Home', 'High quality pressure cooker for your daily needs.', 29.99, 2023, 'Wood', 1000, 'Dyson', 6),
            ('Lego Remote Car Max', 'Toys', 'High quality remote car for your daily needs.', 199.99, 2021, 'Rubber', 500, 'Lego', 1),
            ('Asus Smartwatch Lite', 'Electronics', 'High quality smartwatch for your daily needs.', 19.99, 2024, 'Aluminum', 1000, 'Asus', 24),
            ('Nike Jeans Pro', 'Clothing', 'High quality jeans for your daily needs.', 29.99, 2023, 'Denim', 1000, 'Nike', 1),
            ('The Bright Biography by HarperCollins', 'Books', 'High quality biography for your daily needs.', 99.99, 2021, 'Paper', 1000, 'HarperCollins', 1),
            ('Panasonic Blender Ultra', 'Home', 'High quality blender for your daily needs.', 299.99, 2020, 'Ceramic', 100, 'Panasonic', 0),
            ('Lego Puzzle Max', 'Toys', 'High quality puzzle for your daily needs.', 49.99, 2021, 'Plastic', 1000, 'Lego', 0),
            ('Samsung Monitor Plus', 'Electronics', 'High quality monitor for your daily needs.', 99.99, 2023, 'Steel', 10, 'Samsung', 24),
            ('H&M Shorts Max', 'Clothing', 'High quality shorts for your daily needs.', 499.99, 2024, 'Polyester', 200, 'H&M', 0),
            ('The Bright Programming Guide by Penguin', 'Books', 'High quality programming guide for your daily needs.', 199.99, 2021, 'Recycled Paper', 100, 'Penguin', 0),
            ('Philips Air Purifier Lite', 'Home', 'High quality air purifier for your daily needs.', 29.99, 2024, 'Stainless Steel', 1000, 'Philips', 24),
            ('Fisher-Price Board Game Pro', 'Toys', 'High quality board game for your daily needs.', 299.99, 2020, 'Cardboard', 100, 'Fisher-Price', 1),
            ('Asus Smartphone V2', 'Electronics', 'High quality smartphone for your daily needs.', 19.99, 2024, 'Glass', 10, 'Asus', 0),
            ('H&M Sneakers Ultra', 'Clothing', 'High quality sneakers for your daily needs.', 499.99, 2023, 'Leather', 50, 'H&M', 1),
            ('The Dark History Book by HarperCollins', 'Books', 'High quality history book for your daily needs.', 29.99, 2021, 'Paper', 500, 'HarperCollins', 1),
            ('Dyson Air Purifier Lite', 'Home', 'High quality air purifier for your daily needs.', 299.99, 2021, 'Plastic', 10, 'Dyson', 24),
            ('Lego Puzzle V2', 'Toys', 'High quality puzzle for your daily needs.', 499.99, 2020, 'Cardboard', 100, 'Lego', 0),
            ('LG Tablet Pro', 'Electronics', 'High quality tablet for your daily needs.', 29.99, 2021, 'Steel', 500, 'LG', 0),
            ('H&M Sneakers X', 'Clothing', 'High quality sneakers for your daily needs.', 299.99, 2020, 'Leather', 10, 'H&M', 1),
            ('The Dark Cookbook by Penguin', 'Books', 'High quality cookbook for your daily needs.', 499.99, 2024, 'Hardcover', 500, 'Penguin', 0),
            ('Instant Brands Vacuum Cleaner Classic', 'Home', 'High quality vacuum cleaner for your daily needs.', 49.99, 2021, 'Ceramic', 10, 'Instant Brands', 6),
            ('Hasbro Board Game V2', 'Toys', 'High quality board game for your daily needs.', 299.99, 2022, 'Wood', 200, 'Hasbro', 0),
            ('LG Laptop Lite', 'Electronics', 'High quality laptop for your daily needs.', 499.99, 2024, 'Aluminum', 100, 'LG', 0),
            ('H&M Jeans Pro', 'Clothing', 'High quality jeans for your daily needs.', 99.99, 2020, 'Polyester', 50, 'H&M', 0),
            ('The Dark Biography by Penguin', 'Books', 'High quality biography for your daily needs.', 29.99, 2022, 'Paper', 100, 'Penguin', 0),
            ('Bosch Heater V2', 'Home', 'High quality heater for your daily needs.', 29.99, 2023, 'Wood', 50, 'Bosch', 6),
            ('Hasbro Remote Car V2', 'Toys', 'High quality remote car for your daily needs.', 29.99, 2021, 'Plastic', 100, 'Hasbro', 1),
            ('Sony Tablet Lite', 'Electronics', 'High quality tablet for your daily needs.', 199.99, 2023, 'Plastic', 100, 'Sony', 0),
            ('Levi Strauss & Co. T-Shirt X', 'Clothing', 'High quality t-shirt for your daily needs.', 19.99, 2022, 'Polyester', 50, 'Levi Strauss & Co.', 1),
            ('The Dark Biography by Avery', 'Books', 'High quality biography for your daily needs.', 299.99, 2024, 'Hardcover', 500, 'Avery', 1),
            ('Philips Heater Classic', 'Home', 'High quality heater for your daily needs.', 99.99, 2022, 'Wood', 500, 'Philips', 24),
            ('Fisher-Price Remote Car Ultra', 'Toys', 'High quality remote car for your daily needs.', 49.99, 2024, 'Rubber', 200, 'Fisher-Price', 1),
            ('Apple Inc. Tablet Lite', 'Electronics', 'High quality tablet for your daily needs.', 149.99, 2021, 'Glass', 1000, 'Apple Inc.', 12),
            ('Nike Socks Max', 'Clothing', 'High quality socks for your daily needs.', 49.99, 2021, 'Cotton', 100, 'Nike', 0),
            ('The Lost History Book by HarperCollins', 'Books', 'High quality history book for your daily needs.', 299.99, 2022, 'Recycled Paper', 500, 'HarperCollins', 1),
            ('Panasonic Vacuum Cleaner Ultra', 'Home', 'High quality vacuum cleaner for your daily needs.', 19.99, 2020, 'Wood', 500, 'Panasonic', 6),
            ('Hasbro Remote Car V2', 'Toys', 'High quality remote car for your daily needs.', 19.99, 2020, 'Plastic', 500, 'Hasbro', 0),
            ('Samsung Camera V2', 'Electronics', 'High quality camera for your daily needs.', 99.99, 2022, 'Steel', 100, 'Samsung', 12),
            ('Zara Sneakers Classic', 'Clothing', 'High quality sneakers for your daily needs.', 49.99, 2022, 'Leather', 10, 'Zara', 0),
            ('The Hidden Biography by Macmillan', 'Books', 'High quality biography for your daily needs.', 29.99, 2023, 'Hardcover', 50, 'Macmillan', 0),
            ('Bosch Blender Lite', 'Home', 'High quality blender for your daily needs.', 49.99, 2023, 'Ceramic', 10, 'Bosch', 0),
            ('Mattel Building Blocks Max', 'Toys', 'High quality building blocks for your daily needs.', 99.99, 2022, 'Rubber', 500, 'Mattel', 1),
            ('Sony Camera X', 'Electronics', 'High quality camera for your daily needs.', 99.99, 2020, 'Plastic', 500, 'Sony', 12),
            ('Zara Jeans Classic', 'Clothing', 'High quality jeans for your daily needs.', 19.99, 2024, 'Wool', 1000, 'Zara', 1),
            ('The Bright Cookbook by Avery', 'Books', 'High quality cookbook for your daily needs.', 99.99, 2020, 'Recycled Paper', 1000, 'Avery', 0),
            ('Instant Brands Air Purifier Classic', 'Home', 'High quality air purifier for your daily needs.', 499.99, 2021, 'Ceramic', 500, 'Instant Brands', 12),
            ('Fisher-Price Doll Ultra', 'Toys', 'High quality doll for your daily needs.', 999.99, 2024, 'Rubber', 200, 'Fisher-Price', 0),
            ('Sony Smartwatch Plus', 'Electronics', 'High quality smartwatch for your daily needs.', 199.99, 2023, 'Plastic', 10, 'Sony', 6),
            ('Zara Jeans Lite', 'Clothing', 'High quality jeans for your daily needs.', 99.99, 2023, 'Polyester', 100, 'Zara', 1),
            ('The Dark Novel by Penguin', 'Books', 'High quality novel for your daily needs.', 29.99, 2024, 'Recycled Paper', 50, 'Penguin', 0),
            ('Panasonic Vacuum Cleaner Pro', 'Home', 'High quality vacuum cleaner for your daily needs.', 49.99, 2020, 'Stainless Steel', 1000, 'Panasonic', 6),
            ('Mattel Doll Ultra', 'Toys', 'High quality doll for your daily needs.', 19.99, 2024, 'Rubber', 50, 'Mattel', 1),
            ('Sony Smartwatch Lite', 'Electronics', 'High quality smartwatch for your daily needs.', 199.99, 2022, 'Steel', 500, 'Sony', 24),
            ('Nike Jacket Lite', 'Clothing', 'High quality jacket for your daily needs.', 19.99, 2020, 'Wool', 10, 'Nike', 1),
            ('The Hidden Biography by Penguin', 'Books', 'High quality biography for your daily needs.', 49.99, 2021, 'Recycled Paper', 1000, 'Penguin', 0),
            ('Instant Brands Pressure Cooker Classic', 'Home', 'High quality pressure cooker for your daily needs.', 999.99, 2022, 'Stainless Steel', 200, 'Instant Brands', 12),
            ('Lego Remote Car Classic', 'Toys', 'High quality remote car for your daily needs.', 149.99, 2021, 'Rubber', 200, 'Lego', 1),
            ('Apple Inc. Smartwatch V2', 'Electronics', 'High quality smartwatch for your daily needs.', 149.99, 2024, 'Steel', 50, 'Apple Inc.', 12),
            ('H&M Jeans V2', 'Clothing', 'High quality jeans for your daily needs.', 149.99, 2023, 'Wool', 200, 'H&M', 1),
            ('The Hidden Cookbook by Penguin', 'Books', 'High quality cookbook for your daily needs.', 199.99, 2024, 'Recycled Paper', 200, 'Penguin', 1),
            ('Instant Brands Blender V2', 'Home', 'High quality blender for your daily needs.', 999.99, 2023, 'Plastic', 1000, 'Instant Brands', 6),
            ('Hasbro Puzzle V2', 'Toys', 'High quality puzzle for your daily needs.', 19.99, 2024, 'Cardboard', 100, 'Hasbro', 0),
            ('Asus Smartwatch V2', 'Electronics', 'High quality smartwatch for your daily needs.', 99.99, 2023, 'Titanium', 50, 'Asus', 6),
            ('Zara Jeans Lite', 'Clothing', 'High quality jeans for your daily needs.', 999.99, 2022, 'Denim', 200, 'Zara', 0),
            ('The Bright Science Book by Scholastic', 'Books', 'High quality science book for your daily needs.', 49.99, 2020, 'Recycled Paper', 500, 'Scholastic', 0),
            ('Dyson Vacuum Cleaner V2', 'Home', 'High quality vacuum cleaner for your daily needs.', 99.99, 2024, 'Plastic', 200, 'Dyson', 6),
            ('Bandai Board Game X', 'Toys', 'High quality board game for your daily needs.', 99.99, 2021, 'Wood', 10, 'Bandai', 0),
            ('Sony Monitor Classic', 'Electronics', 'High quality monitor for your daily needs.', 29.99, 2022, 'Plastic', 500, 'Sony', 12),
            ('Nike Jacket Ultra', 'Clothing', 'High quality jacket for your daily needs.', 299.99, 2023, 'Wool', 100, 'Nike', 0),
            ('The Bright Cookbook by Macmillan', 'Books', 'High quality cookbook for your daily needs.', 999.99, 2023, 'Hardcover', 10, 'Macmillan', 1),
            ('Panasonic Coffee Maker Max', 'Home', 'High quality coffee maker for your daily needs.', 499.99, 2020, 'Ceramic', 1000, 'Panasonic', 12),
            ('Bandai Doll Max', 'Toys', 'High quality doll for your daily needs.', 19.99, 2022, 'Cardboard', 50, 'Bandai', 1),
            ('LG Smartphone X', 'Electronics', 'High quality smartphone for your daily needs.', 99.99, 2020, 'Plastic', 200, 'LG', 24),
            ('Zara Jacket Plus', 'Clothing', 'High quality jacket for your daily needs.', 999.99, 2022, 'Denim', 10, 'Zara', 1),
            ('The Bright Novel by Avery', 'Books', 'High quality novel for your daily needs.', 29.99, 2021, 'Paper', 100, 'Avery', 1),
            ('Instant Brands Air Purifier Pro', 'Home', 'High quality air purifier for your daily needs.', 999.99, 2021, 'Wood', 50, 'Instant Brands', 12),
            ('Hasbro Doll Classic', 'Toys', 'High quality doll for your daily needs.', 19.99, 2022, 'Rubber', 1000, 'Hasbro', 1),
            ('Samsung Smartwatch Plus', 'Electronics', 'High quality smartwatch for your daily needs.', 299.99, 2024, 'Glass', 1000, 'Samsung', 12),
            ('Levi Strauss & Co. Jeans Max', 'Clothing', 'High quality jeans for your daily needs.', 49.99, 2020, 'Polyester', 50, 'Levi Strauss & Co.', 0),
            ('The Lost Novel by Macmillan', 'Books', 'High quality novel for your daily needs.', 49.99, 2021, 'Recycled Paper', 100, 'Macmillan', 0),
            ('Philips Vacuum Cleaner V2', 'Home', 'High quality vacuum cleaner for your daily needs.', 999.99, 2021, 'Wood', 50, 'Philips', 6),
            ('Mattel Board Game Classic', 'Toys', 'High quality board game for your daily needs.', 199.99, 2023, 'Cardboard', 10, 'Mattel', 0),
        ]
        cursor.executemany("INSERT INTO products (name, category, description, price, production_year, material, stock_quantity, manufacturer, warranty_months) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", products)

        db.commit()
        cursor.close()

if __name__ == '__main__':
    init_db()
    print('Database initialized.')
