/**
 * Created by khosh on 5/7/2017 AD.
 */
$(document).ready(function() {
    $('#home').click(function() {
        document.location = 'Blog.html';
    });
    $('#post').click(function() {
        var title = $('#title').val();
        var sum = $('#sum').val();
        var text = $('#text').val();
        var blog_id = loc.substring(loc.indexOf('blog/') + 5);
        console.log(blog_id);

        $.post({
                    url: '/blog/post',
                    data: {
                        'title': title,
                        'summary': sum,
                        'text': text
                    },
                    beforeSend: function(xhr) {
                        xhr.setRequestHeader('myToken', Cookies.get('myToken'));
                    },
                    success: function (data) {
                        console.log(data);
                        if(data.status == -1) {
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
                            document.location = 'Blog.html';
                        }
                    }
        });
    });
});