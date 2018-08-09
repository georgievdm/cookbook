import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo

app= Flask(__name__)
app.config['MONGO_DBNAME'] = 'task_manager'
app.config['MONGO_URI'] = 'mongodb://admin:admin123@ds217092.mlab.com:17092/task_manager'

mongo = PyMongo(app)


app = Flask(__name__)

@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    return render_template("tasks.html",
    tasks=mongo.db.tasks.find())


#@app.route('/')
#def hello():
#    return 'Task Manager'

if __name__ == '__main__':
    app.run(host=os.environ.get('IP', '0.0.0.0'),
        port=int(os.environ.get('PORT', 8080)),
        debug=True)
