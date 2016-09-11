from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    bio = models.TextField(default='user biography', max_length=100, blank=True)
    avatar = models.FileField(default='static/placeholder.jpg', blank=True)
    location = models.CharField(default='City', max_length=50)

    def __unicode__(self):
        return self.user.username


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

