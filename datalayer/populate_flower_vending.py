import sqlite3
conn = sqlite3.connect('dispense.db')

flower_data = [
    {
        "vendingId":1,
        "merchantId":1,
        "storeId": 1,
        "strain": "Peanut Butter Pie",
        "type": "Indica",
        "farm": "Noble",
        "weight_in_grams": 1.09,
        "thc_percent": 27.30,
        "cbd_percent": 0.09,
        "harvest": "10/22/19",
        "description": "Indoor/outdoor terpenes",
        "price": 12.00,
        "count":10
    },
    {
        "vendingId":1,
        "merchantId":1,
        "storeId": 1,
        "strain": "Sunset Sherbert",
        "type": "Hybrid",
        "farm": "HighWinds",
        "weight_in_grams": 1.01,
        "thc_percent": 28.40,
        "cbd_percent": 0.10,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 11.00,
        "count":10
    },
    {
        "vendingId":1,
        "merchantId":1,
        "storeId": 1,
        "strain": "Headdog",
        "type": "Hybrid",
        "farm": "Heros of the Farm",
        "weight_in_grams": 1.04,
        "thc_percent": 26.64,
        "cbd_percent": 0.07,
        "harvest": "11/14/19",
        "description": "Indoor/outdoor terpenes",
        "price": 8.00,
        "count":10
    },
    {
        "vendingId":1,
        "merchantId":1,
        "storeId": 1,
        "strain": "OG KB",
        "type": "Indica",
        "farm": "Makru Farms",
        "weight_in_grams": 1.04,
        "thc_percent": 25.03,
        "cbd_percent": 0.09,
        "harvest": "10/21/19",
        "description": "Indoor/outdoor terpenes",
        "price": 10.00,
        "count":10
    },    {
        "vendingId":1,
        "merchantId":1,
        "storeId": 1,
        "strain": "Lost Cause",
        "type": "Sativa",
        "farm": "Trichome",
        "weight_in_grams": 1.08,
        "thc_percent": 22.06,
        "cbd_percent": 0.00,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 9.00,
        "count":10
    },    
    ###
    {
        "vendingId":2,
        "merchantId":1,
        "storeId": 1,
        "strain": "Peanut Butter Pie",
        "type": "Indica",
        "farm": "Noble",
        "weight_in_grams": 1.09,
        "thc_percent": 27.30,
        "cbd_percent": 0.09,
        "harvest": "10/22/19",
        "description": "Indoor/outdoor terpenes",
        "price": 12.00,
        "count":10
    },
    {
        "vendingId":2,
        "merchantId":1,
        "storeId": 1,
        "strain": "Sunset Sherbert",
        "type": "Hybrid",
        "farm": "HighWinds",
        "weight_in_grams": 1.01,
        "thc_percent": 28.40,
        "cbd_percent": 0.10,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 11.00,
        "count":10
    },
    {
        "vendingId":2,
        "merchantId":1,
        "storeId": 1,
        "strain": "Headdog",
        "type": "Hybrid",
        "farm": "Heros of the Farm",
        "weight_in_grams": 1.04,
        "thc_percent": 26.64,
        "cbd_percent": 0.07,
        "harvest": "11/14/19",
        "description": "Indoor/outdoor terpenes",
        "price": 8.00,
        "count":10
    },
    {
        "vendingId":2,
        "merchantId":1,
        "storeId": 1,
        "strain": "OG KB",
        "type": "Indica",
        "farm": "Makru Farms",
        "weight_in_grams": 1.04,
        "thc_percent": 25.03,
        "cbd_percent": 0.09,
        "harvest": "10/21/19",
        "description": "Indoor/outdoor terpenes",
        "price": 10.00,
        "count":10
    },    
    {
        "vendingId":2,
        "merchantId":1,
        "storeId": 1,
        "strain": "Lost Cause",
        "type": "Sativa",
        "farm": "Trichome",
        "weight_in_grams": 1.08,
        "thc_percent": 22.06,
        "cbd_percent": 0.00,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 9.00,
        "count":10
    },
    ###  
        {
        "vendingId":3,
        "merchantId":1,
        "storeId": 2,
        "strain": "Peanut Butter Pie",
        "type": "Indica",
        "farm": "Noble",
        "weight_in_grams": 1.09,
        "thc_percent": 27.30,
        "cbd_percent": 0.09,
        "harvest": "10/22/19",
        "description": "Indoor/outdoor terpenes",
        "price": 12.00,
        "count":10
    },
    {
        "vendingId":3,
        "merchantId":1,
        "storeId": 2,
        "strain": "Sunset Sherbert",
        "type": "Hybrid",
        "farm": "HighWinds",
        "weight_in_grams": 1.01,
        "thc_percent": 28.40,
        "cbd_percent": 0.10,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 11.00,
        "count":10
    },
    {
        "vendingId":3,
        "merchantId":1,
        "storeId": 2,
        "strain": "Headdog",
        "type": "Hybrid",
        "farm": "Heros of the Farm",
        "weight_in_grams": 1.04,
        "thc_percent": 26.64,
        "cbd_percent": 0.07,
        "harvest": "11/14/19",
        "description": "Indoor/outdoor terpenes",
        "price": 8.00,
        "count":10
    },
    {
        "vendingId":3,
        "merchantId":1,
        "storeId": 2,
        "strain": "OG KB",
        "type": "Indica",
        "farm": "Makru Farms",
        "weight_in_grams": 1.04,
        "thc_percent": 25.03,
        "cbd_percent": 0.09,
        "harvest": "10/21/19",
        "description": "Indoor/outdoor terpenes",
        "price": 10.00,
        "count":10
    },    {
        "vendingId":3,
        "merchantId":1,
        "storeId": 2,
        "strain": "Lost Cause",
        "type": "Sativa",
        "farm": "Trichome",
        "weight_in_grams": 1.08,
        "thc_percent": 22.06,
        "cbd_percent": 0.00,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 9.00,
        "count":10
    },
        ###  
        {
        "vendingId":4,
        "merchantId":2,
        "storeId": 3,
        "strain": "Peanut Butter Pie",
        "type": "Indica",
        "farm": "Noble",
        "weight_in_grams": 1.09,
        "thc_percent": 27.30,
        "cbd_percent": 0.09,
        "harvest": "10/22/19",
        "description": "Indoor/outdoor terpenes",
        "price": 12.00,
        "count":10
    },
    {
        "vendingId":4,
        "merchantId":2,
        "storeId": 3,
        "strain": "Sunset Sherbert",
        "type": "Hybrid",
        "farm": "HighWinds",
        "weight_in_grams": 1.01,
        "thc_percent": 28.40,
        "cbd_percent": 0.10,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 11.00,
        "count":10
    },
    {
        "vendingId":4,
        "merchantId":2,
        "storeId": 3,
        "strain": "Headdog",
        "type": "Hybrid",
        "farm": "Heros of the Farm",
        "weight_in_grams": 1.04,
        "thc_percent": 26.64,
        "cbd_percent": 0.07,
        "harvest": "11/14/19",
        "description": "Indoor/outdoor terpenes",
        "price": 8.00,
        "count":10
    },
    {
        "vendingId":4,
        "merchantId":2,
        "storeId": 3,
        "strain": "OG KB",
        "type": "Indica",
        "farm": "Makru Farms",
        "weight_in_grams": 1.04,
        "thc_percent": 25.03,
        "cbd_percent": 0.09,
        "harvest": "10/21/19",
        "description": "Indoor/outdoor terpenes",
        "price": 10.00,
        "count":10
    },    {
        "vendingId":4,
        "merchantId":2,
        "storeId": 3,
        "strain": "Lost Cause",
        "type": "Sativa",
        "farm": "Trichome",
        "weight_in_grams": 1.08,
        "thc_percent": 22.06,
        "cbd_percent": 0.00,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 9.00,
        "count":10
    },
            ###  
        {
        "vendingId":5,
        "merchantId":2,
        "storeId": 4,
        "strain": "Peanut Butter Pie",
        "type": "Indica",
        "farm": "Noble",
        "weight_in_grams": 1.09,
        "thc_percent": 27.30,
        "cbd_percent": 0.09,
        "harvest": "10/22/19",
        "description": "Indoor/outdoor terpenes",
        "price": 12.00,
        "count":10
    },
    {
        "vendingId":5,
        "merchantId":2,
        "storeId": 4,
        "strain": "Sunset Sherbert",
        "type": "Hybrid",
        "farm": "HighWinds",
        "weight_in_grams": 1.01,
        "thc_percent": 28.40,
        "cbd_percent": 0.10,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 11.00,
        "count":10
    },
    {
        "vendingId":5,
        "merchantId":2,
        "storeId": 4,
        "strain": "Headdog",
        "type": "Hybrid",
        "farm": "Heros of the Farm",
        "weight_in_grams": 1.04,
        "thc_percent": 26.64,
        "cbd_percent": 0.07,
        "harvest": "11/14/19",
        "description": "Indoor/outdoor terpenes",
        "price": 8.00,
        "count":10
    },
    {
        "vendingId":5,
        "merchantId":2,
        "storeId": 4,
        "strain": "OG KB",
        "type": "Indica",
        "farm": "Makru Farms",
        "weight_in_grams": 1.04,
        "thc_percent": 25.03,
        "cbd_percent": 0.09,
        "harvest": "10/21/19",
        "description": "Indoor/outdoor terpenes",
        "price": 10.00,
        "count":11
    },    {
        "vendingId":5,
        "merchantId":2,
        "storeId": 4,
        "strain": "Lost Cause",
        "type": "Sativa",
        "farm": "Trichome",
        "weight_in_grams": 1.08,
        "thc_percent": 22.06,
        "cbd_percent": 0.00,
        "harvest": "11/05/19",
        "description": "Indoor/outdoor terpenes",
        "price": 9.00,
        "count":9
    }



]


if __name__ == "__main__":
    TABLE_NAME = "vending_flowers"
    cursor = conn.cursor()

    table = """ CREATE TABLE vending_flowers (
            vendingId INT,
            merchantId INT,
            storeId INT,
            strain VARCHAR(255),
            type VARCHAR(255),
            farm VARCHAR(50),
            weight_in_grams REAL,
            thc_percent REAL,
            cbd_percent REAL,
            harvest VARCHAR(9),
            description VARCHAR(255),
            price REAL,
            count INT
        ); """

    cursor.execute("DROP TABLE IF EXISTS {}".format(TABLE_NAME))
    cursor.execute(table)
    

    for x in flower_data:
        sql = "INSERT INTO {} VALUES ({},{},{}, '{}','{}','{}','{}','{}','{}','{}','{}', {},{})".format(
            TABLE_NAME, x["vendingId"], x["merchantId"], x["storeId"], x["strain"], x["type"], x["farm"], x["weight_in_grams"], x["thc_percent"], x["cbd_percent"], x["harvest"], x["description"], x["price"], x["count"])
        cursor.execute(sql)

    print("Created the table '{}' and inserted {} rows into it".format(
        TABLE_NAME, len(flower_data)))

    conn.commit()
    conn.close()
