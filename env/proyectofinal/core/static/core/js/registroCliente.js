var getDatos = function(){
    var nombre = document.getElementById("nombres").value;
    var apellido = document.getElementById("apellidos").value;
    var correo = document.getElementById("correo").value;
    var contra = document.getElementById("contrasena").value;
    if (nombre == "") {
        document.getElementById("nombres").focus();
    } else {
        if (apellido == "") {
            document.getElementById("apellidos").focus();
        }else{
            if (correo == "") {
                document.getElementById("correo").focus();
            }else{
                if (contra=="") {
                    document.getElementById("contrasena").focus();
                }else{
                    document.getElementById("nombres").value = "";
                    document.getElementById("apellidos").value = "";
                    document.getElementById("correo").value = "";
                    document.getElementById("contrasena").value = "";+
                    document.getElementById("nombres").focus();
                }
            }
        }
    }
    console.log(nombre+" "+apellido+" "+correo+" "+contra);
}