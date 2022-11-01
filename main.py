from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL

import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Map (URL)',validators=[DataRequired(), URL()])
    open = StringField('Opening Time e.g. 8AM', validators=[DataRequired()])
    close = StringField('Closing Time e.g. 5:30PM', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating',choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"], validators=[DataRequired()])
    wifi_rating = SelectField('WiFi Strength Rating',choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"], validators=[DataRequired()])
    power_rating = SelectField('Power Socket Availability ',choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")

""" Form to add a coffee shop to the cafe-data.csv file  """
@app.route('/add', methods=['GET','POST'])
def add_cafe():
    form = CafeForm()
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    if form.validate_on_submit():
        with open("cafe-data.csv", "a", encoding="utf-8") as csv_file:
            csv_file.write(f"\n{form.cafe.data},"
                       f"{form.location.data},"
                       f"{form.open.data},"
                       f"{form.close.data},"
                       f"{form.coffee_rating.data},"
                       f"{form.wifi_rating.data},"
                       f"{form.power_rating.data},")
            return redirect('/cafes')
    return render_template('add.html', form=form)

"""Display the list of coffee shops that are found in 'cafe-data.csv' (with data) """
@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        header = next(csv_data)
        list_of_rows = []
        """loop to  show the contain of each rows from the csv file"""
        for row in csv_data:
            list_of_rows.append(row)
        list_of_headers = []
        """loop to  show the header of the csv file"""
        for title in header:
            list_of_headers.append(title)
    return render_template('cafes.html', cafes=list_of_rows, header=list_of_headers )


if __name__ == '__main__':
    app.run(debug=True)
