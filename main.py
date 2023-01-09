
from flask import Flask, redirect, url_for, request, render_template
from flask_login import LoginManager, login_user, logout_user, login_required, UserMixin, current_user
from common import yellow, cyan, log, green, getUsers

app = Flask(__name__)
login_manager = LoginManager(app)

# Create a fake user class for example purposes
class User(UserMixin):
    def __init__(self, id, password):
        self.id = id
        self.name = id # // str(id)
        self.password = password
users = {}

# Create a user with the id 1
#users["a"] = User("a")

# Create a login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    cyan("login")
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        yellow( "{}   {}".format(username, password))
        if username in users:
            if password == users[username].password:
                login_user(users[username])

                return redirect(url_for('protected'))
            else:
                print("username2: " + users[username].username) 
                print("password2: " + users[username].password) 
        else:
            print("username is NOPE " + username )
            print(users)
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=password name=password>
            <p><input type=submit value=Login>
            Hello
        </form>
    '''
# Create a protected route
@app.route('/protected')
@login_required
def protected():
    cyan("protected")
    # return 'Logged in as: ' + 
    # message = { 
    #     "status":"status",
    #     "projectpath":"projectpath", 
    #     "kittycat":"kittycat"
    # }
    return render_template('main.html', username=current_user.name)



# Create a logout route
@app.route('/logout')
def logout():
    cyan("logged out")
    logout_user()
    return 'Logged out'

# Tell Flask-Login how to load a user
@login_manager.user_loader
def load_user(user_id):
    cyan("load_user")
    # return users.get(int(user_id))
    return users.get(user_id)

def setUsers():
    u = getUsers()
    for x in u:
        users[x] = User(x, u[x]) 
    yellow("setUsers has {} many".format( len(users)))

if __name__ == '__main__':
    setUsers()
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'

    cyan("http://34.83.236.108:4040 with database at data/dispense.db")
    cyan("http://localhost:4040 with database at data/dispense.db")

    from waitress import serve
    serve(app, host="0.0.0.0", port=4040)
