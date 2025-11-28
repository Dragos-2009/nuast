from flask import Flask

app = Flask(__name__)

@app.route("/")
def helloWorld():
    return "Hello World"

@app.route("/getFlashcard/<flashcard>")

def main():
    app.run()

if __name__ == "__main__":
    main()
