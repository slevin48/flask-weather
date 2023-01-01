from flask import Flask, request, render_template
import plotly.express as px
import weather

app = Flask(__name__)
appid='b1b15e88fa797225412429c1c50c122a1'

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # get the value from the form
        city = request.form['city']
        country = request.form['country']
        # json_data = weather.get_current_weather(city,country,appid,api='samples')
        json_data = weather.get_forecast(city,country,appid,api='samples')
        data = weather.parse_forecast_json(json_data)
        time = data['current_time']
        temp = data['temp']
        # Create a Plotly figure
        fig = px.line(x=time, y=temp)
        fig.update_layout(title='Temperature Forecast', xaxis_title='Time', yaxis_title='Temperature')
        # Convert the figure to JSON
        fig_json = fig.to_json()
        return render_template('index.html', plot=fig_json)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()