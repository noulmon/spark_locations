from django.contrib.gis.db import models
from django.utils.translation import ugettext_lazy as _


class Place(models.Model):
    name = models.CharField(max_length=100)
    # The location of the place where user have checked-in
    location = models.PolygonField()
    city = models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.name)


class User(models.Model):
    username = models.CharField(_('Username'), max_length=30, blank=True, default='')
    first_name = models.CharField(_('First name'), max_length=30, blank=True, default='')
    last_name = models.CharField(_('Last name'), max_length=30, blank=True, default='')
    email = models.EmailField(_('Email'), blank=True, default='')

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)


class UserCheckedInPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='locations')
    place = models.ForeignKey(Place, on_delete=models.PROTECT, related_name='users',
                              help_text=_('The place user checked-in'))
    is_active = models.BooleanField(help_text=_('Checks whether the user is currently in this position'), default=True)
    is_deleted = models.BooleanField(
        help_text=_('True if the user deleted a particular check-in details and will not be shown in user locations'),
        default=False)

    def __str__(self):
        return "{} checked into {}".format(self.user.username, self.place.name)


class UserFollow(models.Model):
    user = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    followed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        # prevents duplication
        unique_together = ("user", "following")

    def __str__(self):
        return "{} follows {}".format(self.user.username, self.following.username)
