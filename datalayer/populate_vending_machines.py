import sqlite3

conn = sqlite3.connect('dispense.db')

vending_machines = [
    {
        "id":1,
        "merchantId":1,
        "storeId": 1,
        "version": "version 1 : machine 1"
    },
    {
        "id":2,
        "merchantId":1,
        "storeId": 1,
        "version": "version 1 : machine 2"
    },
    {
        "id":3,
        "merchantId":1,
        "storeId": 2,
        "version": "version 1 : machine Becky"
    },
    {
        "id":4,
        "merchantId":2,
        "storeId": 3,
        "version": "version 1 : machine Jack"
    },
    {
        "id":5,
        "merchantId":2,
        "storeId": 4,
        "version": "version 1 : machine Samantha"
    },

]


if __name__ == "__main__":
    TABLE_NAME = "vending_machines"
    cursor = conn.cursor()

    table = """ CREATE TABLE vending_machines (
            id INT,
            merchantId INT,
            storeId INT,
            version VARCHAR(50)
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(TABLE_NAME))
    cursor.execute(table)

    for x in vending_machines:
        sql = "INSERT INTO {} VALUES ({}, {}, {}, '{}')".format(
            TABLE_NAME, x["id"], x["merchantId"], x["storeId"], x["version"])
        cursor.execute(sql)

    print("Created the table '{}' and inserted {} rows into it".format(
        TABLE_NAME, len(vending_machines)))
    conn.commit()
    conn.close()
