function initJournal() {
    var indicator = $('#ajax-progress-indicator');

    $('.day-box input[type="checkbox"]').click(function(event){
        var box = $(this);
        $.ajax(box.data('url'), {
            'type': 'POST',
            'async': true,
            'dataType': 'json',
            'data': {
                'pk': box.data('student-id'),
                'date': box.data('date'),
                'present': box.is(':checked') ? '1' : '',
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            'beforeSend': function(){
                indicator.empty()
                         .append( 'Йде збереження... ' )
                         .show();
            },
            'error': function(xhr, status, error){
                indicator.empty()
                         .removeClass('alert-warning')
                         .addClass('alert-danger')
                         .append( 'Виникла наступна помилка: ' + error );
            },
            'success': function(data, status, xhr){
                indicator.delay( 5800 ).empty().hide();
            }
        });
    });
}

$(document).ready(function(){
    initJournal();
})