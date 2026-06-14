from flask import Flask, request

# Create Flask application
app = Flask(__name__)

# Sample data stored in memory
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

# Home route
@app.route("/")
def home():
    return {"message": "FlowFit backend running"}

# Get all workouts
@app.route("/workouts", methods=["GET"])
def get_workouts():
    return {"workouts": workouts}

# Add workout
@app.route("/workouts", methods=["POST"])
def add_workout():

    data = request.json

    # Validate request data
    if not data:
        return {"message": "No workout data provided"}, 400

    if "name" not in data or "sets" not in data:
        return {"message": "Workout must include name and sets"}, 400

    workouts.append(data)

    return {
        "message": "Workout added",
        "workouts": workouts
    }, 201

# Get workout by index
@app.route("/workouts/index/<int:index>", methods=["GET"])
def get_workout_by_index(index):

    if index < 0 or index >= len(workouts):
        return {"message": "Invalid workout index"}, 404

    return workouts[index]

# Get workout by name
@app.route("/workouts/<name>", methods=["GET"])
def get_workout_by_name(name):

    for workout in workouts:

        if workout["name"].lower() == name.lower():
            return workout

    return {"message": "Workout not found"}, 404

# Update workout
@app.route("/workouts/<name>", methods=["PUT"])
def update_workout(name):

    data = request.json

    if not data:
        return {"message": "No update data provided"}, 400

    for workout in workouts:

        if workout["name"].lower() == name.lower():

            if "name" in data:
                workout["name"] = data["name"]

            if "sets" in data:
                workout["sets"] = data["sets"]

            return {
                "message": "Workout updated",
                "workout": workout
            }

    return {"message": "Workout not found"}, 404

# Delete workout
@app.route("/workouts/<name>", methods=["DELETE"])
def delete_workout(name):

    for workout in workouts:

        if workout["name"].lower() == name.lower():

            workouts.remove(workout)

            return {
                "message": "Workout deleted",
                "workouts": workouts
            }

    return {"message": "Workout not found"}, 404

# Get users
@app.route("/users", methods=["GET"])
def users():
    return {
        "users": [
            "Walter",
            "Alex",
            "Lucilla"
        ]
    }

# Run Flask server
if __name__ == "__main__":
    app.run(debug=True)