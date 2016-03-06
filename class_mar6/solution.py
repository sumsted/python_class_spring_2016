from bottle import get, template, run

@get('/')
def get_index():
    return template('index')

run(host='0.0.0.0', port=8080)
