from flask import Flask, render_template ## render_template��ǉ�

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') ## render_template���g�p

## �N���p
if __name__ == "__main__":
    app.run(debug=True)