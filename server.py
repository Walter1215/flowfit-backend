from flask import Flask, request

# Create Flask Application
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

# Home Route 
@app.route("/")
def home():
    return {"message": "FlowFit backend running"}

# Get all workouts 
@app.route("/workouts")
def get_workouts():
    return {"workouts": workouts}

# Add new workout 
@app.route("/add-workout", methods=["POST"])
def add_workout():

    # Get JSON data from request
    data = request.json
    print(data)

    # Add workout to list 
    workouts.append(data)

    return {
        "message": "Workout added",
        "workouts": workouts
    }

# Get list of users
@app.route("/users")
def users():
    return {
        "users": [
            "Walter",
            "Alex",
            "Lucilla"
        ]
    }

# Get workout by index position
@app.route("/workouts/index/<int:index>")
def get_workout_by_index(index):
    return workouts[index]

# Get worout by name
@app.route("/workouts/<name>")
def get_workout_by_name(name):

    # Search through workouts
    for workout in workouts:

        # Compare names ignoring capitalization
        if workout["name"].lower() == name.lower():
            return workout

    return {"message": "Workout not found"}

# Delete worout by name
@app.route("/delete-workout/<name>", methods=["DELETE"])
def delete_workout(name):

    # Search for workout
    for workout in workouts:
        if workout["name"].lower() == name.lower():
            
            # Remove workout from list
            workouts.remove(workout)

            return {
                "message": "Workout deleted",
                "workouts": workouts
            }

    return {"message": "Workout not found"}

# Update workout by name 
@app.route("/update-workout/<name>", methods=["PUT"])
def update_workout(name):

    # Get updated data from request 
    data = request.json

    # Search for workout 
    for workout in workouts:

        if workout["name"].lower() == name.lower():

            # Update workout name if provided 
            if "name" in data:
                workout["name"] = data["name"]

            # Update workout sets if provided
            if "sets" in data:
                workout["sets"] = data["sets"]

            return {
                "message": "Workout updated",
                "workout": workout
            }

    return {"message": "Workout not found"}

# Run Flask Server 
if __name__ == "__main__":
    app.run(debug=True)