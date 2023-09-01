from flask import render_template, request
from application import create_app
from api import create_consumer, run_requests
from db.db_utils import get_all_consumers

# Create flask app
app = create_app()


@app.route('/', methods=["GET"])
def create():
    return render_template('initial.html')


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        consumer_request = create_consumer.createConsumerRequest(
            app, request.form)

        if consumer_request.status == "FAILED":
            return render_template('error.html', errors=consumer_request)

        return render_template('consumer_created.html', consumer=consumer_request)

    return render_template('register.html')


@app.route('/report', methods=["GET", "POST"])
def report():
    if request.method == 'POST':
        selected_items = request.form.getlist('selected_items')
        data = run_requests.getData(app, selected_items)
        return render_template('summary.html', data=data)

    consumers = get_all_consumers()
    return render_template('report_init.html', items=consumers)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
