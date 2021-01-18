from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)


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


@app.route('/assignment11/users')
def users():
    if request.method == 'GET':
        query = "SELECT * FROM users"
        query_result = interact_db(query=query, query_type = 'fetch')
        if len(query_result) == 0:
            return jsonify({
                'success': 'FALSE',
                'data': []
            })
        else:
            return jsonify({
                'success': 'TRUE',
                'data': query_result
            })


@app.route('/assignment11/users/selected', defaults={'user_id':1})
@app.route('/assignment11/users/selected/<int:user_id>')
def selected(user_id):
    if request.method == 'GET':
        query = "SELECT * FROM users WHERE id = '%s';" % user_id
        query_result = interact_db(query=query, query_type='fetch')
        if len(query_result) == 0:
            return jsonify({
                'ERROR - user do not exist'
                'data':[]
            })
        else:
            return jsonify({
                'success': 'TRUE',
                'data': query_result[0]
            })


if __name__ == '__main__':
    app.run()
