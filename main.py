# Importar a classe Flask e o objeto request:
from flask import Flask, request
# Criar o objeto Flask app:
app = Flask(__name__)

@app.route('/valor', methods=['GET', 'POST'])
def maior_menor_media():
    # Trata a requisição com método POST:
    if request.method == 'POST':
        valor01 = int(request.form.get('valorA'))
        valor02 = int(request.form.get('valorB'))
        valor03 = int(request.form.get('valorC'))

        maior = valor01
        if maior < valor02:
            maior = valor02
        if maior < valor03:
            maior = valor03

        menor = valor01
        if menor > valor02:
            menor = valor02
        if menor > valor03:
            menor = valor03    

        media = (valor01 + valor02 + valor03) / 3

        return '''

            <h1>Maior: {}</h1>
            <h1>Menor: {}</h1>
            <h1>Media: {}</h1>'''.format(maior, menor,media)

    return '''
        <form method="POST">
            <div><label>valor01: <input type="text"name="valorA"></label></div>
            <div><label>valor02: <input type="text"name="valorB"></label></div>
            <div><label>valor03: <input type="text"name="valorC"></label></div>
            <input type="submit" value="Enviar">
        </form>'''


@app.route('/imc', methods=['GET', 'POST'])
def formulario_imc():
    # Trata a requisição com método POST:
    if request.method == 'POST':
        altura =  float(request.form.get('altura'))
        peso = float(request.form.get('peso'))

        indice = peso / pow(altura, 2) 

        if(indice <= 18.5):
            imc = 'abaixo do peso'
        elif(indice >= 18.6 and indice <= 24.9):
            imc = 'peso ideal parabens'
        elif(indice >= 25.0 and indice <= 29.9):
            imc = 'levemete acima do peso'
        elif(indice >= 30.0 and indice <= 34.9):
            imc = 'obesidade grau 1'
        elif(indice >= 35.0 and indice <= 39.9):
            imc = 'obesidade grau II'
        else:
            imc = 'obesidade grau III'

        return '''
            <h1>IMC: {}</h1>'''.format(imc)

    return '''
        <form method="POST">
            <div><label>altura: <input type="text"name="altura"></label></div>
            <div><label>peso: <input type="text"name="peso"></label></div>
            <input type="submit" value="Enviar">
        </form>'''



if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)