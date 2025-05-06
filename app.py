from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'REY BENEDIC PAJUTA<br>BSIT-A<br>SYSTEM INTEGRATION AND ARCHITECTURE<br>SEMI-FINAL EXAM!'

if __name__ == '__main__':
    app.run(debug=True)