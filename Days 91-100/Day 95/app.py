from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/weather/<city>')
def weather(city):
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY'
    response = requests.get(url)
    data = response.json()
    temperature = round(data['main']['temp'] - 273.15, 1)
    description = data['weather'][0]['description']
    return render_template('weather.html', city=city, temperature=temperature, description=description)


if __name__ == '__main__':
    app.run(debug=True)
