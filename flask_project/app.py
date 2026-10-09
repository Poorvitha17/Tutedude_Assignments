from flask import Flask, jsonify, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
from urllib.parse import quote_plus
import os
import json
import certifi

app = Flask(__name__)

# Load values from .env
load_dotenv(override=True)

# MongoDB credentials
mongo_username = os.getenv("MONGO_USERNAME")
mongo_password = os.getenv("MONGO_PASSWORD")
mongo_host = os.getenv("MONGO_HOST")

# Encode credentials safely
encoded_username = quote_plus(mongo_username)
encoded_password = quote_plus(mongo_password)

# MongoDB Atlas connection string
mongo_uri = (
    f"mongodb+srv://{encoded_username}:{encoded_password}"
    f"@{mongo_host}/?retryWrites=true&w=majority&appName=Cluster0"
)

# Connect to MongoDB
client = MongoClient(
    mongo_uri,
    tls=True,
    tlsCAFile=certifi.where(),
    serverSelectionTimeoutMS=5000
)

database = client["student_database"]
collection = database["students"]


# Home route
@app.route('/')
def home():
    return "Flask application is running!"


# Task 1 - JSON API
@app.route('/api')
def api():
    try:
        with open('data.json', 'r') as file:
            data = json.load(file)

        return jsonify(data), 200

    except FileNotFoundError:
        return jsonify({
            "error": "Data file not found"
        }), 404

    except json.JSONDecodeError:
        return jsonify({
            "error": "Invalid JSON data"
        }), 500


# Display form
@app.route('/form')
def form():
    return render_template('form.html')


# Handle form submission
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get('name', '').strip()
        course = request.form.get('course', '').strip()

        if not name or not course:
            return render_template(
                'form.html',
                error='Name and course are required.'
            )

        student_data = {
            'name': name,
            'course': course
        }

        # Insert into MongoDB Atlas
        collection.insert_one(student_data)

        # Redirect to success page
        return redirect(url_for('success'))

    except Exception as error:
        return render_template(
            'form.html',
            error=str(error)
        )


# Success page
@app.route('/success')
def success():
    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)