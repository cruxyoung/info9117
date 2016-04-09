# all the imports

import time
from sqlite3 import dbapi2 as sqlite3
from hashlib import md5
from datetime import datetime
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g, flash, _app_ctx_stack
from werkzeug import check_password_hash, generate_password_hash
from contextlib import closing




# configuration
DATABASE = '/tmp/flaskr.db'
DEBUG = False
#DEBUG = True

SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)

def serve_forever():
    app.run()

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with Werkzeug server")
    func()
    
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()




def query_db(query, args=(),one=False):
    cur = g.db.execute(query, args)
    rv = cur.fetchall()
    return(rv[0] if rv else None) if one else rv

def get_user_id(username):
    rv = query_db('select user_id from user where username = ?',
                  [username], one=True)
    return rv[0] if rv else None

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/shutdown')
def shutdown():
    shutdown_server()
    
@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method =='POST':

        user = query_db('''select * from user where username = ?''',
                        [request.form['username']], one=True)
        print(user)
        passwordd = query_db('''select passwd from user where username = ?''',
                        [request.form['username']], one=True)
        password = request.form['password']
        
        if user is None:
            error = 'Invalid username' 
            
        '''elif not check_password_hash(user['passwd'],
                                     request.form['password']):
            error = 'Invalid password'
        else:
            flash('You were logged in')
            session['user_id'] = user['user_id']
            return redirect(url_for('show_entries'))'''
        if user is not None:
    
            if passwordd[0] == password:
                flash('You were logged in')
            
                return redirect(url_for('show_entries'))
            elif passwordd != password: 
                error = "Invalid password"
        
        
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

@app.route('/register',methods=['GET', 'POST'])
def register():
    error = None
    if request.method =='POST':
        if not request.form['username']:
            error = 'You have to enter a username'
        elif not request.form['password']:
            error = 'You have to enter a password'
        elif request.form['password']!=request.form['password2']:
            error = 'The two passwords do not match'
        elif get_user_id(request.form['username']) is not None:
            error = 'The username is already taken'
        else:
            db = g.db
            db.execute('''insert into user (
              username, passwd) values (?, ?)''',
              [request.form['username'],
               request.form['password']])
            db.commit()
            flash('You were successfully registered and can login now')
            return redirect(url_for('login'))
    return render_template('register.html', error=error)



if __name__ == '__main__':
    serve_forever()

