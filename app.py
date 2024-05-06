# app.py
from flask import Flask, jsonify, request
from flask_cors import CORS
import get_data

app = Flask(__name__)
CORS(app)

REPORT_NAMES = ["report1", "report2", "report3"]
LEADERBOARD_NAMES = ["lb1", "lb2", "lb3"]


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Flask API!"}), 200


def show_table(table_name):
    return jsonify(get_data.generate_random_dataframe(10, 50)), 200


@app.route("/reports/<name>", methods=["GET"])
def report(name):
    if name not in REPORT_NAMES:
        return jsonify({"message": "Report not found"}), 404
    # You can replace this with your own code to generate a report
    return show_table(name)


@app.route("/leaderboards/<name>", methods=["GET"])
def leaderboard(name):
    if name not in LEADERBOARD_NAMES:
        return jsonify({"message": "leaderboard not found"}), 404
    # You can replace this with your own code to generate a report
    return show_table(name)


@app.route("/reports", methods=["GET"])
def reports():
    return jsonify(REPORT_NAMES), 200


@app.route("/leaderboards", methods=["GET"])
def leaderboards():
    return jsonify(LEADERBOARD_NAMES), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0")
