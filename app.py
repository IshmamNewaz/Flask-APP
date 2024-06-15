from flask import Flask,redirect,url_for
app=Flask(__name__) #Name of the Flask Application Name
@app.route('/') # This will trigger the next below function with same name. This is an app decorator for building URL
def welcome():
    return "Welcome to My App Good day"


@app.route('/fail/<float:score>')
def fail(score):
    return "Failed and mark is: "+ str(score)


@app.route('/passed/<float:score>')
def passed(score):
    return "Passed and mark is: "+ str(score)




@app.route('/chk/<float:res>')
def LikeGetMethod(res):
    if res>49:
        page_url = "passed"
    else:
        page_url = "fail"
    return redirect(url_for(page_url, score=res))




if __name__ == '__main__': # Starting point of Program Application
    app.run(debug=True) #will change in live everytime The file is saved