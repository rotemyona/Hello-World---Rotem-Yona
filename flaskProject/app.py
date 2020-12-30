from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('CV_Rotem_Yona.html')


@app.route('/userlist')
def hello_userlist():
    return render_template('UserList.html')


@app.route('/assignment8')
def hello_new_world():
    return render_template('assignment8.html',
                           user={'firstname': "Rotem", 'lastname': "Yona"},
                           hobbies=['Music', 'Food', 'Dance'])


@app.route('/assignemt8part2')
def replace():
    return render_template('assignemt8part2.html')


if __name__ == '__main__':
    app.run()
