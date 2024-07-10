// botones de tabla filtro de usuarios
let filterButtons = {
    "todos": document.querySelector("#VerTodos"),
    "activos": document.querySelector("#VerActivos"),
    "eliminados": document.querySelector("#VerEliminados"),
    "buscar": document.querySelector("#VerById")
}

//
function setActiveFilter(event) {
    // recorro estructura de mi lista de botones
    // y le quito el estado activo a cada boton
    for (filter in filterButtons) {
        filterButtons[filter].classList.remove("active");
    }
    // dejo "active" al boton que estoy haciendo click
    event.currentTarget.classList.add("active");
    // carga vista y pasa como parametro el nombre del boton
    cargaTabla(event.currentTarget.filterName);
}


// agarra cada boton y les pega un evento click
function setFilters() {
    // recorro estructura de mi lista de botones
    for (button in filterButtons) {
        filterButtons[button].addEventListener("click", setActiveFilter);
        // con "filterName" obtengo el nombre del boton y lo guardo 
        filterButtons[button].filterName = button;
    }
}

// llamo a la función 
setFilters();
// cargo la tabla por defecto
cargaTabla("todos");

// recibe nombre del filtro del boton seleccionado
function cargaTabla(filtro_boton) {
    let fetch_data = {
        'todos': {
            'URL': 'http://127.0.0.1:5000/api/users/all/'
        },

        'activos': {
            'URL': 'http://localhost:5000/api/users/activos/'
        },

        'eliminados': {
            'URL': 'http://localhost:5000/api/users/delete/'
        },
        'buscar': {
            'URL': 'http://localhost:5000/api/users/byid/<int:users_id>'
        },
    }

    // validación en caso de no encontrar el tipo de filtro del boton
    if (!(filtro_boton in fetch_data)) {
        throw new Error(`El Parametro: ${filtro_boton} no está definido!`);
    }

    fetchData(fetch_data[filtro_boton].URL, "GET", (data) => {
        let cadenainnerHTML =``;
         cadenainnerHTML = `  <table class="table">
                        <thead>
                            <tr>
                                <th>idusuarios</th>
                                <th>nombre_apellido</th>
                                <th>password</th>
                                <th>primera_conexion</th>
                                <th>ultima_conexion</th>
                                <th>foto_perfil</th>
                                <th>perfil</th>
                                <th>estado</th>
                            </tr>
                        </thead>
                        <tbody>`;
        // Procesamiento de la info que llega de la API
        for (const user of data) {
            cadenainnerHTML += `
                            <tr class="table-primary">
                                <td>${user.idusuarios}</td>
                                <td>${user.nombre_apellido}</td>
                                <td>${user.password}</td>
                                <td>${user.primera_conexion}</td>
                                <td>${user.ultima_conexion}</td>
                                <td>${user.foto_perfil}</td>
                                <td>${user.perfil}</td>
                                <td>${user.estado}</td>
                                </tr> `;
            //

        } // termina for
        cadenainnerHTML +=  `</tbody></table>`;
       // alert(cadenainnerHTML);
        document.getElementById("container-mt-3").innerHTML =cadenainnerHTML ;
    });
}