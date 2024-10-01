from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Student, Course, enrollment
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///basedatos.db'
db.init_app(app)
migrate = Migrate(app,db)
CORS(app)


@app.route('/')
def index():
  return "Hola mundo"


@app.route('/students', methods=['POST'])
def create_student():
  data = request.get_json()
  student = Student()
  course = Course.query.filter_by(name=data['course']).first()

  if not course:
    course = Course(name=data['course'])
    student.name = data['name']
    student.course.append(course)

    db.session.add(course)
    db.session.add(student)
    db.session.commit()
    return jsonify({'message': 'Student created successfully'}), 201
  return jsonify({"message": "Course not found"}), 404


if __name__ == "__main__":
  app.run(host="localhost",port=5004, debug=True)