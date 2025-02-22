from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/proxy/<path:path>')
def proxy(path):
    # Construct the full URL to fetch data from
    url = f"https://a.windbornesystems.com/{path}"
    
    # Fetch data from the external URL
    response = requests.get(url)
    
    # Return the JSON response to the client
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(debug=True)
