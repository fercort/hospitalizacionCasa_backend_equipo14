
function getPaciente() {
    const urlpaciente = 'https://hopitalizacion-casa.herokuapp.com/getOnePaciente/';
    const id = 123;
  // Petición HTTP
  //fetch('https://proy-001.herokuapp.com/getAllCustomers/')

  //fetch('http://127.0.0.1:8000/getOnePaciente/' + id)
  //fetch('https://hopitalizacion-casa.herokuapp.com/getOnePaciente/')
  //fetch('https://hopitalizacion-casa.herokuapp.com/getOnePaciente/123')
  fetch( urlpaciente + id)


    .then(response => {
      console.log(response);
      if (response.ok)
        return  response.text()
      else
        throw new Error(response.status);
    })
    .then(data => {
      console.log("Datos: " + data);
      paciente = JSON.parse(data);
      handlePaciente();
    })
    .catch(error => {
        console.error("ERROR: ", error.message);      
      handleError();
    });
}
// function handlePaciente(paciente) {
//     const accInfo = [];
    //paciente.medicoss.forEach(acc => {
      //const singleAccInfo = `
        //<h4>Nombre: ${acc.nombre}</h4>
        //<h4>telefono: ${acc.telefono}</h4>`;
      //accInfo.push(singleAccInfo);
    //});
//     const custDiv = document.createElement("div");
//     custDiv.innerHTML = `
      
//       <h3>Nombre: ${paciente.nombre}</h3>
//       <h3>direccion: ${paciente.direccion}</h3>
//       <h3>telefono: ${paciente.telefono}</h3>
//       <h3>contacto: ${paciente.contacto}</h3>
//       <h3>telefono_contacto: ${paciente.telefono_contacto}</h3>
//       `;
//     accInfo.forEach(acc => custDiv.innerHTML );
//     document.getElementById("cargando").remove();
//     const info = document.getElementById("info-customers");
//     info.appendChild(custDiv);
  
//   }

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
    const info = document.getElementById("info-customers");
    divs.forEach(div => info.appendChild(div));
  }


  
  function handleError() {
    document.getElementById("cargando").remove();
    const message = document.createElement("p");
    message.innerText = "No se pudo cargar la información. Intente más tarde.";
    const info = document.getElementById("info-customers");
    info.appendChild(message);
   
  }
  
  //-----------------------------------
  
  document.addEventListener("DOMContentLoaded", getPaciente);