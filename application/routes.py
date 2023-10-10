from application import app
from flask import render_template, url_for, request
import json 
import plotly
import plotly_express as px

from application.database import Database
db = Database()


years = db.get_years()
@app.route('/')
def index():
    # Graph One
    return render_template("layout.html", years=years)

@app.route('/estadisticas', methods=['POST'])
def diagnosis():
    year = request.form['year']
    results = db.get_diagnosis(year)
    x_values = [result[0] for result in results]
    y_values = [result[1] for result in results]
    fig1 = px.pie(results, names= x_values, values=y_values, title=f"Enfermedades de los Univallunos, año {year}")
    fig_json = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)
    return render_template("figure.html", years=years, fig_json=fig_json)

