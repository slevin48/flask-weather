from flask import Flask, render_template
import weather

app = Flask(__name__)
appid='b1b15e88fa797225412429c1c50c122a1'

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/", methods=['POST'])
def get_weather():
    # get weather message
    json_data = weather.get_current_weather('London','uk',appid,api='samples')
    data = weather.parse_current_json(json_data)
    return render_template('index.html', weather_message=data['temp']-273.15)

if __name__ == '__main__':
    app.run()