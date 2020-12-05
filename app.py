from flask import Flask, request, render_template
from markupsafe import escape
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def amortizacion():
 if request.method == 'POST': 
    pagetitle = 'Tabla Amortizacion:'
    lista_amortizacion = [

    ]
  
    valorprestado = int(request.form['valor'])
    tasa_interes = int(request.form['interes'])
    tiempo_limite = int(request.form['tiempo'])

    amortizacion = round(valorprestado/tiempo_limite)
    saldo = valorprestado
    
    for i in range(int(tiempo_limite)):
        interes_generado = round((saldo * (tasa_interes/100)))
        valorpagar = interes_generado + amortizacion
        saldo = (saldo + interes_generado) - valorpagar
        deudainicial = round(saldo + amortizacion)
        if saldo < 0:
           saldo = 0 
        lista_amortizacion.append(
            {
                'Mes': int(i+1),
                'Deuda Inicial $': float(deudainicial),
                'Interes Generado $': float(interes_generado),
                'Amortizacion $': float(amortizacion),
                'Valor a pagar $': float(valorpagar),
                'Deuda Final $': float(saldo)
            }
        )

    return render_template(
        'index.html',
        mytitle=pagetitle,
        lista_amortizacion=lista_amortizacion
    )


@app.route('/conversor/<int:pesos>')
def conversor_pesos_dolar(pesos):
   valor = pesos / 3815.82
   return 'Valor convertido a Dolar es :  %d' % valor


if __name__ == '__main__':
   app.run()

