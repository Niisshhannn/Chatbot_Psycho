# -*- coding: UTF-8 -*-

from flask import Flask, render_template, request
from server.chatcore import chat

app = Flask(__name__, static_folder="web/dist/static",
            template_folder="web/dist")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/chat', methods=['POST'])
def chat_main():
    msg = request.json.get('msg')
    typ = request.json.get('type')
    lang = request.json.get('lang')
    return chat(msg, lang, typ)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
