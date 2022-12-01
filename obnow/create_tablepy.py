import sqlite3

db_mat = sqlite3.connect(r'D:\kursach\obnow\material_accounting.db')
cur=db_mat.cursor()
cur.execute("""CREATE TABLE material_accounting(
	id_m INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(50),
	count INTEGER,
    price INTEGER
)""")
db_mat.commit()

# db_buy = sqlite3.connect(r'D:\kursach\Buy.db')
# cur_buy=db_buy.cursor()
# cur_buy.execute("""CREATE TABLE buy(
# 	id_buy INTEGER PRIMARY KEY AUTOINCREMENT,
# 	name VARCHAR(50),
# 	count INTEGER
#     price INTEGER
# )""")
# db_buy.commit()


cur.execute("""INSERT INTO material_accounting(name,count,price) VALUES('Дрожжи',100,20)""")
cur.execute("""INSERT INTO material_accounting(name,count,price) VALUES('Солод',50,100)""")
cur.execute("""INSERT INTO material_accounting(name,count,price) VALUES('Хлеб',72,15)""")
cur.execute("""INSERT INTO material_accounting(name,count,price) VALUES('Молоко',132,25)""")
cur.execute("""INSERT INTO material_accounting(name,count,price) VALUES('Яблоки',14,28)""")
cur.execute("""INSERT INTO material_accounting(name,count,price) VALUES('Консерванты',140,200)""")
db_mat.commit()

