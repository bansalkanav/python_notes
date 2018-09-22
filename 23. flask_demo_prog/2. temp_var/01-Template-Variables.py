from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> Go to /puppy/name </h1>'


@app.route('/puppy/<name>')
def adv_puppy_name(name):
    letters = list(name)
    pup_dict = {'pup_name':name}
    return render_template('temp_var.html',
                           name=name,mylist=letters,mydict=pup_dict)


if __name__ == '__main__':
    app.run(debug=True)
