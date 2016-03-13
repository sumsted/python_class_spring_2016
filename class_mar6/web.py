from bottle import get, template, run

# http://0.0.0.0:8080/

@get('/')
def get_index():
    web_page = template('index')
    return web_page


run(host='0.0.0.0', port=8080)