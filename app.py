#!/usr/bin/python3
""" Flask Application """
from models import storage
# from api.v1.views import app_views

#################### flask imports ###########################################################
from os import environ
from flask import Flask, render_template, make_response, jsonify, redirect, request, session
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from flask_session import Session
####################### Models imports ##################################################
from models.base_model import BaseModel
from models.review import Review
from models.user import User
from models.question import Question
from models.answer import Answer
from models.quiz import Quiz
from models.quiz_questions import Quiz_Questions
from models.quiz_questions_choices import Quiz_Questions_Choices
##########################################################################################

classes = {"BaseModel": BaseModel,"Review": Review , "User": User, "Question": Question, "Answer": Answer,
           "Quiz": Quiz, "Quiz_Questions": Quiz_Questions, "Quiz_Questions_Choices": Quiz_Questions_Choices}


app = Flask(__name__ , static_url_path='')

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
# app.register_blueprint(app_views)
cors = CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})



@app.teardown_appcontext
def close_db(error):
    """ Close Storage """
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'Mathifestation API',
    'uiversion': 3
}

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Swagger(app)
Session(app)


@app.route('/', strict_slashes=False)
@app.route('/index', strict_slashes=False)
def index():
    """ Index
    ---
    responses:
      200:
        description: Index
    """
    # print(session.get("username"))
    return render_template('index.html', user=session.get("username"), error=None)



@app.route('/signUp', strict_slashes=False, methods=["POST", "GET"])
def signUp():
    if request.method == "POST":
        ####### record the user name  #####
        # print(request.form.get("name"))
        # print(request.form.get("username"))
        # print(request.form.get("email"))
        # print(request.form.get("firstname"))
        # print(request.form.get("lastname"))
        ####################################
        res = storage.get_attribute("User", "username", request.form.get("username"))
        print(res)
        if (len(res) > 0):
            return render_template('signUp.html', error="User already exists")
        
        newUser = User(username=request.form.get("username"), email=request.form.get("email"), password=request.form.get("password") , first_name=request.form.get("firstname"), last_name=request.form.get("lastname"))
        session["user_id"] = newUser.id
        session["username"] = request.form.get("username")
        storage.new(newUser)
        storage.save()
        # redirect to the main page
        return redirect("/")

    return render_template('signUp.html',  user=session.get("username"))


@app.route('/login', strict_slashes=False, methods=["POST", "GET"])
def login():
    if request.method == "POST":
        userRegistered = storage.get_attribute("User", ["email", "password"], [request.form.get("email"), request.form.get("password")])
        if (userRegistered == []):
            return render_template('login.html', error="User not found")
        session["user_id"] = userRegistered.id
        session["username"] = userRegistered.username
        # redirect to the main page
        return redirect("/")
    return render_template('login.html', error=None, user=session.get("username"))



@app.route('/checkUserNameExists', strict_slashes=False)
def check_username():
    print(request.values.get('username'))
    res = storage.get_attribute("User", ["username"], [request.values.get('username')])
    if (len(res) > 0):
        return jsonify({"exists": True})
    return jsonify({"exists": False})


@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("user_id", None)
    return redirect("/")


@app.route('/ask_question', strict_slashes=False, methods=["POST", "GET"])
def ask_question():
    """ Question
    ---
    responses:
      200:
        description: Question
    """
    if request.method == "POST":
        title = request.form.get("title")
        question = request.form.get("question")
        print(title)
        print(question)
        if (session.get("user_id") is None):
            return render_template('ask_question.html', error="You need to be logged in to ask a question")
        newQuestion = Question(title=title, body=question, user_id=session.get("user_id"))
        if (question == ""):
            return render_template('ask_question.html', error="Question cannot be empty", user=session.get("username"))
        storage.new(newQuestion)
        storage.save()
        # redirect to the main page
        print("kaa")
        return redirect("/")
    return render_template('ask_question.html',  user=session.get("username"), error=None)


@app.route('/question/<id>', strict_slashes=False)
def question(id):
    """ Question
    ---
    responses:
      200:
        description: Question
    """
    question = storage.get_attribute("Question", ["id"], [id])[0]
    if (question == []):
        return render_template('ask_question.html', error="Question not found", user=session.get("username"))
    
    print(question.id)
    answers = storage.get_attribute("Answer", ["question_id"], [id])
    users_names = []
    for answer in answers:
        users_names.append(storage.get_attribute("User", ["id"], [answer.user_id]))
    
    return render_template('question.html', question=question,
                           user=session.get("username"), answers=answers, users_names_answers=users_names)


@app.route('/search_question', strict_slashes=False, methods=["GET", "POST"])
def search_question():
    search_value = request.values.get("search_value")
    if request.method == "POST":
        availableQuestions = storage.search("Question", ["title"], [search_value], limit=5)
        questions = []
        for q in availableQuestions:
            questions.append(q.to_dict())
        return jsonify({'questions_list': questions})
    else:
        availableQuestions = storage.search("Question", ["title"], [search_value], limit=5)
        questions = []
        for q in availableQuestions:
            questions.append(q.to_dict())
        return render_template('search_question.html', questions=questions, user=session.get("username"))

@app.route('/answer_question/<question_id>', strict_slashes=False, methods=["GET", "POST"])
def answer_question(question_id):
    search_value = request.values.get("search_value")
    if request.method == "POST":
        availableQuestions = storage.search("Question", ["title"], [search_value], limit=5)
        questions = []
        for q in availableQuestions:
            questions.append(q.to_dict())
        return jsonify({'questions_list': questions})
    else:
        availableQuestions = storage.search("Question", ["title"], [search_value], limit=5)
        questions = []
        for q in availableQuestions:
            questions.append(q.to_dict())
        return render_template('search_question.html', questions=questions, user=session.get("username"))


@app.route('/test', strict_slashes=False, methods=["GET", "POST"])
def test():

    questions = {"1": "lol"}

    return render_template('test.html', user=session.get("username"), questions = questions)

@app.route('/test_create', strict_slashes=False, methods=["GET", "POST"])
def test_create():

    questions = {"1": "lol"}

    return render_template('test_create.html', user=session.get("username"), questions = questions)



if __name__ == "__main__":
    """ Main Function """
    host = environ.get('MATHS_API_HOST')
    port = environ.get('MATHS_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, threaded=True)
