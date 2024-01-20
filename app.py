from flask import Flask

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return 'Welcome to my Python website!'

if __name__ == '__main__':
    app.run()