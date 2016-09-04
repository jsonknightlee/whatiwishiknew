from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, primary_key=True, related_name='profile')
    bio = models.TextField(max_length=100, null=True, blank=True)
    avatar = models.FileField(default='static/placeholder.jpg', null=True, blank=False)

    def __unicode__(self):
        return self.user.username


User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

