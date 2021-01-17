from flask import Flask, render_template, url_for, redirect, blueprints, session, request, Blueprint
import mysql.connector

Users = Blueprint('users', __name__,
                  static_folder='static',
                  static_url_path='/users',
                  template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='HW10',
                                         auth_plugin='mysql_native_password')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result

    connection.close()
    cursor.close()
    return return_value


#insert users
@Users.route('/insertuser', methods=['GET','POST'])
def insertuser():
    if request.method == 'POST':
        id = request.form['id']
        first_name = request.form['f_name']
        last_name = request.form['l_name']
        email = request.form['email']
        query = "INSERT into users (id, first_name, last_name, email) VALUES ('%s', '%s', '%s', '%s')" % (id, first_name, last_name, email)
        interact_db(query, 'commit')

    return redirect('/assignment10')


#delete users
@Users.route('/deleteuser', methods=['GET','POST'])
def deleteuser():
    if request.method == 'POST':
        user_id = request.form['id']
        query = "DELETE FROM users WHERE id='%s';" % user_id
        interact_db(query, 'commit')

    return redirect('/assignment10')


#update users
@Users.route('/updateuser')
def update_user():
    id = request.args['id']
    email = request.args['email']
    query = "UPDATE users SET email = '%s' WHERE id = '%s' " % (email, id)
    interact_db(query, 'commit')

    return redirect('/assignment10')


@Users.route('/')
@Users.route('/assignment10')
def users():
    query = "select * from users;"
    query_result = interact_db(query, 'fetch')
    return render_template('assignment10.html', users=query_result)

