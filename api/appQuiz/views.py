from .app import app
from .models import Questionnaire, Question, get_all_questionnaires, get_questionnaire, create_quiz, delete_questionnaire
from flask import abort, request, url_for, jsonify

@app.route('/questionnaires', methods=['GET'])
def list_questionnaires():
    questionnaires: list[Questionnaire] = get_all_questionnaires()

    if not questionnaires:
        abort(404, description="No questionnaires found")

    return jsonify({"questionnaires": [make_public_questionnaire(questionnaire) for questionnaire in questionnaires]}), 200

@app.route('/questionnaires/<int:id_questionnaire>', methods=['GET'])
def get_questionnaire_by_id(id_questionnaire: int):
    questionnaire = get_questionnaire(id_questionnaire)

    if not questionnaire:
        abort(404, description=f"Questionnaire with ID {id_questionnaire} not found")

    return questionnaire.to_json(full=True), 200

@app.route('/questionnaires', methods=['POST'])
def create_questionnaire():
    if not request.is_json:
        abort(400, description="Request must be JSON")

    if "name" not in request.json or not isinstance(request.json.get("name"), str):
        abort(400, description="Missing name in request data")

    questionaire: Questionnaire = create_quiz(request.json.get("name"))

    if not questionaire:
        abort(400,description= "Couldn't create the quiz, name may already exists")

    return make_public_questionnaire(questionaire), 201

@app.route('/questionnaires/<int:id_question>', methods=['DELETE'])
def remove_questionnaire(id_question: int):

    questionnaire = get_questionnaire_by_id(id_question)

    if not questionnaire:
        abort(404, description=f"Questionnaire with ID {id_question} not found")

    if not delete_questionnaire(id_question):
        abort(400, description="Id not found or can't be deleted")

    return make_public_questionnaire(questionnaire), 200

@app.route('/questionnaires/<int:id_questionnaire>/questions', methods=['GET'])
def get_questions(id_questionnaire: int):

    questionnaire: Questionnaire = get_questionnaire(id_questionnaire)

    if questionnaire is None:
        abort(404, f"No quiz with id {id_questionnaire} found")

    return jsonify({"questions": [make_public_question(questionnaire.id, question) for question in questionnaire.get_questions()]}), 200

@app.route('/questionnaires/<int:id_questionnaire>/questions/<int:num_question>', methods=['GET'])
def get_question_by_num(id_questionnaire: int, num_question: int):
    questionnaire = get_questionnaire(id_questionnaire)

    if not questionnaire:
        abort(404, description=f"Questionnaire with ID {id_questionnaire} not found")

    question: Question = questionnaire.get_question(num_question)

    if question is None:
        abort(404, description=f"Question with Num {num_question} not found pour le questionnaire {id_questionnaire}")

    return make_public_question(id_questionnaire, question),200

@app.route('/questionnaires/<int:id_questionnaire>/questions', methods=['POST'])
def create_question(id_questionnaire: int):
    if not request.is_json:
        abort(400, description="Request must be JSON")

    if "title" not in request.json or not isinstance(request.json.get("title"), str):
        abort(400, description="Missing question's title in request data")

    if "type" not in request.json or not isinstance(request.json.get("type"), str):
        abort(400, description="Missing question's type in request data : fermee, ouverte or standard")

    title: str = request.json.get("title")
    type: str = request.json.get("type")

    if type == "fermee":
        if "proposition1" not in request.json or not isinstance(request.json.get("proposition1"), str):
            abort(400, description="Missing question's first proposition in request data")

        if "proposition2" not in request.json or not isinstance(request.json.get("proposition2"), str):
            abort(400, description="Missing question's second proposition in request data")

    if type != "standard" and"answer" not in request.json or not isinstance(request.json.get("answer"), str | int):
        abort(400, description="Missing question's type in request data : multiple, true/false or standard")    

    answer = request.json.get("answer") or None
    prop1 = request.json.get("proposition1") or None
    prop2 = request.json.get("proposition2") or None

    questionaire: Questionnaire = get_questionnaire(id_questionnaire)

    if questionaire is None:
       abort(404, description=f"Questionnaire with ID {id_questionnaire} not found")

    questionaire.add_question(title= title,type= type, propositions= [prop1, prop2],answer= answer,)

    return make_public_question(id_questionnaire, questionaire.get_questions()[-1]), 201

@app.route('/questionnaires/<int:id_questionnaire>/questions/<int:num_question>', methods=['DELETE'])
def delete_question(id_questionnaire: int, num_question: int):

    questionnaire: Questionnaire = get_questionnaire(id_questionnaire)

    if not questionnaire:
        abort(404, description=f"Questionnaire with ID {id_questionnaire} not found")

    question: Question = questionnaire.get_question(num_question)

    if not questionnaire.remove_question(num_question):
        abort(400, description="Num not found or can't be deleted")

    return make_public_question(questionnaire.id ,question), 200

def make_public_questionnaire(questionnaire: Questionnaire):
    questionnaire_json = questionnaire.to_json()
    questionnaire_json['uri'] = url_for('get_questionnaire_by_id', id_questionnaire=questionnaire.id, _external=True)
    return questionnaire_json

def make_public_question(id_quiz: int, question: Question):
    question_json = question.to_json()
    question_json['uri'] = url_for('get_question_by_num', id_questionnaire= id_quiz,num_question = question.get_num(), _external=True)
    return question_json

@app.errorhandler(404)
def handle_404(e):
    return jsonify(error=str(e)), 404

@app.errorhandler(400)
def handle_400(e):
    return jsonify(error=str(e)), 400
