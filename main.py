from flask import Flask, render_template, request, redirect, url_for, flash
#Definindo chave Flash, criando um dicionário de usuários e uma lista de tópicos
app = Flask(__name__)
app.secret_key = 'supersecretkey'

usuarios = {}

topicos = []
#Definindo rotas
@app.route("/")
def home():
    return render_template("Landing_Page.html")

@app.route("/Login", methods=['GET', 'POST'])
def login():
    #Salvando dados do formulário e fazendo a validação do login
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']
        if email in usuarios and usuarios[email] == senha:
            return redirect(url_for('forum_principal'))
        else:
            flash("Email ou senha inválidos. Tente novamente.")
    return render_template("Login.html")

@app.route("/Cadastro", methods=['GET', 'POST'])
def cadastro():
    #Salvando dados do formulário de cadastro e validando
    if request.method == 'POST':
        nome = request.form['Nome']
        email = request.form['email']
        idade = request.form['idade']
        senha = request.form['senha']
        rsenha = request.form['rsenha']
        if senha == rsenha:
            if email not in usuarios:
                usuarios[email] = senha
                flash("Cadastro realizado com sucesso!")
                return redirect(url_for('login'))
            else:
                flash("Email já cadastrado. Tente novamente.")
        else:
            flash("As senhas não coincidem. Tente novamente.")
    return render_template("Cadastro.html")

@app.route("/forum_principal")
def forum_principal():
    #Criando Id para cada tópico e comentário
    for i, topico in enumerate(topicos):
        topico["id"] = i
        for j, comentario in enumerate(topico["comentarios"]):
            comentario["id"] = j
    return render_template("forum principal.html", topicos=topicos)

@app.route("/adicionar_topico", methods=["POST"])
def adicionar_topico():
    #Adiciona um dicionário dentro da lista tópicos com as chaves texto e comentários, o valor de comentários é uma lista vazia
    novo_topico = request.form["novo_topico"]
    topicos.append({"texto": novo_topico, "comentarios": []})
    return redirect(url_for("forum_principal"))

@app.route("/adicionar_comentario/<int:topico_id>", methods=["POST"])
def adicionar_comentario(topico_id):
    #Adiciona um dicionário dentro da lista comentários com a chave texto
    novo_comentario = request.form["novo_comentario"]
    topicos[topico_id]["comentarios"].append({"texto": novo_comentario})
    return redirect(url_for("forum_principal"))

@app.route("/editar_comentario/<int:topico_id>/<int:comentario_id>", methods=["POST"])
def editar_comentario(topico_id, comentario_id):
    #Atribui o valor do campo de texto do formulário para o dicionário comentário, caso deseje editar o texto
    novo_texto = request.form["novo_texto"]
    topicos[topico_id]["comentarios"][comentario_id]["texto"] = novo_texto
    return redirect(url_for("forum_principal"))

@app.route("/excluir_comentario/<int:topico_id>/<int:comentario_id>", methods=["POST"])
def excluir_comentario(topico_id, comentario_id):
    #Remove o dicionário comentário da lista de comentários
    del topicos[topico_id]["comentarios"][comentario_id]
    return redirect(url_for("forum_principal"))


if __name__ == "__main__":
    app.run(debug=True)
