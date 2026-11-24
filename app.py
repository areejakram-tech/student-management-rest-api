from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory database
students = [
    {"id": 1, "name": "Ali Khan", "department": "Computer Science", "cgpa": 3.5},
    {"id": 2, "name": "Sara Ahmed", "department": "Software Engineering", "cgpa": 3.8}
]

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify({"status": "success", "count": len(students), "data": students}), 200

@app.route('/students', methods=['POST'])
def add_student():
    data = request.get_json()
    if not data or 'name' not in data or 'department' not in data:
        return jsonify({"status": "error", "message": "Name and department are required"}), 400
    
    new_student = {
        "id": len(students) + 1,
        "name": data['name'],
        "department": data['department'],
        "cgpa": data.get('cgpa', 0.0)
    }
    students.append(new_student)
    return jsonify({"status": "success", "data": new_student}), 201

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    global students
    students = [s for s in students if s['id'] != student_id]
    return jsonify({"status": "success", "message": f"Student {student_id} deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
