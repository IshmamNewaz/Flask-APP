from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__) #Name of the Flask Application Name
@app.route('/') # This will trigger the next below function with same name. This is an app decorator for building URL


# {%......%} conditions, for loops
# {{}} expressions to print output
# {#.....#} comments




def welcome():
    return render_template("form.html")


# @app.route('/fail/<float:score>')
# def fail(score):
#     return render_template("failed.html", score = score)


# @app.route('/passed/<float:score>')
# def passed(score):
#     return render_template("passed.html", score = score)

@app.route('/checker/<float:score>')
def checker(score):
    return render_template("result.html", score = score)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    ttl_score = 0
    if request.method=='POST':
        eng=float(request.form['english'])
        ban=float(request.form['bangla'])
        math=float(request.form['math'])
        ttl_score = (eng+ban+math)/3

    return redirect(url_for('checker', score=ttl_score))


if __name__ == '__main__': # Starting point of Program Application
    app.run(debug=True) #will change in live everytime The file is saved