from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate,identity


app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['PROPAGATE_EXCEPTIONS']=True
app.secret_key='snake'
api=Api(app)

@app.before_first_request
def create_tables():
    db.create_all()



jwt=JWT(app,authenticate,identity) #/auth 

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)