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

@app.route("/workouts/index/<int:index>")
def get_workout_by_index(index):
    return workouts[index]

@app.route("/workouts/<name>")
def get_workout_by_name(name):
    for workout in workouts:
        if workout["name"].lower() == name.lower():
            return workout

    return {"message": "Workout not found"}

@app.route("/delete-workout/<name>", methods=["DELETE"])
def delete_workout(name):
    for workout in workouts:
        if workout["name"].lower() == name.lower():
            workouts.remove(workout)

            return {
                "message": "Workout deleted",
                "workouts": workouts
            }

    return {"message": "Workout not found"}


if __name__ == "__main__":
    app.run(debug=True)