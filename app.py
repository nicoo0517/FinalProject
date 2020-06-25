# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
import model
from flask import session


# -- Initialization section --
app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    # result= model.test()
    # print(result)s
    return render_template("index.html")


@app.route('/startgame', methods = ['GET', 'POST'])
def startgame():
    session["consonants"]= (model.letters())
    print(session["consonants"])
    session["vowels"]= (model.letters2())
    print(session["vowels"])
    return render_template('game.html', consonants= session["consonants"], vowels=session["vowels"])


@app.route('/submitword', methods = ['GET', 'POST'])
def submitword():
    f = open("validwords.txt")
    validWords = f.readlines()
    validWords = [x.strip() for x in validWords]
    f.close()
    inputword = request.form["submitword"]
    print(inputword)
    inputwordlist = inputword.split(", ")
    print(inputwordlist)
    session["counter"] = 0
    letters = []
    for letter in session["consonants"]:
        letters.append(letter)
    for letter in session["vowels"]:
        letters.append(letter)
    print(letters)
    for word in inputwordlist:
        print(word)
        isvalid = True
        for letter in word:
            print(letter)
            if letter not in letters:
                isvalid = False
        print(isvalid)
        if isvalid == True:
            print(word)
            if word in validWords:
                session["counter"] += 1  
    # for word in inputwordlist:
    #     for letter in word:
    #         if letter in session["consonants"] or letter in session["vowels"]:
    #             if word in validWords:
    #                 counter += 1
    print(session["consonants"])
    print(session["vowels"])


    print(session["counter"])
    return render_template('results.html', inputword = inputword, consonants= session["consonants"], vowels=session["vowels"])

@app.route('/results', methods = ['GET', 'POST'])
def results():
    return render_template('results.html', points = " points earned! ")