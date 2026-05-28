from flask import Flask, request

app = Flask(__name__)

workouts = [
    {
        "name": "Pushups",
        "sets": 3
    },
    {
        "name": "Squats",
        "sets": 4
    },

    {
        "name": "PullUps",
        "sets": 5
    }
]

@app.route("/")
def home():
    return {"message": "FlowFit backend running"}

@app.route("/workouts")
def get_workouts():
    return {"workouts": workouts}

@app.route("/add-workout", methods=["POST"])
def add_workout():
    data = request.json

    print(data)

    workouts.append(data)

    return {
        "message": "Workout added",
        "workouts": workouts
    }

@app.route("/users")
def users():
    return {
        "users": [
        "Walter",
        "Alex",
        "Lucilla"

        ]
    }

app.run(debug=True)