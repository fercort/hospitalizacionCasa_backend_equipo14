pacientes = [];

function getPacientes() {
  // Petición HTTP
  //fetch('https://proy-001.herokuapp.com/getAllCustomers/')
  //fetch('https://proy-001.herokuapp.com/getAllCustomers/')
  
  //fetch('http://127.0.0.1:8000/getAllMedicos/')
  fetch('https://hopitalizacion-casa.herokuapp.com/getAllPacientes/')
  //fetch('https://hopitalizacion-casa.herokuapp.com/getOnePaciente/123')
  //fetch('https://hopitalizacion-casa.herokuapp.com/getOnePaciente')


    .then(response => {
      console.log(response);
      if (response.ok)
        return  response.text()
      else
        throw new Error(response.status);
    })
    .then(data => {
      console.log("Datos: " + data);
      pacientes = JSON.parse(data);
      handlePaciente();
    })
    .catch(error => {
      console.error("ERROR: ", error.message);
      handleError();
    });
}

function handlePaciente() {
  const divs = [];
  pacientes.forEach((cust) => {
    const div = document.createElement("div");
    div.innerHTML = `
      <h3>id_paciente: ${cust.id_paciente}</h3>
      <h3>nombre: ${cust.nombre}</h3>
      <h3>direccion: ${cust.direccion}</h3>
      <h3>telefono: ${cust.telefono}</h3>
      <h3>contacto: ${cust.contacto}</h3>
      <h3>telefono_contacto: ${cust.telefono_contacto}</h3>
      `;
    divs.push(div);
  });
  document.getElementById("cargando").remove();
  const info = document.getElementById("info-pacientes");
  divs.forEach(div => info.appendChild(div));
}

function handleError() {
  document.getElementById("cargando").remove();
  const message = document.createElement("p");
  message.innerText = "No se pudo cargar la información. Intente más tarde.";
  const info = document.getElementById("info-pacientes");
  info.appendChild(message);
}

//-----------------------------------

document.addEventListener("DOMContentLoaded", getPacientes); // cuando termine de cargar la pagina que me llame a la funcion getCustomers