from flask import render_template, request
from api import run_requests
from application import create_app

# Create flask app
app = create_app()


@app.route('/', methods=["GET"])
def create():
    return render_template('register.html')


@app.route('/result', methods=["POST"])
def getResult():
    response = run_requests.getData(app, request.form)

    if response.status == 'FAILED':
        return render_template('error.html', errors=response)
    return render_template('success.html', consumer=response, data=response.data, sku=app.config["SKU"])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
