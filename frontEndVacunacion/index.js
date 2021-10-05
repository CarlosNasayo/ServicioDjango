var PATH_URL="http://127.0.0.1:8000/api/"
var TOKEN= "";
// Ejemplo implementando el metodo POST:
async function postData(url = '', data = {}) {
    // Opciones por defecto estan marcadas con un *
    const response = await fetch(url, {
      method: 'POST', // *GET, POST, PUT, DELETE, etc.
      //mode: 'no-cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      headers: {
        'Content-Type': 'application/json'
        // 'Content-Type': 'application/x-www-form-urlencoded',
      },
      redirect: 'follow', // manual, *follow, error
      referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
      body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    return response.json(); // parses JSON response into native JavaScript objects
  }
  function login(){
    let username=document.getElementById("username").value
    let password=document.getElementById("password").value
    data={username:username,password:password}
    postData(PATH_URL+'token', data)
    .then(data => {
      console.log(data);
      TOKEN= data.token;
    });
  }
function imprimirDatos(datos){
  //console.log(datos)
  let personas= datos.map((p) =>"<li>"+p.nombre+"</li>")
  document.getElementById("datos").innerHTML=personas;
}
function getPersonas(){
  if (TOKEN==""){
    alert("por favor ingrese las credenciales del usuario")

  }
  {
    let headers= {
      'Content-Type': 'application/json',
      'Authorization': 'token '+TOKEN
    }
    console.log(headers);
    fetch(PATH_URL+'personas',{
      method: 'GET', // *GET, POST, PUT, DELETE, etc.
      headers: headers})
    .then(response => response.json())
    .then(data => imprimirDatos(data));
  }
 
}