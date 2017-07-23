$(document).ready(function() {
    var offset = 0;
    var loc = document.location.href;
    var blog_id = loc.substring((loc.indexOf('blog/') + 5)).substr(0);
    console.log(blog_id);

    $(window).on('scroll', function() {
        if($(window).scrollTop() + $(window).height() == $(document).height()) {
            offset += 6;
            $.get({
                url: '/blog/'.concat(blog_id.toString().concat('posts')),
                data: {'count': 6, 'offset': offset},
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('myToken', Cookies.get('myToken'));
                },
                success: function (data) {
                    data.posts.forEach(function (post) {
                        var template = '<li class="blog-card">\n<div class="cd-content">\n<div class="cd-title">#TITLE#</div>\n<div class="cd-text">\n<p>\n#SUMMARY#\n</p>\n</div>\n<div class="cd-date blog-date">#DATE#</div>\n<div class="cd-more">\n<a href="' + blog_id + '/Blog-more.html?id=#ID#">\nmore\n</a>\n</div>\n</div>\n</li>';
                        var text = template.replace('#ID#', post.id).replace('#TITLE#', post.title).replace('#SUMMARY#', post.sum).replace('#DATE#', getPersianDateString(post.datetime));
                        $('#blog').append($.parseHTML(text));
                    });
                }
            });
        }
    });

    $.get({
                url: '/blog/'.concat(blog_id.toString().concat('posts')),
                data: {'count': 6, 'offset': offset},
                beforeSend: function(xhr) {
                    xhr.setRequestHeader('myToken', Cookies.get('myToken'));
                },
                success: function (data) {
                    data.posts.forEach(function(post) {
                       var template = '<li class="blog-card">\n<div class="cd-content">\n<div class="cd-title">#TITLE#</div>\n<div class="cd-text">\n<p>\n#SUMMARY#\n</p>\n</div>\n<div class="cd-date blog-date">#DATE#</div>\n<div class="cd-more">\n<a href="' + blog_id + 'Blog-more.html?id=#ID#">\nmore\n</a>\n</div>\n</div>\n</li>';
                       var text = template.replace('#ID#', post.id).replace('#TITLE#', post.title).replace('#SUMMARY#', post.sum).replace('#DATE#', getPersianDateString(post.datetime));
                       $('#blog').append($.parseHTML(text));
                    });
                }
    });
});