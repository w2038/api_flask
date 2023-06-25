from flask import Flask, request, jsonify

app = Flask(__name__)

livros = [
    {"id":1, "titulo":"O senhor dos aneis", "autor": "jrr tolkien"},
    {"id":2, "titulo":"harry portter", "autor":"jk rowling"}
]


@app.route("/livros")
def lista_lisvros():
    return jsonify(livros)

if __name__ == "__main__":
    app.run(debug=True)