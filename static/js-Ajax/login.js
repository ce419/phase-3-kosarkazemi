/**
 * Created by khosh on 5/7/2017 AD.
 */
$(document).ready(function() {
    $('#login').click(function() {
        var user = $('#username').val();
        var pass = $('#pass').val();
        $.post('/login/', {'username': user, 'password': pass}, function (data) {
            if(data.status === -1) {
                // error
                $('#body').find('.row .column .ui.error.message').parent().parent().remove();

                $('#regForm').addClass('error');

                var row = document.createElement('div');
                $(row).addClass('row');

                var col = document.createElement('div');
                $(col).addClass('column');
                $(row).append(col);

                var msg = document.createElement('div');
                $(col).append(msg);
                $(msg).addClass('ui error message');
                $(msg).html(data.message);

                $('#body').prepend(row);
            }
            else {
                // success
                Cookies.set('myToken', data.token);
                // document.location = 'google.com';

                $.get({
                url: '/blog_id/',
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('myToken', Cookies.get('myToken'));
                },
                success: function (data) {
                    window.location.href= '/blog/'.concat(data.blog_id.toString()).concat('/')
                }
                });

            }
        });
    });
});