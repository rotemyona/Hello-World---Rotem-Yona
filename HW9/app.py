from flask import Flask, render_template, url_for, redirect, request, session

app = Flask(__name__)
app.secret_key = '103'


@app.route('/')
def home():
    return redirect(url_for('assignment9'))


@app.route('/assignment9', methods=['GET', 'POST'])
def assignment9():

    search, username, = '', ''
    users = ({'Name': "Michael Lawson", 'mail': "michael.lawson@reqres.in"},
             {'Name': "Lindsay Ferguson", 'mail': "lindsay.ferguson@reqres.in"},
             {'Name': "Tobias Funke", 'mail': "tobias.funke@reqres.in"},
             {'Name': "Byron Fields", 'mail': "byron.fields@reqres.in"},
             {'Name': "George Edwards", 'mail': "george.edwards@reqres.in"},
             {'Name': "Rachel Howell", 'mail': "rachel.howell@reqres.in"})

    if request.method == 'POST':
        username = request.form['Name']
        session['login'] = True
        session['Name'] = username

    if request.method == 'GET':
        if 'inputSearch' in request.args:
            search = request.args['inputSearch']
            return render_template('assignment9.html',
                                   users=users,
                                   search=search)

    return render_template('assignment9.html',
                           request_method=request.method,
                           username=username)



@app.route('/logout')
def logout():
    session['login'] = False
    return redirect(url_for('assignment9'))


if __name__ == '_main_':
    app.run(debug=True)
