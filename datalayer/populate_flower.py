import sqlite3
from pretty_print import yellow, cyan, log, green
conn = sqlite3.connect('dispense.db')

flower_data = [
    {
        "strain": "Peanut Butter Pie",
        "type": "Indica",
        "farm": "Noble",
        "weight_in_grams": 1.09,
        "thc_percent": 27.30,
        "cbd_percent": 0.09,
        "harvest": "10/22/19",
        "description": "Indoor/outdoor terpenes",
        "price": 12.00,
    },
    {
        "strain": "Sunset Sherbert",
        "type": "Hybrid",
        "farm": "HighWinds",
        "weight_in_grams": 1.01,
        "thc_percent": 28.40,
        "cbd_percent": 0.10,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 11.00,
    },
    {
        "strain": "Headdog",
        "type": "Hybrid",
        "farm": "Heros of the Farm",
        "weight_in_grams": 1.04,
        "thc_percent": 26.64,
        "cbd_percent": 0.07,
        "harvest": "11/14/19",
        "description": "Indoor/outdoor terpenes",
        "price": 8.00,
    },
    {
        "strain": "OG KB",
        "type": "Indica",
        "farm": "Makru Farms",
        "weight_in_grams": 1.04,
        "thc_percent": 25.03,
        "cbd_percent": 0.09,
        "harvest": "10/21/19",
        "description": "Indoor/outdoor terpenes",
        "price": 10.00,
    },    {
        "strain": "Lost Cause",
        "type": "Sativa",
        "farm": "Trichome",
        "weight_in_grams": 1.08,
        "thc_percent": 22.06,
        "cbd_percent": 0.00,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 9.00,
    },
]


if __name__ == "__main__":
    TABLE_NAME = "flowers"
    cursor = conn.cursor()

    table = """ CREATE TABLE flowers (
            strain VARCHAR(255),
            type VARCHAR(255),
            farm VARCHAR(50),
            weight_in_grams REAL,
            thc_percent REAL,
            cbd_percent REAL,
            harvest VARCHAR(9),
            description VARCHAR(255),
            price REAL
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(TABLE_NAME))
    cursor.execute(table)

    for x in flower_data:
        sql = "INSERT INTO {} VALUES ('{}','{}','{}','{}','{}','{}','{}','{}', {})".format(
            TABLE_NAME, x["strain"], x["type"], x["farm"], x["weight_in_grams"], x["thc_percent"], x["cbd_percent"], x["harvest"], x["description"], x["price"])
        cursor.execute(sql)

    cyan("Created the table '{}' and inserted {} rows into it".format(
        TABLE_NAME, len(flower_data)))

    conn.commit()
    conn.close()
