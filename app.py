from flask import Flask
from flask import render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY']='SuperSecretKey'


class MemberForm(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])


@app.route('/')
def index():
    return render_template('index.html', pageTitle='lakers team member')

@app.route('/add_member', methods=['GET','POST'])
def add_member():
    form = MemberForm()
    if form.validate_on_submit():
        return "<h2> Los Angeles Lakers team member name is {0} {1}".format(form.first_name.data, form.last_name.data)

    return render_template('add_member.html', form=form, pageTitle='Add A New Member')

if __name__ == '__main__':
    app.run(debug=True)
