from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/weather/", methods=['POST'])
def get_weather():
    # Dummy get weather message
    weather_message = "Sunny"
    return render_template('index.html', weather_message=weather_message);