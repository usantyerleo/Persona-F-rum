const form = document.getElementById("form");
const nome = document.getElementById("Nome");
const email = document.getElementById("email");
const senha = document.getElementById("senha");
const rsenha = document.getElementById("rsenha");
const idade = document.getElementById("idade");

form.addEventListener('submit', (event) => {
    checkForm();
});

function checkIdade() {
    if (idade.value === "") {
        inputErro(idade, "Preencha uma data");
    } else {
        const item = idade.parentElement;
        item.className = "cont";
    }
}

function checkNome() {
    if (nome.value === "") {
        inputErro(nome, "Preencha um nome");
    } else {
        const item = nome.parentElement;
        item.className = "cont";
    }
}

function checkEmail() {
    if (email.value === "") {
        inputErro(email, "Preencha um email");
    } else {
        const item = email.parentElement;
        item.className = "cont";
    }
}

function checkSenha() {
    if (senha.value === "") {
        inputErro(senha, "Senha obrigatória");
    } else {
        const item = senha.parentElement;
        item.className = "cont";
    }
}

function checkRsenha() {
    const valorSenha = senha.value;
    const valorSenhaConfirmacao = rsenha.value;
    if (valorSenhaConfirmacao === "") {
        inputErro(rsenha, "Obrigatório confirmar senha");
    } else if (valorSenhaConfirmacao !== valorSenha) {
        inputErro(rsenha, "As senhas não são iguais");
    } else {
        const item = rsenha.parentElement;
        item.className = "cont";
    }
}

function checkForm() {
    checkNome();
    checkEmail();
    checkSenha();
    checkRsenha();
    checkIdade();
    const items = form.querySelectorAll(".cont");

    const valido = [...items].every((item) => {
        return item.className === "cont";
    });

    if (valido) {
        form.submit();
    }
}

function inputErro(input, msg) {
    const item = input.parentElement;
    const texto = item.querySelector("a.erro-msg");

    texto.innerText = msg;
    item.className = "cont erro";
}