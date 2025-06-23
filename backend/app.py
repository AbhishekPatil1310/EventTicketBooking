from flask import Flask
from flask_cors import CORS
from routes import booking_routes

app = Flask(__name__)
CORS(app)
app.register_blueprint(booking_routes)

# For Vercel
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

# For local dev
if __name__ == "__main__":
    app.run(debug=True, port=5000)
