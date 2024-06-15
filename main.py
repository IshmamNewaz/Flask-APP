from flask import Flask,redirect,url_for,render_template,request
app=Flask(__name__) #Name of the Flask Application Name
@app.route('/') # This will trigger the next below function with same name. This is an app decorator for building URL
def welcome():
    return render_template("form.html")


@app.route('/fail/<float:score>')
def fail(score):
    return render_template("failed.html", score = score)


@app.route('/passed/<float:score>')
def passed(score):
    return render_template("passed.html", score = score)



@app.route('/submit', methods=['POST', 'GET'])
def submit():
    ttl_score = 0
    if request.method=='POST':
        eng=float(request.form['english'])
        ban=float(request.form['bangla'])
        math=float(request.form['math'])
        ttl_score = (eng+ban+math)/3
    
    result=""
    if ttl_score>49:
        result = "passed"
    else:
        result = "fail"

    return redirect(url_for(result, score=ttl_score))


if __name__ == '__main__': # Starting point of Program Application
    app.run(debug=True) #will change in live everytime The file is saved