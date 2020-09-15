from flask import Flask, jsonify, request
from .entities.entity import Session, engine, Base
from .entities.exam import Exam, ExamSchema



#Create the Flask application
app = Flask(__name__)


#Generate database Schema
Base.metadata.create_all(engine)

@app.route('/exams')
def get_exams():
    #Fetch the database
    session = Session()
    exam_objects = session.query(Exam).all()


    #Transform into JSON-serialisable objects
    schema = ExamSchema(many = True)
    exams = schema.dump(exam_objects)

    #Serialise as JSON
    session.close()
    return exams

@app.route('/exams', methods = ['POST'])
def add_exam():
    #Mount exam object
    posted_exam = ExamSchema(only = ('title', 'description')).load(request.get_json())

    exam = Exam(**posted_exam.data, created_by = "HTTP post request")

    #Persist the exam
    session = Session()
    session.add(exam)
    session.commit()

    #return created exam
    new_exam = ExamSchema().dump(exam).data
    session.close()

    return jsonify(new_exam), 201


