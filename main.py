from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def template():
    return render_template("samplefile.html")

@app.route('/userInp', methods=['POST'])
def usuario():

    user = request.form['user']
    print(user)
    
    return user
if __name__ == '__main__':
    app.run(debug=True)