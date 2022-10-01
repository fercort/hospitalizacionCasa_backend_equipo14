//const updateMedicoUrl = 'https://mintic-bancoproj-g2.herokuapp.com/updateMedico/';
const updateMedicoUrl = 'http://127.0.0.1:8000/updateMedico/';

//const userId = 147; //no

const parsedUrl = new URL(window.location.href);
//console.log(parsedUrl);
const userId = parsedUrl.searchParams.get("id");


function collectData(evt) {
    evt.preventDefault();



    const nombre = document.actualizar.nombre.value.trim();
    const direccion = document.actualizar.direccion.value.trim();
    const telefono = document.actualizar.telefono.value.trim();
    const especialidad = document.actualizar.especialidad.value;

   

    const medico = {}
    if (nombre)
        medico.nombre = nombre;
    if (direccion)
        medico.direccion = direccion;
    if (telefono)
        medico.telefono = telefono;
    if (especialidad)
        medico.especialidad = especialidad;
    console.log(medico);
    const dataToSend = JSON.stringify(medico);
    updateMedico(dataToSend);
}

function updateMedico(data) {
   
    fetch(updateMedicoUrl + userId , {
        method: "PUT",
        headers: {
            "Content-Type": "application/json",
        },
        body: data
    })
        .then(response => {
            console.log(response);
            if (response.ok)
                return response.text()
            else
                throw new Error(response.text());
        })
        .then(data => {
            console.log(data);
            alert('Datos actualizados');
            goBack();
        })
        .catch(error => {
            console.error("ERROR: ", error.message);
            alert('Error al actualizar datos');
            goBack();
        });
}

function goBack() {
    //window.location.href = './cliente.html?id=' + userId;
    window.location.href = './consulta_pacientes.html';
}


// --------------------
document.actualizar.addEventListener("submit", collectData);
