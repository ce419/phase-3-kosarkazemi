from django.db.models.signals import post_save
from django.dispatch import receiver
from author.models import Blog,WordsString
from blog.models import Post


def count_task( sender, instance, **kwargs):  # get blog_id and count all the posts_words
    posts_words = ''
    blog = Blog.objects.get(id=instance.blog_id)
    WS=WordsString()
    post_of_the_blog = Post.objects.filter(blog=blog)
    for post in post_of_the_blog:
        posts_words=WS.updade_by_text(post.text,posts_words)
    return posts_words
