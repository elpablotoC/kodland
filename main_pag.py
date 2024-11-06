
from flask import Flask, url_for
import random

app = Flask(__name__)

# Lista de hechos al azar
random_facts = [
    "Los pulpos tienen tres corazones.",
    "El corazón de un camarón está en su cabeza.",
    "Una vaca produce alrededor de 200,000 vasos de leche en su vida.",
    "Los plátanos son bayas, pero las fresas no lo son.",
    "Las abejas pueden reconocer rostros humanos."
]

@app.route("/")
def home():
    return '''
    <h1>Hola, en esta página puedes aprender un par de cosas interesantes sobre las dependencias tecnológicas.</h1>
    <a href="''' + url_for('random_fact') + '''">¡Ver un hecho al azar!</a>
    '''

@app.route("/random_fact")
def random_fact():
    fact = random.choice(random_facts)
    return f'<h1>Hecho al azar:</h1><p>{fact}</p>'

if __name__ == "__main__":
    app.run(debug=True)
