from flask import Flask, request, jsonify

app = Flask(__name__)

livros = [
    {"id":1, "titulo":"O senhor dos aneis", "autor": "jrr tolkien"},
    {"id":2, "titulo":"harry portter", "autor":"jk rowling"}
]


@app.route("/livros")
def lista_livros():
    return jsonify(livros)

@app.route("/livros/<int:livro_id>", methods=['GET'])
def lista_livro(livro_id):
    for livro in livros:
        if livro['id'] == livro_id:
            return jsonify(livro)
    return jsonify({"mensagem":"Livro não encontrado"}), 404

@app.route("/livros", methods=['POST'])
def adicionar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify({"mensagem": "livro adicionado com sucesso!"})

if __name__ == "__main__":
    app.run(debug=True)