from flask import Blueprint, render_template, request, redirect, url_for, flash
import requests

# Criando o Blueprint para o clima
cotacoes_bp = Blueprint('cotacoes', __name__, template_folder='templates/cotacoes')

@cotacoes_bp.route("/cotacoes", methods=["GET", "POST"])
def cotacoes():
    return "<h1>alguma coisa</h1>"
    if request.method == "POST":
            city = request.form.get("city")
            api_key = "46aebe122fb2bbf95d955e886be39685"
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            complete_url = f"{base_url}?q={city}&appid={api_key}&units=metric"
            response = requests.get(complete_url)
            data = response.json()

            if data["cod"] != "404" and "name" in data:
                weather_data = {
                    "city": data["name"],
                    "temperature": data["main"]["temp"],
                    "description": data["weather"][0]["description"],
                    "icon": data["weather"][0]["icon"],
                }
                return render_template("cotacoes/cotacoes.html", weather_data=weather_data)
            else:
                flash("Cidade não encontrada. Tente novamente.")
                return redirect(url_for("cotacoes"))
    return render_template("cotacoes/cotacoes.html")