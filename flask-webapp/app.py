from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='public')

@app.route('/')
def home():
    return send_from_directory('public', 'index.html')

@app.route('/about')
def about():
    return send_from_directory('public', 'about.html')

@app.route('/contact')
def contact():
    return send_from_directory('public', 'contact.html')

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
