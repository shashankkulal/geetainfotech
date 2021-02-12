from flask import Flask, render_template, request
from Geetainfotech import getSpeed

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/speedtest', methods=['POST'])
def checkSpeed():
    if request.method == 'POST':
        data = request.form['page']
        data = str(data).strip()
        return getSpeed(data)
    else:
        page = 'Error'
    return str(page)

if __name__ == '__main__':
    app.run()