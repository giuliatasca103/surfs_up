from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

def hello_me():
    return 'Hello Me'

if __name__=='__main__': 
    app.run(debug=True)