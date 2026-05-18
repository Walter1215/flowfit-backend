from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "FlowFit backend running"}

@app.route("/workouts")
def workouts():
    return {
        "workouts": [
            "Push Ups",
            "Squats",
            "Running"
        ]
    }

app.run(debug=True)