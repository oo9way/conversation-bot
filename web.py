from flask import Flask


app = Flask(__name__)
@app.route("/home", methods=['GET'])
def home_page():
    html = """
    <a href='/home'>Home page</a>
    <a href='/contact'>Contact page</a>
    <a href='/hello'>Hello page</a>
    <h1>This is home page</h1>
    """
    return html


@app.route("/contact", methods=['GET'])
def contact_page():
    return "<h1>Do not contact me</h1>"



@app.route("/hello", methods=['GET'])
def hello_page():
    return "<h1>Hello wolrd</h1>"