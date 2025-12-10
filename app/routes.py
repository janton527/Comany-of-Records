from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Altimor'}
    return '''
<html>
    <head>
        <title>Home Page - Company of Records</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''
