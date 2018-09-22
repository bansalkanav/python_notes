from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    puppies = ['abc', 'lmn', 'xyz']
    return render_template('03-Template-Control-Flow.html',
                           puppies=puppies)


if __name__ == '__main__':
    app.run(debug=True)
