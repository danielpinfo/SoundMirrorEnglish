from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify({
        "status": "ok",
        "service": "soundmirror-phoneme-backend",
        "language": os.environ.get("LANGUAGE", "en"),
        "model_id": os.environ.get("MODEL_ID", "not-set")
    })

@app.get("/health")
def health():
    return "ok", 200

if __name__ == "__main__":
    # For local testing only; Railway will use the Gunicorn command in the Dockerfile
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
