// formulario.js
$(document).ready(function() {
    // Carga las regiones cuando la página se carga
    $.getJSON('/api/regiones/', function(data) {
        data.forEach(function(region) {
            $('#regiones').append('<option value="' + region.id + '">' + region.nombre + '</option>');
        });
    });

    // Cuando se selecciona una región, carga las provincias para esa región
    $('#regiones').change(function() {
        var regionId = $(this).val();
        $.getJSON('/api/provincias/?region=' + regionId, function(data) {
            $('#provincias').empty();
            data.forEach(function(provincia) {
                $('#provincias').append('<option value="' + provincia.id + '">' + provincia.nombre + '</option>');
            });
        });
    });

    // Cuando se selecciona una provincia, carga las comunas para esa provincia
    $('#provincias').change(function() {
        var provinciaId = $(this).val();
        $.getJSON('/api/comunas/?provincia=' + provinciaId, function(data) {
            $('#comunas').empty();
            data.forEach(function(comuna) {
                $('#comunas').append('<option value="' + comuna.id + '">' + comuna.nombre + '</option>');
            });
        });
    });
});