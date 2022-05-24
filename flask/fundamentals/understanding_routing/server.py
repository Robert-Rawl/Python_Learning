
from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!"

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<name>')
def say_hi(name):
    return f"Hi {name}!"

@app.route('/repeat/<int:num>/<string:anything>')
def repeat(num, anything):
    output =""

    for i in range(0,num):
        output += f'<p>{anything}</p>'
    return output




if __name__=="__main__":
    app.run(debug=True)