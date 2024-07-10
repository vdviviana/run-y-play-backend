// todo lo que tenga que ver con hablar con la API
// ocurre a traves de la función fechData
function  fetchData(url, method, callback, data = null) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: data ? JSON.stringify(data) : null,  // Si hay datos, los convierte a JSON y los incluye en el cuerpo
    };
// en el caso de POST PUT DELETE, necesito pasarle el 'body', se lo paso como 'options'
    fetch(url, options)
    .then(response => response.json())
    .then(data => {
        // callback se ejecuta cuando .then(data) este disponible
        callback(data);
    })
    .catch(error => console.log("Ocurrió un error! " + error));
}

/* ------------- evento click boton submit de modal ------------ */
/* ------------- agregar nuevo usuario ------------ */
function add_new_user(event) {   
    let data = {
        'nombre_apellido': document.getElementById("nombre_apellido").value,
        'password' : document.getElementById("password").value,
        "primera_conexion":  "2022-06-01",
        "ultima_conexion ":   "2024-06-15",
        'foto_perfil': document.getElementById("foto_perfil").value,
        'perfil': document.getElementById("perfil").value,
        "estado" :  "activo"
    }
    let url = 'http://127.0.0.1:5000/api/users/create/';

    fetchData(url, "POST", () => {}, data);
    alert("Usuario agregado");
    //function  fetchData(url, method, callback, data = null) {
}