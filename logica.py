from flask import jsonify

users = {
    "João": "joao@example.com",
    "Maria": "maria@example.com",
    "Pedro": "pedro@example.com"
}

users["Wagner"] = "wgnr@com.br"
del users["Pedro"]

for user in users:
    print(user)