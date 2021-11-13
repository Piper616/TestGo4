$(document).on('blur','#rut', () => { 
    let rut = $('#rut').val();
    let validarRut = new ValidarRut(rut)

    if(validarRut.validado){
        $('#resultado').html(mensajeAlerta('success', `Rut válido ${validarRut.formato()}`));
        return '';
    }

    $('#resultado').html(mensajeAlerta('danger','Rut Inválido'));
    
})

function mensajeAlerta(tipo, mensaje) {
    return `
        <div class='alert alert-${tipo}'>
            <strong>${mensaje}</strong>
        </div>
    `;    
}