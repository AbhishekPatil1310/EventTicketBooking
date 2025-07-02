from flask import Flask
from flask_cors import CORS
from routes import booking_routes
import os

app = Flask(__name__)

# ✅ Allow both local and deployed frontend URLs
CORS(app, origins=[
    "http://localhost:5173",  # Local Vite dev
    "https://event-ticket-booking-v98x-702tg90bp-abhisheks-projects-680a2fd9.vercel.app"  # Your deployed frontend
])

# Register routes
app.register_blueprint(booking_routes)

# ✅ Vercel entrypoint
def handler(environ, start_response):
    return app.wsgi_app(environ, start_response)

# ✅ Local dev
if __name__ == "__main__":
    app.run(debug=True, port=5000)
