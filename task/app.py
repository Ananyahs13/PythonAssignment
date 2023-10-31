from flask import Flask, request, jsonify

app = Flask(__name__)

# Dummy data for courses and students
courses = [
    {"id": 1, "name": "Math 101"},
    {"id": 2, "name": "History 101"},
]

students = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
]

# Route to get the list of available courses
@app.route('/api/courses', methods=['GET'])
def get_courses():
    return jsonify(courses)

# Route to get the list of students
@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify(students)

# Route to enroll a student in a course
@app.route('/api/enroll', methods=['POST'])
def enroll_student():
    data = request.get_json()
    student_id = data.get('student_id')
    course_id = data.get('course_id')

    # Check if student and course exist
    student = next((student for student in students if student["id"] == student_id), None)
    course = next((course for course in courses if course["id"] == course_id), None)

    if student is None or course is None:
        return jsonify({"message": "Student or course not found"}), 404

    # Implement the enrollment logic here (e.g., add the course to the student's enrolled courses)
    # This is where you would interact with your database or data store

    return jsonify({"message": f"Enrolled {student['name']} in {course['name']}"}), 200

if __name__ == '__main__':
    app.run(debug=True)
