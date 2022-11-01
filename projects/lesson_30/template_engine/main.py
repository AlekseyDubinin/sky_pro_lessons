from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/users/<id>')
def users(id):
    return render_template(
        'show.html',
        id=id,
    )

app.run(debug=True)