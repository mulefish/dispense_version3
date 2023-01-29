
from flask import Flask, redirect, url_for, request, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from common import yellow, cyan, green, magenta # , getUsers
import sqlite3
import json
from datalayer.do_selects import do_select
from flask import jsonify
# from datalayer.b import goat

app = Flask(__name__)
login_manager = LoginManager(app)

class User(UserMixin):
    def __init__(self, id, password):
        self.id = id
        self.name = id
        self.password = password
users = {}
user_ids = {} 

@app.route('/login', methods=['GET', 'POST'])
def login():
    cyan("login")

    if not 'username' in request.form or 'password' not in request.form: 
        yellow("reject")
        return render_template('index_not_logged_in.html')

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        yellow( "{}   {}".format(username, password))
        if username in users and password == users[username].password:
            login_user(users[username])
            return redirect(url_for('merchant'))
    return render_template('index_not_logged_in.html')


@app.route('/merchant')
@login_required
def merchant():
    cyan("merchant")
    username = current_user.name 
    merchantId= user_ids[username]
    green("username {} and merchantId {} " . format( username, merchantId ))

    conn = sqlite3.connect('datalayer/dispense.db')
    cursor = conn.cursor()
    sqlfetch = f"select * from stores where merchantId = {merchantId};"; 
    cursor.execute(sqlfetch)
    stores = cursor.fetchall()
    #print(stores)
    ###

    sqlfetch = f"select * from vending_machines where merchantId = {merchantId};"; 
    cursor.execute(sqlfetch)
    vending_machines = cursor.fetchall()
    # print(vending_machines )

    sqlfetch = f"select * from vending_flowers where merchantId = {merchantId};"; 
    cursor.execute(sqlfetch)
    vending_flowers = cursor.fetchall()
    # print(vending_machines )
    
    sqlfetch = f"select * from vending_prerolls where merchantId = {merchantId};"; 
    cursor.execute(sqlfetch)
    vending_prerolls = cursor.fetchall()
    # print(vending_machines )
    conn.close()

    green("vending_machines")
    print(vending_machines)
    return render_template('index_is_logged_in.html', vending_flowers=vending_flowers,  vending_prerolls=vending_prerolls, merchantName=username,vending_machines=vending_machines,  stores=stores, attempt=14, id=merchantId, username=username)

@app.route('/')
def lulu():
    cyan("index")
    return render_template('index_not_logged_in.html')


@app.route('/vending')
@login_required
def vending():
    username = current_user.name 
    cyan("vending {}".format(username))    
    return render_template('vending.html', username=username )

@app.route('/get_vending_machine', methods=['POST'])
def get_vending_machine():
    cyan("get_vending_machine")

    obj = {
        "status":"Missing information"
    }
    if request.method == 'POST':
        x = request.get_json()
        if "storeId" in x and "merchantId" in x and "vendingId" in x:
            vendingId = x["vendingId"]
            storeId = x["storeId"]
            merchantId = x["merchantId"]
            #query = "select * from vending_flowers where vendingId = {} and merchantId = {} and storeId = {}".format(vendingId, merchantId, storeId)
            query = "select * from vending_flowers where vendingId = 1 and merchantId = 1 and storeId = 1"
            obj["query"] = query
            obj["status"] = "OK"
            obj["data"] = do_select(query)
    else:
        obj["status"] = "Incorrect HTTP verb"

    return jsonify(obj)
    





@app.route('/logout')
def logout():
    cyan("logged out")
    logout_user()
    return render_template('index_not_logged_in.html')

@login_manager.user_loader
def load_user(user_id):
    cyan("load_user")
    return users.get(user_id)

def setUsers():
    green("setUsers")
    conn = sqlite3.connect('datalayer/dispense.db')
    cursor = conn.cursor()
    sqlfetch = "select id, name, password  from merchants"; 
    cursor.execute(sqlfetch)
    row = cursor.fetchall()
    for x in row:
        id = x[0]
        username = x[1]
        password = x[2]
        msg = f"{id} {username} {password}"
        print(msg)
        users[username] = User(username, password) 
        user_ids[username] = id
    conn.close()

if __name__ == '__main__':
    setUsers()

    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.debug = True # REMOVE THIS ONCE IN PRODUCTION
    cyan("http://34.82.219.228:8080 with database at data/dispense.db")
    # cyan("http://localhost:4040 with database at data/dispense.db")

    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
