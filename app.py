from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'REY BENEDIC G. PAJUTA<br>BSIT-A 2nd 25<br>SYSTEM INTEGRATION AND ARCHITECTURE 1<br>SEMI-FINAL EXAM!'

if __name__ == '__main__':
    app.run(debug=True)