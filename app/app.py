from flask import Flask, request, jsonify
from minio_config import minio_client, bucket_name
from keycloak_config import keycloak_openid
import uuid

app = Flask(__name__)

@app.route("/upload", methods=["POST"])
def upload_file():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Unauthorized"}), 401

    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    file_id = str(uuid.uuid4())
    minio_client.put_object(
        bucket_name, file_id, file.stream, length=-1, part_size=10*1024*1024
    )
    return jsonify({"file_id": file_id}), 201


@app.route("/download/<file_id>", methods=["GET"])
def download_file(file_id):
    try:
        response = minio_client.get_object(bucket_name, file_id)
        return response.data, 200
    except Exception:
        return jsonify({"error": "File not found"}), 404


@app.route("/update/<file_id>", methods=["PUT"])
def update_file(file_id):
    file = request.files.get("file")
    if not file:
        return jsonify({"error": "No file provided"}), 400

    try:
        minio_client.remove_object(bucket_name, file_id)
        minio_client.put_object(
            bucket_name, file_id, file.stream, length=-1, part_size=10*1024*1024
        )
        return jsonify({"message": "File updated"}), 200
    except Exception:
        return jsonify({"error": "File not found"}), 404


@app.route("/delete/<file_id>", methods=["DELETE"])
def delete_file(file_id):
    try:
        minio_client.remove_object(bucket_name, file_id)
        return jsonify({"message": "File deleted"}), 200
    except Exception:
        return jsonify({"error": "File not found"}), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
