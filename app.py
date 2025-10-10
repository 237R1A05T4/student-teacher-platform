from flask import Flask, request, jsonify, render_template
import os

app = Flask(__name__)

# In-memory storage (simple, no DB)
announcements = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/announcements', methods=['GET'])
def get_announcements():
    return jsonify(announcements)

@app.route('/announcements', methods=['POST'])
def post_announcement():
    data = request.json
    if 'text' in data and data['text']:
        announcements.append(data)
        return jsonify({"message": "Announcement posted"}), 201
    return jsonify({"error": "Invalid data"}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

