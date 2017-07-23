$(document).ready(function() {
    var loc = document.location.href;
    var id = loc.substring(loc.indexOf('id=') + 3);
    var blog_id = loc.substring(loc.indexOf('blog/') + 5);
    console.log(blog_id);

    $('#cm').attr('href', 'comments.P2?id=' + id);

    $.get({
                url: '/blog/post',
                data: {'id': id},
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('myToken', Cookies.get('myToken'));
                },
                success: function (data) {
                    if(data.status == 0) {
                        // valid post
                        data.post.text = data.post.text.replace('\n', '<br />');
                        $('.more-title').html(data.post.title);
                        $('.more-text p').html(data.post.text);
                        $('.more-date').html(getPersianDateString(data.post.datetime));
                    }
                    else {
                        $('.more-title').html('Invalid post !');
                        $('.more-text p').html('No text to show.');
                        $('.more-date').html('This always happens. :p');
                    }
                }
    });
});