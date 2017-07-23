/**
 * Created by khosh on 5/7/2017 AD.
 */
$(document).ready(function() {
    var offset = 0;

    var loc = document.location.href;
    var id = loc.substring(loc.indexOf('id=') + 3);
    var blog_id = loc.substring(loc.indexOf('blog/') + 5);
    console.log(blog_id);

    $(window).on('scroll', function() {
        if($(window).scrollTop() + $(window).height() == $(document).height()) {
            offset += 4;
            $.get({
                url: '/blog/comments',
                data: {'post_id': id, 'count': 4, 'offset': offset},
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('myToken', Cookies.get('myToken'));
                },
                success: function (data) {
                    if(data.status == 0) {
                        // valid post
                        data.comments.forEach(function(comment) {
                            comment.text = comment.text.replace('\n', '<br />');
                            var template = '<div class="comment">\n<div class="content">\n<div class="text">\n#TEXT#\n</div>\n<div class="metadata">\n<span class="date">#DATE#</span>\n</div>\n</div>\n</div><div class="ui divider"></div>';
                            var text = template.replace('#TEXT#', comment.text).replace('#DATE#', getPersianDateString(comment.datetime));
                            $('#comments').append($.parseHTML(text));
                        });
                    }
                }
            });
        }
    });

    $('#home').click(function() {
        document.location = "Blog.html";
    });

    $('#back').click(function() {
        document.location = "Blog-more.P2?id=" + id;
    });

    $.get({
        url: '/blog/comments',
        data: {'post_id': id, 'count': 4, 'offset': offset},
        beforeSend: function(xhr) {
            xhr.setRequestHeader('myToken', Cookies.get('myToken'));
        },
        success: function (data) {
            if(data.status == 0) {
                // valid post
                if(data.comments.length == 0) {
                    $('#comments').html('No comments on this post yet.');
                }
                data.comments.forEach(function(comment) {
                    comment.text = comment.text.replace('\n', '<br />');
                    var template = '<div class="comment">\n<div class="content">\n<div class="text">\n#TEXT#\n</div>\n<div class="metadata">\n<span class="date">#DATE#</span>\n</div>\n</div>\n</div><div class="ui divider"></div>';
                    var text = template.replace('#TEXT#', comment.text).replace('#DATE#', getPersianDateString(comment.datetime));
                    $('#comments').append($.parseHTML(text));
                });
            }
        }
    });

    $('#send').click(function() {
        var text = $('#cmText').val();

        $.post({
            url: '/blog/comment',
            data: {'post_id': id, 'text': text},
            beforeSend: function(xhr) {
                xhr.setRequestHeader('myToken', Cookies.get('myToken'));
            },
            success: function (data) {
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
                    document.location = document.location;
                }
            }
        });
    });
});