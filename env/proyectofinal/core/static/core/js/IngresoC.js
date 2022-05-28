var loginC = function(){
    var user=document.getElementById("usuario").value;
    var password=document.getElementById("contrasena").value;
    if (user=="Carolina" && password=="1234") {
        window.location="galeria.html";
    } if (user=="Felipe" && password=="123") {
        window.location="galeria.html";
    }if (user=="Jessica" && password=="1234") {
        window.location="galeria.html";
    }
    console.log(user+""+password);
}