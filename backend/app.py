from flask import Flask
from flask_cors import CORS
from routes import booking_routes  # Make sure routes/booking_routes.py exists

app = Flask(__name__)
# In app.py
CORS(app, resources={r"/api*": {"origins": "*"}})


app.register_blueprint(booking_routes)

# ✅ For Vercel: expose a WSGI-compatible `handler`
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

# ✅ For local development
if __name__ == "__main__":
    app.run(debug=True, port=5000)
