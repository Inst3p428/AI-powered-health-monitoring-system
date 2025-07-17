from flask import Flask, render_template, jsonify
import pandas as pd
import random

app = Flask(__name__)

# Simulated or real-time data loading
def get_latest_data():
    # Replace with actual sensor input or database query
    hr = random.randint(55, 100)
    spo2 = random.randint(88, 99)
    met = round(random.uniform(1.0, 10.0), 1)

    # Anomaly detection
    alerts = []
    if hr < 65 or hr > 95:
        alerts.append("Abnormal Heart Rate")
    if spo2 < 90:
        alerts.append("Low Blood Oxygen")
    if met > 8:
        alerts.append("High Physical Activity")

    return {
        "hr": hr,
        "spo2": spo2,
        "met": met,
        "alerts": alerts
    }

@app.route("/")
def dashboard():
    return render_template("dashboard.html")

@app.route("/api/data")
def api_data():
    return jsonify(get_latest_data())

if __name__ == "__main__":
    app.run(debug=True)
