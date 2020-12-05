from flask import Flask
from markupsafe import escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/conversor/<int:pesos>')
def conversor_pesos_dolar(pesos):
   valor = pesos / 3815.82
   return 'Valor convertido a Dolar es :  %d' % valor


if __name__ == '__main__':
   app.run()