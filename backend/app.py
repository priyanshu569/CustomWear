from flask import Flask, request, jsonify
from flask_cors import CORS
from backend.routes.customization import customization_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(customization_bp, url_prefix="/api/custom")

@app.route("/")
def home():
    return "Welcome to CustomWear Backend"

if __name__ == '__main__':
    app.run(debug=True)
