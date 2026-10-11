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

# Existing students collection
collection = database["students"]

# Task 3 - To-Do collection
todo_collection = database["todo_items"]


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


# Display student form
@app.route('/form')
def form():
    return render_template('form.html')


# Handle student form submission
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

        # Insert student into MongoDB Atlas
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


# -------------------------------------------------
# Task 3 - Backend API for To-Do items
# -------------------------------------------------

@app.route('/submittodoitem', methods=['POST'])
def submit_todo_item():
    try:
        # Get values submitted by the To-Do form
        item_name = request.form.get('itemName', '').strip()
        item_description = request.form.get('itemDescription', '').strip()

        # Validate form fields
        if not item_name or not item_description:
            return "Item Name and Item Description are required.", 400

        # Create MongoDB document
        todo_data = {
            "itemName": item_name,
            "itemDescription": item_description
        }

        # Insert To-Do item into MongoDB
        todo_collection.insert_one(todo_data)

        return "To-Do item submitted successfully!", 200

    except Exception as error:
        return f"Error: {str(error)}", 500


if __name__ == '__main__':
    app.run(debug=True)