$(document).ready(function(){
    var table = $('#filtro').DataTable({
        orderCellsTop: true,
        fixedHeader: true,

        "language": {
            "url": "https://cdn.datatables.net/plug-ins/1.11.3/i18n/es_es.json"
        },

        responsive :"true",
        dom: 'Bfrtilp',
        buttons:[
            {
                extend: 'excelHtml5',
                text: '<i class="fas fa-file-excel"></i>',
                titleAttr: 'Exportar a Excel',
                className: "btn btn-success"
            },
            {
                extend: 'pdfHtml5',
                text: '<i class="fas fa-file-pdf"></i>',
                titleAttr: 'Exportar a PDF',
                className: "btn btn-danger"
            },
            {
                extend: 'print',
                text: '<i class="fas fa-print"></i>',
                titleAttr: 'Imprimir',
                className: "btn btn-info"
            },
        ]
    });

      //Crea una fila en el head de la tabla y la clona
    $('#filtro thead tr').clone(true).appendTo( '#filtro thead' );
    
    $('#filtro thead tr:eq(1) th').each( function (i) {
        var title = $(this).text(); //nombre columna
        $(this).html('<input type="text" placeholder="Buscar por '+title+'" />');
    
        $( 'input', this ).on( 'keyup change', function () {
            if (table.column(i).search() !== this.value ) {
                table
                    .column(i)
                    .search( this.value )
                    .draw();
            }
        } );
    } ); 
} ); 