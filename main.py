
from flask import Flask, redirect, url_for, request, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from common import yellow, cyan, green, magenta # , getUsers
import sqlite3
import json
from datalayer.b import goat

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

    conn = sqlite3.connect('datalayer/dispense.db')
    cursor = conn.cursor()
    sqlfetch = "select * from stores where merchantId = 1;"; 
    cursor.execute(sqlfetch)
    stores = cursor.fetchall()

    # asJson = json.dumps( stores )

    # print( asJson )
    conn.close()

    asJson = ["hello","there"]
    return render_template('index_is_logged_in.html', stores=stores, attempt=14, id=merchantId, username=username)

@app.route('/')
def lulu():
    cyan("index")
    return render_template('index_not_logged_in.html')


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
    cyan("http://34.83.236.108:4040 with database at data/dispense.db")
    cyan("http://localhost:4040 with database at data/dispense.db")

    from waitress import serve
    serve(app, host="0.0.0.0", port=4040)
