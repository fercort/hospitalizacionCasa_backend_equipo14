
newPacienteUrl = 'https://hopitalizacion-casa.herokuapp.com/newPaciente/'

// funcion para solo permitir letras en lugar de numeros en la casilla de nombre 
function validate_names(val) {
    const letters = /^[A-Z a-zÁÉÍÓÚáéíóúñ]+$/;
    if (val.match(letters))
        return true;
    else
        return false;
}




function collectData(evt){
    evt.preventDefault();

    const id_paciente = document.registro.id_paciente.value;
    const nombre = document.registro.nombre.value.trim(); // metodo trim() elimina los espacios inicial y final
    const direccion = document.registro.direccion.value.trim();
    const telefono = document.registro.telefono.value.trim();
    const contacto = document.registro.contacto.value.trim();
    const telefono_contacto = document.registro.telefono_contacto.value; 

    result = validate_names(nombre);
    if (!result) {
        alert('Nombre no es válido');
        return;
    }



    const paciente ={
        id_paciente : id_paciente,
        nombre: nombre,
        direccion : direccion,
        telefono : telefono,
        contacto :contacto,
        telefono_contacto : telefono_contacto
    }
    console.log(paciente);
    const dataToSend = JSON.stringify(paciente);
    savePaciente(dataToSend);

}

function savePaciente(data){
    // peticion HTTP
    fetch(newPacienteUrl, {
        method: "POST",
        headers: {
            "Content-Type": "text/json"
        },
        body: data
    })

    .then(response => {
        //console.log(response);
        if (response.ok)
            return response.text()
        else
            throw new Error(response.status);
    })

    .then(data => {
        console.log(data);
        handleSuccess();
    })
    .catch(error => {
        console.error("ERROR: ", error.message);
        handleError();
    });
}

function handleSuccess() {
    document.getElementById("formData").remove();
    const message = document.createElement("p");
    message.innerText = "paciente creado exitosamente.";
    const info = document.getElementById("info");
    info.appendChild(message);
}


function handleError() {
    document.getElementById("formData").remove();
    const message = document.createElement("p");
    message.innerText = "No se puede crear el paciente.";
    const info = document.getElementById("info");
    info.appendChild(message);
}
  

document.registro.addEventListener("submit", collectData)

