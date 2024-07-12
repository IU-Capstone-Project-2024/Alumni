$(document).ready(function() {
        $('#tags-input').select2({
            tags: true,
            tokenSeparators: [',', ' '], // Разделители для разделения тегов
        });
    });