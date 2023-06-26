from flask import Flask, request, jsonify

app = Flask(__name__)

livros = [
    {"id":1, "titulo":"O senhor dos aneis", "autor": "jrr tolkien"},
    {"id":2, "titulo":"harry portter", "autor":"jk rowling"}
]


@app.route("/livros")
def lista_lisvros():
    return jsonify(livros["id"])

@app.route("/livros/<int:livro_id>", methods=['GET'])
def lista_livro(livro_id):
    for livro in livros:
        if livro['id'] == livro_id:
            return jsonify(livro)
    return jsonify({"mensagem":"Livro não encontrado"}), 404

if __name__ == "__main__":
    app.run(debug=True)