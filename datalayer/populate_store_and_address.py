import sqlite3

conn = sqlite3.connect('dispense.db')

populate_store_and_address_data = [
    {
        "id":1,
        "name": "Super Fresh",
        "street": "2145 NE Martin Luther King Jr Blvd",
        "city": "Portland",
        "state": "Oregon",
        "zip": "97211",
        "url": "example.com",
        "img": "static/leaf.png",
        "phone": "503.123.1234",
        "lat":45.538720,
        "long":-122.662000
    },
    {
        "id":2,
        "name": "Happy Market",
        "street": "823 SW Naito Pkwy",
        "city": "Portland",
        "state": "Oregon",
        "zip": "97211",
        "url": "example.com",
        "img": "static/leaf.png",
        "phone": "503.123.1234",
        "lat":45.516500,
        "long":-122.673520

    },
    {
        "id":3,
        "name": "Shoal Farms",
        "street": "427 NW Broadway",
        "city": "Portland",
        "state": "Oregon",
        "zip": "97211",
        "url": "example.com",
        "img": "static/leaf.png",
        "phone": "503.123.1234",
        "lat":45.526348,
        "long":-122.677887

    },
    {
        "id":4,
        "name": "Paper Jolt Cannabis",
        "street": "4011 SE Belmont St",
        "city": "Portland",
        "state": "Oregon",
        "zip": "97211",
        "url": "example.com",
                "img": "static/leaf.png",
        "phone": "503.123.1234",
        "lat":45.516760,
        "long":-122.621370
    },

]


if __name__ == "__main__":
    TABLE_NAME = "stores"
    cursor = conn.cursor()

    table = """ CREATE TABLE stores (
            id INT,
            name VARCHAR(255),
            street VARCHAR(255),
            city VARCHAR(50),
            state VARCHAR(5),
            zip VARCHAR(5),
            url VARCHAR(255),
            img VARCHAR(255),
            phone VARCHAR(12),
            lat REAL, 
            long REAL
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(TABLE_NAME))
    cursor.execute(table)

    for x in populate_store_and_address_data:
        sql = "INSERT INTO {} VALUES ({}, '{}','{}','{}','{}','{}','{}','{}','{}', {}, {})".format(
            TABLE_NAME, x["id"], x["name"], x["street"], x["city"], x["state"], x["zip"], x["url"], x["img"], x["phone"], x["lat"], x["long"])
        print( sql )
        cursor.execute(sql)

    print("Created the table '{}' and inserted {} rows into it".format(
        TABLE_NAME, len(populate_store_and_address_data)))
    populate_store_and_address_data = cursor.execute('''SELECT * FROM stores''')
    conn.commit()
    conn.close()
