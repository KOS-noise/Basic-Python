from pathlib import Path
from flask import Flask
from bs4 import BeautifulSoup

app = Flask(__name__)

# Load the sample XML file next to the python-file folder.
xml_path = Path(__file__).parent / "weather_sample.xml"

@app.route("/")
def weather():
    target = xml_path.read_text(encoding="utf-8")
    soup = BeautifulSoup(target, "html.parser")

    output = "<h1>Weather Forecast</h1>"

    for location in soup.select("location"):
        city = location.select_one("city").get_text(strip=True)
        weather = location.select_one("wf").get_text(strip=True)
        low = location.select_one("tmn").get_text(strip=True)
        high = location.select_one("tmx").get_text(strip=True)

        output += f"<h2>{city}</h2>"
        output += f"Weather: {weather}<br/>"
        output += f"Low / High: {low}°C / {high}°C"
        output += "<hr/>"

    return output
