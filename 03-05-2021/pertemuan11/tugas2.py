import mysql.connector
# Mengkoneksikan MySQL ke Python

# connect ke mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="tugas_2_LanaSaifulAqil"
)

mycursor = mydb.cursor()

# Membuat Database
# mycursor.execute("CREATE DATABASE tugas_2_LanaSaifulAqil")

# buat tabel
mycursor.execute(
    "CREATE TABLE WISHLIST (id INT PRIMARY KEY, nama_produk VARCHAR(30), jumlah INT, total_harga INT, link_produk VARCHAR(50))")

# insert data
sql = "INSERT INTO WISHLIST (id, nama_produk, jumlah, total_harga, link_produk) VALUES (1, 'Mouse Gaming', 2, 498000, 'shorturl.at/bcBOT')"

mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO WISHLIST(id, nama_produk, jumlah, total_harga, link_produk) VALUES(2, 'Mechanical Keyboard', 1, 199000, 'shorturl.at/etzBZ')"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO WISHLIST(id, nama_produk, jumlah, total_harga, link_produk) VALUES(3, 'Macbook', 1, 18649000, 'shorturl.at/xAHM7')"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO WISHLIST(id, nama_produk, jumlah, total_harga, link_produk) VALUES(4, 'iPhone 12', 1, 12000000, 'shorturl.at/gtyG5')"
mycursor.execute(sql)
mydb.commit()

sql = "INSERT INTO WISHLIST(id, nama_produk, jumlah, total_harga, link_produk) VALUES(5, 'Meja Kursi Gaming Set', 1, 2418000, 'shorturl.at/dijuD')"
mycursor.execute(sql)
mydb.commit()

# update table
mycursor.execute(
    "UPDATE WISHLIST SET nama_produk = 'iPhone 11', total_harga = 19592000, link_produk = 'shorturl.at/hwIX9' WHERE id = 4")
mydb.commit()

# delete data from table
mycursor.execute("DELETE FROM WISHLIST WHERE id = 5")
mydb.commit()

# # drop table
# mycursor.execute("DROP TABLE WISHLIST")
# mydb.commit()
