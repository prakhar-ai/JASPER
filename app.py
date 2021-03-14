from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
import re
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class TaskData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(300))
    effort = db.Column(db.Integer)
    urgency = db.Column(db.Integer)
    importance = db.Column(db.Integer)
    label = db.Column(db.String(100))


@app.route("/")
@app.route("/home")		
def home():
    return render_template('home.html', active='home')

@app.route("/addtask", methods=["POST"])
def addtask():
    task = request.form.get("task")
    effort  = request.form.get("effort")
    urgency = request.form.get("urgency")
    importance = request.form.get("importance")
    label  = request.form.get("label")
    new_data = TaskData(task=task, effort=effort, urgency=urgency, importance=importance,label=label)
    db.session.add(new_data)
    db.session.commit()
    return redirect(url_for("database"))


@app.route("/database")		
def database():
    Tasklist = TaskData.query.all()
    return render_template('database.html', title='Database', active='database',Tasklist=Tasklist)

@app.route("/chart3")			
def statistics():
    return render_template('chart3.html', title='chart3', active='chart3')


@app.route("/chart")	
def howitworks():
    return render_template('chart.html', title='How it works', active='chart')


@app.route("/chart2")		
def credits():
    return render_template('chart2.html', title='Chart2', active='chart2')

@app.route("/add")
def add():
    return render_template('add.html', title='Add', active='add')
    
def getApp():
    return app
    
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)		

