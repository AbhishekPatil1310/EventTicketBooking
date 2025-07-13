from flask import Flask
from flask_cors import CORS
from routes import booking_routes

app = Flask(__name__)

# Allow all origins (you can restrict later)
CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(booking_routes)

# For Vercel
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

# Local dev
if __name__ == "__main__":
    app.run(debug=True)
