from flask import Flask, request, render_template
import weather

app = Flask(__name__)
appid='b1b15e88fa797225412429c1c50c122a1'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get the value from the form
        city = request.form['city']
        country = request.form['country']
        json_data = weather.get_current_weather(city,country,appid,api='samples')
        data = weather.parse_current_json(json_data)
        return render_template('index.html', results=data['temp']-273.15)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()