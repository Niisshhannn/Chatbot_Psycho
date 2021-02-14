from flask import Flask, render_template, request
app = Flask(__name__, static_folder="web/dist/static",
            template_folder="web/dist")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/api/init')
def chat_init():
    return {'test': '111'}


@app.route('/api/chat', methods=['POST'])
def chat_main():
    msg = request.json.get('msg')
    return {'msg': msg + '!!!!!!'}


if __name__ == '__main__':
    app.run(port=5000, debug=True)
