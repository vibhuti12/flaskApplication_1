from flask_blog import app

@app.route('/')
@app.route('/index')
def index():
    return "Hey, There!!"