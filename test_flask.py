from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
from app import app

@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('../static/css', path)

@app.route('/scss/<path:path>')
def send_scss(path):
    return send_from_directory('../static/scss', path)

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('../static/js', path)

@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('../static/img', path)

@app.route('/vendor/<path:path>')
def send_vendor(path):
    return send_from_directory('../static/vendor', path)

#if __name__ == "__main__":
#    app.run()
