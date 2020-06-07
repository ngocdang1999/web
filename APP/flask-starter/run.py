from flask import Flask ,render_template
app = Flask(__name__)

@app.route("/")
def index():  
     return render_template('index.html')

@app.route("/1")
def tivi():  
     return render_template('1.html')

@app.route("/2")
def tivi1():  
     return render_template('2.html')

@app.route("/3")
def tivi2():  
     return render_template('3.html')

@app.route("/4")
def tivi3():  
     return render_template('4.html')

@app.route("/5")
def tivi4():  
     return render_template('5.html')

@app.route("/6")
def tivi5():  
     return render_template('6.html')

@app.route("/7")
def tivi6():  
     return render_template('7.html')

@app.route("/8")
def tivi7():  
     return render_template('8.html')

@app.route("/9")
def tivi8():  
     return render_template('9.html')

@app.route("/11")
def tivi9():  
     return render_template('11.html')

@app.route("/22")
def tivi11():  
     return render_template('22.html')

@app.route("/33")
def tivi22():  
     return render_template('33.html')

@app.route("/44")
def tivi33():  
     return render_template('44.html')

@app.route("/55")
def tivi44():  
     return render_template('55.html')

@app.route("/66")
def tivi55():  
     return render_template('66.html')

@app.route("/66")
def tivi66():  
     return render_template('66.html')

@app.route("/thanhtoan")
def thanhtoan():  
     return render_template('thanhtoan.html')


@app.route("/thanhtoan0")
def thanhtoan0():  
     return render_template('thanhtoan0.html')

@app.route("/thanhtoan1")
def thanhtoan1():  
     return render_template('thanhtoan1.html')

@app.route("/thanhtoan2-1")
def thanhtoan2():  
     return render_template('thanhtoan2-1.html')

@app.route("/thanhtoan2")
def thanhtoan3():  
     return render_template('thanhtoan2.html')

@app.route("/thanhtoan3")
def thanhtoan4():  
     return render_template('thanhtoan3.html')

@app.route("/thanhtoan4")
def thanhtoan5():  
     return render_template('thanhtoan4.html')

@app.route("/thanhtoan5")
def thanhtoan6():  
     return render_template('thanhtoan5.html')

@app.route("/thanhtoan6")
def thanhtoan7():  
     return render_template('thanhtoan6.html')

@app.route("/thanhtoan7")
def thanhtoan8():  
     return render_template('thanhtoan7.html')

@app.route("/thanhtoan8")
def thanhtoan9():  
     return render_template('thanhtoan8.html')

@app.route("/thanhtoan9")
def thanhtoan10():  
     return render_template('thanhtoan9.html')

@app.route("/thanhtoan10")
def thanhtoan11():  
     return render_template('thanhtoan10.html')

@app.route("/thanhtoan11")
def thanhtoan12():  
     return render_template('thanhtoan11.html')

@app.route("/thanhtoan12")
def thanhtoan13():  
     return render_template('thanhtoan12.html')

@app.route("/thanhtoan13")
def thanhtoan14():  
     return render_template('thanhtoan13.html')

@app.route("/thanhtoan14")
def thanhtoan15():  
     return render_template('thanhtoan14.html')








@app.route("/donhang")
def donhang():  
     return render_template('donhang.html')




@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/hello/<string:name>/")
def hello_user(name):  
    return render_template('hello.html', name=name)


if __name__ == "__main__":  
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)
