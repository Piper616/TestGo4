$(document).on('click','#btn-validar', () => {
    let rut = $('#txt-rut').val();
    console.log(rut);
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