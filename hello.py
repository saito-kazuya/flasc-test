from flask import Flask, render_template ## render_templateを追加

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') ## render_templateを使用

## 起動用
if __name__ == "__main__":
    app.run(debug=True)