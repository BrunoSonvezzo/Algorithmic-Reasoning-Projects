let nome = document.getElementById('nome');
let telefone = document.getElementById('telefone');
let email = document.getElementById('email');
let senha = document.getElementById('senha');
let repitasenha = document.getElementById('repitasenha');
let form = document.querySelector('form');
let textform = document.getElementById('textform');
let textemail = document.getElementById('textemail');

form.addEventListener('submit', (e) => {
    if(nome.value == '' || telefone.value ==''  || email.value == '' || senha.value == ''  || repitasenha.value == ''){

    alert("Preencha todos os campos, por favor.") 
}
   
    else {
    console.log(nome.value);
    console.log(telefone.value);
    console.log(email.value);
    console.log(senha.value);
    console.log(repitasenha.value);
    }
    e.preventDefault()

});

email.addEventListener("keyup", () => {
    if (validatorEmail(email.value) !== true) {
      textemail.textContent = "O formato do email deve ser Ex: name@abc.com";
    } else {
      textemail.textContent = "";
    }
  })
function validatorEmail(email) {
    let emailPattern = /^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$/;
    return emailPattern.test(email);
  }
 
