from flask import Flask, render_template, url_for,redirect

app = Flask(__name__)



from pages.assignment10.assignment10 import Users
app.register_blueprint(Users)


if __name__ == '__main__':
    app.run(debug=True)
