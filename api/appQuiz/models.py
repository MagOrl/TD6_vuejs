from .app import db
from sqlalchemy import Column, Integer, String, ForeignKey, ForeignKeyConstraint
from sqlite3 import IntegrityError

class Question(db.Model):

    __tablename__ = "QUESTION"

    num = Column("num",  Integer, primary_key=True)
    id_quiz = Column(Integer, ForeignKey("QUIZ.id_quiz"),primary_key= True)

    title = Column("title", String, nullable= False)

    questionnaire = db.relationship("Questionnaire", back_populates="questions")

    typeQuestion = Column(String)

    def __init__(self, num: int,title: str):
        self.num = num
        self.title = title

    def get_num(self):
        return self.num

    def get_title(self):
        return self.title
    
    def to_json(self):
        return {
            "num": self.num,
            "title": self.title
        }
    
    __mapper_args__ = {
        "polymorphic_identity": "question",
        "polymorphic_on": typeQuestion
    }

class Questionnaire(db.Model):

    __tablename__ = "QUIZ"

    id = Column("id_quiz", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String, unique= True)

    questions = db.relationship("Question", back_populates="questionnaire", cascade="all, delete-orphan")

    def __init__(self,quiz_name: str):

        self.name = quiz_name
        self.questions = []

    def to_json(self, full: bool = False):

        if full :
            return {
                "id": self.id,
                "name": self.name,
                "questions": [question.to_json() for question in self.questions]
            }
        
        else:
            return {
                "id": self.id,
                "name": self.name,
            }

    def get_question(self,num: int):
        for question in self.questions:
            question: Question
            if question.get_num() == num:
                return question
        return None

    def get_questions(self):
        return self.questions

    def add_question(self, title: str, type: str = "standard", propositions: list[str] = [], answer: str|int = None) -> Question|None:
        try:
            max_num = db.session.execute(
                db.select(db.func.max(Question.num)).where(Question.id_quiz == self.id)
                ).scalar()

            num = (max_num or 0) + 1

            question : Question = None
            match(type):
                case "fermee":
                    question = QuestionFermee(num= num, title= title, propositions= propositions, answer= answer)

                case "ouverte":
                    question = QuestionOuverte(num= num, title= title, answer= answer) 
                case _ :
                    question = Question(num, title) 

            question.id_quiz = self.id
            self.questions.append(question)
            db.session.add(question)
            db.session.commit()

            return question
        except IntegrityError as e:
            return None

    def remove_question(self, num: int) -> Question|None:

        question: Question = db.session.execute(db.select(Question).where(Question.id_quiz == self.id and Question.num == num))
        
        if not question:
            return None
        
        db.session.delete(question)
        db.session.commit()
        return question
    
class QuestionOuverte(Question):

    __tablename__ = "questionOuverte"

    num = Column(Integer, ForeignKey("QUESTION.num"), primary_key= True)
    id_quiz = Column(Integer,ForeignKey("QUESTION.id_quiz"), primary_key= True)
    answer = Column("answer", String, nullable= False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['num', 'id_quiz'],
            ['QUESTION.num', 'QUESTION.id_quiz']
        ),
    )

    __mapper_args__ = {
        "polymorphic_identity": "ouverte",
        "inherit_condition": db.and_(
            num == Question.num,
            id_quiz == Question.id_quiz
        )
    }

    def __init__(self, num, title, answer):
        super().__init__(num, title)
        self.answer = answer

    def to_json(self):
        json: dict = super().to_json()
        json["answer"] = self.answer

        return json

class QuestionFermee(Question):

    __tablename__ = "questionFermee"

    num = Column(Integer, ForeignKey("QUESTION.num"), primary_key= True)
    id_quiz = Column(Integer,ForeignKey("QUESTION.id_quiz"), primary_key= True)

    first_proposition = Column(String)
    second_proposition = Column(String)

    answer = Column("answer", Integer, nullable= False)

    def __init__(self, num, title, propositions: list, answer: int):
        super().__init__(num, title)
        self.answer = answer
        self.first_proposition = propositions[0]
        self.second_proposition = propositions[1]

    __table_args__ = (
        ForeignKeyConstraint(
            ['num', 'id_quiz'],
            ['QUESTION.num', 'QUESTION.id_quiz']
        ),
    )


    __mapper_args__ = {
        "polymorphic_identity": "fermee",
        "inherit_condition": db.and_(
            num == Question.num,
            id_quiz == Question.id_quiz
        )
    }

    def to_json(self):
        json: dict = super().to_json()
        json["propositions"] = [self.first_proposition, self.second_proposition]
        json["answer"] = self.answer

        return json

def get_all_questionnaires() -> list[Questionnaire]:
    return db.session.execute(db.select(Questionnaire)).scalars()

def get_questionnaire(id_question: int) -> Questionnaire|None:
    #return next((questionaire for questionaire in questionaires if questionaire.id == id_question), None)

    return db.session.get(Questionnaire, id_question)


def create_quiz(name: str) -> Questionnaire|None:
    try:
        quiz: Questionnaire = Questionnaire(name)
        db.session.add(quiz)
        db.session.commit()
        db.session.flush()

        return quiz
    # Name already exists
    except IntegrityError as e:
        return None

def delete_questionnaire(id_question: int) -> bool:
    
    questionaire = get_questionnaire(id_question)
    if questionaire:
        db.session.delete(questionaire)
        db.session.commit()
        return True
    return False
