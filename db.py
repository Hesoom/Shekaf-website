# import sqlite3
# import os

# # Path to the database
# base = r"D:\100 Days of Code\96 Day 96 - Professional Portfolio Project - [Web Development] [UdemyIran.Com]\shekaf-store"
# db_path = os.path.join(base, "instance", "store.db")

# # Connect to the database
# conn = sqlite3.connect(db_path)
# c = conn.cursor()

# # List of items to insert

# "D:\100 Days of Code\96 Day 96 - Professional Portfolio Project - [Web Development] [UdemyIran.Com]\shekaf-store\static\img\items"

# items = [
#     ('Taxi Driver', 50000, '/static/img/items/7.jpg'),
#     ('No Sleep', 50000, '/static/img/items/1.jpg'),
#     ('Adulthood', 50000, '/static/img/items/2.jpg'),
#     ('Be Yourself', 50000, '/static/img/items/3.jpg'),
#     ('The Hangover', 50000, '/static/img/items/4.jpg'),
#     ('Pare Parvaz', 50000, '/static/img/items/5.jpg'),
#     ('Procrastination', 50000, '/static/img/items/6.jpg'),
#     ('Shining', 50000, '/static/img/items/8.jpg'),
#     ('Clockwork Orange', 50000, '/static/img/items/9.jpg')
# ]

# # Insert items (id will auto-increment)
# c.executemany("INSERT INTO items (name, price, image_url) VALUES (?, ?, ?)", items)

# # Commit and close
# conn.commit()
# conn.close()

# print("Items inserted successfully!")
