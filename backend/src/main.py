from .entities.entity import Session, engine, Base
from .entities.exam import Exam

#Generate database Schema
Base.metadata.create_all(engine)

#Start Session
session = Session()

#Check for existing data
exams = session.query(Exam).all()

if len(exams) == 0:
    #Create an initial dummy exam

    python_exam = Exam('SQLAlchemy Exam', 'Test your knowledge', "script")
    session.add(python_exam)
    session.commit()
    session.close()

    #Reload exams
    exams = session.query(Exam).all()

print("### Exams")
for exam in exams:
    print(f'({exam.id}) {exam.title} - {exam.description}')
