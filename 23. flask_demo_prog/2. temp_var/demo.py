from flask import Flask, render_template
app = Flask(__name__)


@app.route('/info/<name>')
def info(name):
    return render_template('demo.html', var_1 = name)

if __name__ == '__main__':
    app.run(debug=True)
