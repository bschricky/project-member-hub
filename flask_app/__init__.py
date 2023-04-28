from flask import Flask
app = Flask(__name__, static_url_path='/flask_app/static')
app.secret_key = "shhhhhh"