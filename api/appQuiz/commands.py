from .app import app, db
from .models import create_quiz, Question

@app.cli.command()
def syncdb():
    
    db.create_all()

    qz1 = create_quiz("Maths")
    db.session.add(qz1)
    db.session.commit()

    question: Question = qz1.add_question("Who's one of the greates mathematicians of all times ?", type="fermee", propositions=["Euler","Fermat"], answer=0)
    print(question.to_json())

    qz1.add_question("What's 2+2 ?", type="ouverte", answer="4")
    qz1.add_question(title= "What is the value of PI ?",type= "ouverte", answer= "3.1415")
