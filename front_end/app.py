from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World"

if __name__ == "__main__":
    print(index())
    app.run(debug=True)