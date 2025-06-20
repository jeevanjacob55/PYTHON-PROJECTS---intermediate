from flask import Flask
from random import randint

app = Flask(__name__)

def make_bold(func):
    def bold():
        return "<b>"+func()+"</b>"
    return bold

def make_emphasis(func):
    def emphasize():
        return "<em>"+func()+"</em>"
    return emphasize

def make_underline(func):
    def underline():
        return "<u>"+func()+"</u>"
    return underline

@app.route("/")
def init():
    global secret_number
    secret_number = randint(1,100)
    return "<h2>Guess a number between 1 to 100!</h2>"\
        "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMjFxZDZxdXBnYXU3OGc4Y2UyNWpkc2M4aWoydGJiczVzdTc5bTJpMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/3o7TKtnuHOHHUjR38Y/giphy.gif'>"

@app.route('/<int:number>')
def check_guess(number:int):
    global secret_number
    if number<secret_number:
        return f"<h2 style='color:rgb(255,0,0);'> Too Low!</h2>"\
            "<img src='https://media2.giphy.com/media/oDK8A6xUNjD2M/giphy.webp?cid=ecf05e47hna4l3o7qz0uz96gadwkmknj7lsoq0w2zj9zzulf&rid=giphy.webp&ct=g'>"
    elif number>secret_number:
        return f"<h2 style='color:rgb(255,0,0);'> Too High!</h2>"\
            "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    return f"<h2> You're correct, the secret number is {secret_number}</h2>"\
            "<img src='https://giphy.com/gifs/thumbs-up-111ebonMs90YLu'>"

@app.route('/decorated_test')
@make_bold
@make_emphasis
@make_underline
def write():
    return "Decorator Tests... wkwkwkkw"

if __name__== '__main__':
    app.run(debug=True)