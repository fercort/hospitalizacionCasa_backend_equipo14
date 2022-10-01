
 const loginUrl = 'https://hopitalizacion-casa.herokuapp.com/login/';
 //const loginUrl = 'http://127.0.0.1:8000/login/';




function collectData(evt){
    evt.preventDefault();

    const id_medico = document.login.id_medico.value;
    const nombre = document.login.nombre.value.trim(); // metodo trim() elimina los espacios inicial y final

    const medico ={
        id_medico : id_medico,
        nombre: nombre
    }
    console.log(medico);
    const dataToSend = JSON.stringify(medico);
    login(dataToSend);

}

function login(data){
    // peticion HTTP
    fetch(loginUrl, {
        method: "POST",
        headers: {
            "Content-Type": "text/json"
        },
        body: data
    })

    .then(response => {
        //console.log(response);
        if (response.ok || response.status==401)
            return response.text()
        else
            throw new Error(response.status);
    })
    .then(data => {
        console.log(data);
        if (data.includes("Credenciales invalidas")){
            handleError(data);
        }
        handleSuccess(JSON.parse(data));
    })
    .catch(error => {
        console.error("ERROR: ", error.message);
        handleError();
    });
}

function handleSuccess(data) {
    document.getElementById("formData").remove();
    const message = document.createElement("p");
    message.innerText = "ingreso exitoso.";
    const info = document.getElementById("info");
    info.appendChild(message);
    window.location.href = './consulta_pacientes.html';
}


function handleError(err) {
    document.getElementById("formData").remove();
    const message = document.createElement("p");
    if (err)
        message.innerText = err;
    else
        message.innerText = "No se pudo ingresar. Intente luego.";
    const info = document.getElementById("info");
    info.appendChild(message);
}
  

document.login.addEventListener("submit", collectData);

