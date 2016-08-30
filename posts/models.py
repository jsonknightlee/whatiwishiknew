from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.utils import timezone
from django.utils.safestring import mark_safe

import datetime
from django.conf import settings


class Categories(models.Model):
    topics = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.topics


class Post(models.Model):
    user = models.ForeignKey(User, default=1)
    post_title = models.CharField(max_length=250)
    post_body = models.TextField(max_length=10000)
    category = models.ForeignKey(Categories, related_name='hats')
    image = models.FileField(default='', null=True, blank=True)
    email = models.EmailField(default='')
    post_date = models.DateTimeField(default=now)
    upvote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('posts:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.post_title + ' - ' + self.post_body

    def __unicode__(self):
        return self.post_title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    text = models.TextField(max_length=500)
    author_comments = models.ForeignKey(User, related_name='author', default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.text







