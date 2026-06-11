# FlowFit Backend

Backend API for the FlowFit fitness application built using Flask.

## Overview

FlowFit Backend is a beginner-friendly REST API project designed to practice backend development concepts including routing, JSON handling, and CRUD operations. Workout data is currently stored in memory using Python lists and dictionaries.

## Features

* View all workouts
* View a workout by name
* View a workout by index
* Add new workouts using POST requests
* Update existing workouts using PUT requests
* Delete workouts using DELETE requests
* JSON request and response handling
* REST API routing with Flask

## Technologies

* Python
* Flask

## API Endpoints

### GET Routes

```text
GET /
GET /workouts
GET /workouts/<name>
GET /workouts/index/<index>
```

### POST Routes

```text
POST /add-workout
```

### PUT Routes

```text
PUT /update-workout/<name>
```

### DELETE Routes

```text
DELETE /delete-workout/<name>
```

## Example Workout Object

```json
{
  "name": "Pushups",
  "sets": 3
}
```

## Concepts Practiced

* REST APIs
* CRUD Operations
* Route Parameters
* JSON Data Handling
* Lists and Dictionaries
* Backend Development Fundamentals

## Future Improvements

* Add workout IDs
* Input validation and error handling
* PostgreSQL database integration
* Persistent data storage
* User authentication
* Project structure with separate routes and models

## Run Locally

```bash
pip install -r requirements.txt
python3 server.py
```

Server runs at:

```text
http://127.0.0.1:5000
```
