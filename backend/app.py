from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/api")
def api():
    return jsonify({
        "message": "Hello from API",
        "status": "ok"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
