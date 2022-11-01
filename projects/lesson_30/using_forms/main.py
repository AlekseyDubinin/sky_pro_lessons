from flask import Flask, request
from flask import render_template

app = Flask(__name__)

use = ['mike', 'mishel', 'adel', 'keks', 'kamila']


@app.route('/users')
def users():
    term = request.args.get('term')
    if term:
        filtered_users = filter(lambda x: term in x, use)
    else:
        filtered_users = use
        term = ''

    return render_template(
        'users/index.html',
        userss=filtered_users,
        search=term,
    )


app.run(debug=True)