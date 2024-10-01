from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

enrollment = db.Table('enrollment',
db.Column('student_id', db.Integer, db.ForeignKey('student.id'), primary_key=True),
db.Column('course_id', db.Integer, db.ForeignKey('course.id'), primary_key=True)
)

class Student(db.Model):
  __tablename__ = "student"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  course = db.relationship('Course',secondary=enrollment, backref='student')

  def serialize(self):
    return {
      "id": self.id,
      "name": self.name,
      "course": [course.serialize() for course in self.course],
    }

class Course(db.Model):
  __tablename__ = "course"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)

  def serialize(self):
    return {
      "id": self.id,
      "name": self.name
    }