from unicodedata import name
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkers():
    return render_template('index.html',row=8,col=8,color_one='red',color_two='black')

@app.route('/<int:x>')
def checkers_row(x):
    return render_template('index.html', row=x,col=8,color_one='red',color_two='black')

@app.route('/<int:x>/<int:y>')
def checkers_row_col(x,y):
    return render_template('index.html', row=x, col=y, color_one='red',color_two='black')

@app.route('/<int:x>/<int:y>/<string:color1>')
def checkers_row_col_color1(x,y,color1):
    return render_template('index.html',row=x,col=y,color_one=color1,color_two='black')

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def checkers_row_col_color1_color2(x,y,color1,color2):
    return render_template('index.html',row=x,col=y,color_one=color1,color_two=color2)







if __name__=="__main__":
    app.run(debug=True)