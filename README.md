# dispense_version3
https://github.com/mulefish/dispense_version3

# DB 
Postgres? Currently focusing on SQLite, because it is a easier. Later TODO: Port to PostGres.

# DB Local machine commands: 
pmontgomery@FVFH51FAQ6LW bin % brew services stop postgresql
#(base) pmontgomery@FVFH51FAQ6LW bin % brew services start postgresql
#(base) pmontgomery@FVFH51FAQ6LW bin % psql -U pmontgomery -H
 
# DB TODO: 
1 - settle on a DB schema 
2 - Get more solid on Google Cloud DB 
3 - Port local DB to Google Cloud DB 

# Flow

```mermaid
    flowchart TB
    A[Splash page]
    TheMerchant[Login]
    DB[DB]
    D[Pick stores]
    E[Pick products]
    F[Money]
    QR[QR]
    H[Pick vending machine]
    Inventory[Upload inventory]


    A-- log in -->TheMerchant
    subgraph Merchant
        TheMerchant-->H
        H-->Inventory
    end
    
    A-->D
    subgraph Enduser
        D-->E
        E-->F
        F-->QR
    end
    D-->DB
    DB-->D

    TheMerchant-->DB
    DB-->TheMerchant
    Inventory-->DB

```
