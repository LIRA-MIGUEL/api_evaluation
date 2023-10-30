function getAll() {
    var request = new XMLHttpRequest();
    request.open('GET', 'http://127.0.0.1:8000/contactos');
    request.send();

    request.onload = function () {
        if (request.status === 200) {
            const response = request.responseText;
            const contactos = JSON.parse(response);
            
            const tbody_contactos = document.getElementById('tbody_contactos');
            tbody_contactos.innerHTML = ''; // Borra cualquier contenido previo en la tabla

            contactos.forEach(function(contacto) {
                var tr = document.createElement('tr');
                var td_email = document.createElement('td');
                var td_nombre = document.createElement('td');
                var td_telefono = document.createElement('td');

                td_email.innerHTML = contacto.email;
                td_nombre.innerHTML = contacto.nombre;
                td_telefono.innerHTML = contacto.telefono;

                tr.appendChild(td_email);
                tr.appendChild(td_nombre);
                tr.appendChild(td_telefono);

                tbody_contactos.appendChild(tr);
            });
        } else {
            console.log('Error al realizar la solicitud. Código de estado: ' + request.status);
        }
    };
}

