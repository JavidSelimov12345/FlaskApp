from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def hello():
   
    return "<h1>Hello</h1>"

@app.route('/about')
def about():
    return "javidin flaski"    

if __name__=='__main__':
    app.run(debug=True)