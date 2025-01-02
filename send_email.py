from dotenv import load_dotenv
import os
import smtplib
from email.mime.text import MIMEText
from tmdb_scrapping import títulos, enlaces, posters, ratings, fechas

load_dotenv()

# Configuración del correo
smtp_server = "smtp.gmail.com"
port = 587
sender_email = os.getenv("SENDER_EMAIL")
password = os.getenv("PASSWORD")
receiver_email = os.getenv("RECEIVER_EMAIL")
subject = "Películas Populares TMDB"

peliculas = ""
for i in range(len(títulos)):
    peliculas += f"""
    <div class='pelicula'>
        <div class='poster'>
            <a title='{títulos[i]}' href='{enlaces[i]}'><img src='{posters[i]}' alt='Poster de {títulos[i]}'></a>
        </div>
        <div class='info'>
            <h3>{títulos[i]}</h3>
            <p>{fechas[i]}</p> 
            <p>Valoración: {ratings[i]}%</p>
        </div>

    </div>
    """


with open("mensaje.html", "r", encoding="utf-8") as file:
    message_body = file.read() 

message_body = message_body.replace("{{ peliculas }}", peliculas)

# Crear el mensaje
message = MIMEText(message_body, "html")
message["Subject"] = subject
message["From"] = "TMDB Películas Populares"
message["To"] = receiver_email

# Enviar el correo
with smtplib.SMTP(smtp_server, port) as server:
    server.starttls()  # Seguridad
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())