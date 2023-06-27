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

@app.route("/livros/<int:livro_id>", methods=['PUT'])
def atualizar_livro(livro_id):
    livro_atualizar = request.get_json()
    for livro in livros:
        if livro['id'] == livro_id:
            livro.update(livro_atualizar)
            return jsonify({'mensagem':'livro atualizado com sucesso'})
    return jsonify({"mensagem": "livro não encontrado"})

@app.route("/livros/<int:livro_id>", methods=['DELETE'])
def deletar_livro(livro_id):
    for livro in livros:
        if livro['id'] == livro_id:
            livros.remove(livro)
            return jsonify({'mensagem':'livro deletado com sucesso!'})
    return jsonify({'mensagem': 'Livro não encontrado'})

if __name__ == "__main__":
    app.run(debug=True)