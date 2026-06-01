from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImQ3ZWY1OTVlLWI0MmYtNDBiZS1iODgyLTYzZDRlYmI3NDRhMCIsImlhdCI6MTc4MDI5NTUwOSwic3ViIjoiZGV2ZWxvcGVyLzFiNzgwMzdkLWEzYjctMTIzZi02MGZhLTkyNjU3ZWZlYzEzZiIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjUyLjg3LjIyOC40Il0sInR5cGUiOiJjbGllbnQifV19.cD9HWbbHhubUN8LsjEgnniJk5kW0cFmqxgDdSJwehWeQO_0Z_jMA7-ymuDe3T5ePSLymF3N-XhqviT0qmQbkNQ"

@app.route('/proxy/<path:path>')
def proxy(path):
    url = f"https://api.clashofclans.com/v1/{path}"
    resp = requests.get(url, headers={'Authorization': f'Bearer {API_TOKEN}'}, params=request.args)
    return jsonify(resp.json()), resp.status_code

@app.route('/')
def home():
    return jsonify({"status": "ok", "message": "COC API Proxy Running"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)