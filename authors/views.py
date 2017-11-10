from flask_blog import app

@app.route('/login', methods =['GET','POST'])
def login():
   return "hello login page"