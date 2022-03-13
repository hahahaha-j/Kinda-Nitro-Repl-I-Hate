from flask import Flask
from threading import Thread

app = Flask('')

@app.route('/')
def main():
    return "Who needs nitro?"

def run():
    app.run(host="0.0.0.0", port=8080)

def go():
    server = Thread(target=run)
    server.start()