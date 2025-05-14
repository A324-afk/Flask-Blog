from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config['sqlalchemy_database_URI']= "sqlite:////todo.db"
app.config['sqlalchemy_database_URI']=False
db=SQLAlchemy(app)
class todo(db.Model):
   sno=db.Column(db.integer,primary_key=True)
   title=db.Column(db.string(300),nullable=False)
   desc=db.Column(db.string(500),nullable=False)
   date_created=db.Column(db.datetime,dafault=datetime.utcnow)
   def __repr__(self) ->str:
      return f"{self.sno} -{self.title}"

@app.route("/")
def hello_world():
    return render_template("index.html")
    #return "<p>Hello, World!</p>"

@app.route("/produts")
def products():
   return "this is product page"


if __name__== "__main__":
  app.run(debug=True, port=8000)



 
