from flask import Flask, render_template, request, json
from flask.ext.mysql import MySQL
from werkzeug import generate_password_hash, check_password_hash
import db

app = Flask(__name__)

@app.route('/')
def main():
    print('toMain')
    return render_template('index.html')


@app.route('/signUp')
def signUp():
    print('toSignUp')
    return render_template('signUp.html')

@app.route('/v1/score?<things>', methods=['POST', 'GET'])
def compute_score(things):
    if request.method == 'POST':
        print things
        # if kwargs is not None:
        #     print'YOooooOoo'
        #     for key, value in kwargs.iteritems():
        #         print "%s == %s" %(key,value)
        return 'Hi'


@app.route('/v1/user/<username>', methods=['GET'])
def show_user(username):
    user = db.find_user_by_username(username)
    print(user.__dict__)
    return user.first_name


@app.route('/v1/user', methods=['POST', 'DELETE'])
def manage_user():
    if request.method == 'POST':
        first_name = request.form['signUp_firstName']
        last_name = request.form['signUp_lastName'] or None
        username = request.form['signUp_username']
        password = request.form['signUp_password']

        # Validate values
        if first_name and username and password:
            hashed_password = generate_password_hash(password)
            db.create_user(first_name, last_name, username, hashed_password)
            return json.dumps({'html':'<span>All fields good !!</span>'})
        else:
            return json.dumps({'html':'<span>Enter the required fields</span>'})

    elif request.method == 'DELETE':
        # id = request.form['id']
        username = request.form['username']
        password = request.form['password']
        # Secure enough?

        if username and password:
            user = db.find_user_by_username(username)
            if check_password_hash(user.password, password):
                print('Yepp they match')
                db.delete_user(username)
                return json.dumps({'deleted': 'ok'})

        return json.dumps({'error': 'missing user or password'}), 400


if __name__ == '__main__':
    db.init()
    app.run(debug=True)
