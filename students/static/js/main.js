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

function initGroupSelector() {
    // look uo select element with groups and attach our even handler
    // on field "change" event
    $('#groupe-selector select').change(function(event){
        // get value of currently selected group option
        var group = $(this).val();

        if (group) {
            // set cookie with expiration date 1 year since now;
            // cookie creation function takes period in days
            Cookies.set('current_group', group, {path: '/', expires: 365});
        } else {
            // otherwise we delete the cookie
            Cookies.remove('current_group', {'path': '/'});
        }

        // and reload a page
        location.reload(true);

        return true;
    });
}

$(document).ready(function(){
    initJournal();
    initGroupSelector();
});