from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({
        "message": "Flask backend is running!"
    })


@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.get_json()

        name = data.get('name', '').strip()
        course = data.get('course', '').strip()

        if not name or not course:
            return jsonify({
                "error": "Name and Course are required"
            }), 400

        submitted_data = {
            "name": name,
            "course": course
        }

        print("Received data:", submitted_data)

        return jsonify({
            "message": "Data submitted successfully!",
            "data": submitted_data
        }), 200

    except Exception as error:
        return jsonify({
            "error": str(error)
        }), 500


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )