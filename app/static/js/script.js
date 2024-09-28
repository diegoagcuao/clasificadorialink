var enlaceId = null;

// Función para abrir el modal y obtener las listas
function openModal(id) {
    enlaceId = id; // Guardar el id del enlace
    // Hacer una solicitud AJAX para obtener las listas del usuario
    $.ajax({
        url: '/obtener_listas', // Ruta para obtener las listas
        method: 'GET',
        success: function(response) {
            // Limpiar el contenido del modal
            $('#lista_id').empty();

            if (response.listas.length > 0) {
                // Si hay listas, llenar el select con las listas obtenidas
                response.listas.forEach(function(lista) {
                    $('#lista_id').append(new Option(lista.nombre, lista.id));
                });
                $('#lista_select_container').show();  // Mostrar el select
                $('#no_listas_message').hide();  // Ocultar el mensaje de "No hay listas"
            } else {
                // Si no hay listas, mostrar un mensaje en el modal
                $('#lista_select_container').hide();  // Ocultar el select
                $('#no_listas_message').show();  // Mostrar el mensaje de "No hay listas"
            }
        },
        error: function(error) {
            console.log(error);
        }
    });
}

// Función para agregar el enlace a la lista seleccionada
function agregarEnlaceALista() {
    var listaId = $('#lista_id').val();

    if (!listaId) {
        alert("Selecciona una lista para agregar el enlace.");
        return;
    }

    // Hacer una solicitud AJAX para agregar el enlace a la lista
    $.ajax({
        url: '/agregar_enlace_a_lista_ajax',
        method: 'POST',
        data: {
            enlace_id: enlaceId,
            lista_id: listaId
        },
        success: function(response) {
            // Cerrar el modal actual y abrir el modal de éxito
            $('#modalAgregarLista').modal('hide');
            $('#modalExito').modal('show');
        },
        error: function(error) {
            console.log(error);
            alert("Hubo un error al agregar el enlace a la lista");
        }
    });
}
