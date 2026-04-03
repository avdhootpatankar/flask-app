import flask

# Initialize the Flask application
app = flask.Flask(__name__)

# Define a route for the default URL ("/")
@app.route("/")
def hello_world():
    return "<h1>Hello, Flask!</h1><p>Your app is running.</p>"

from users.views import mod as users_blueprint

app.register_blueprint(users_blueprint)

if __name__ == "__main__":
    app.run(debug=True)