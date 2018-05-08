#!flask/bin/python
from flask import Flask, jsonify, request, render_template
from lib.consulta import Consulta
from lib.utils import criar_sessao

sessao = criar_sessao()

app = Flask(__name__)

@app.route("/consultas", methods=["GET", "POST"])
def consultas():
    if request.method == "GET":
        order_by = request.args.get('orderBy')
        resposta = Consulta.get_consultas(sessao, order_by)
        return render_template('index.html', consultas=resposta)
    dados = request.json
    consulta = Consulta(dados["paciente"], dados["exame"])
    Consulta.criar(consulta, sessao)

    return "Consulta criada e salva com sucesso!", 200
if __name__ == "__main__":
    app.run(debug=True)
