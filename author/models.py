import re
from django.db import models
from django.contrib.auth.models import User
import heapq


class BlogUser(models.Model):
    user = models.ForeignKey(User, blank=True, null=True)
    blog_id = models.IntegerField(default=0)
    token = models.CharField(max_length=20, blank=True, null=True, default=None)




class Blog(models.Model):
    owner = models.ForeignKey(BlogUser, blank=True, null=True)
    posts_words = models.CharField(max_length=1000, blank=True, null=True, default='')
    title = models.CharField(max_length=100, blank=True, null=True, default='NO Title')




class WordsString:

    def make_dict(self,ws): # make dictionary out of ws
        dict={}
        if ws is not '':
            if ws is not None:
                for item in ws.split(','):
                    it = item.split('-')
                    dict[it[0]] = it[1]
        return dict

    def dict_to_ws(self,dict): # make ws out of dictionary
        ws=''
        for key in dict:
            ws=str(key)+'-'+str(dict[key])+','+ws
        ws = ws[:-1]
        return ws


################## SET POSTS_WORDS
    def count_text_to_dict(self,txt): # count a given text words number as a dict
        dict={}
        rx = re.compile('\W+')
        txt = rx.sub(' ', txt).strip()
        for word in txt.split():
            if dict.get(word,0) is 0:
                dict[word] = 1
            else:
                n=int(dict[word])+1
                dict[word] = n
        return dict

    def updade_by_text(self,txt,ws): # add a text words number to a given ws returns new_ws\
        new_dict=self.count_text_to_dict(txt)
        dict=self.make_dict(ws)
        comb_dict=dict
        for key in new_dict:
            if comb_dict.get(key, 0) is 0:
                comb_dict[key] = new_dict[key]
            else:
                n = int(new_dict[key]) + int(comb_dict[key])
                dict[key] = n
        new_ws = self.dict_to_ws(comb_dict)
        return new_ws


################## SEARCH POSTS_WORDS

    def search_blogs(self,searched_words): # search given words in all blogs, rate them and return top ten
        blogs = []
        for blog in Blog.objects.all():
            blogs.append([blog , self.score_blog(blog.posts_words,searched_words)])
        top_blogs = heapq.nlargest( 10 , blogs , key=lambda x:x[1])
        return top_blogs

    def score_blog(self,ws,searched_words): # assigns a score number to given blog
        sp_words = searched_words.split()[::-1]
        score=0
        factor=1
        for word in sp_words:
            n=int(self.count_word(word,ws))
            if n>0:
                factor=factor+0.1 # first word is more important
            score=round(score+n*factor,4)
        return score

    def count_word(self,word,ws): # returns the number of a given word in a ws
        dict=self.make_dict(ws)
        return dict.get(word,0)


