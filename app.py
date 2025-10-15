from flask import Flask, render_template, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    bmi = None
    category = None
    if request.method == 'POST':
        weight = float(request.form['weight'])
        height = float(request.form['height']) / 100  # convert cm to meters
        bmi = round(weight / (height ** 2), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')
