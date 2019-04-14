from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _

from .managers import CollabUserManager

# Create your models here.
class CollabUser(AbstractBaseUser, PermissionsMixin):
	name = models.CharField(_('name'), max_length=60)
	email = models.EmailField(_('email'), max_length=60, unique=True)

	is_staff = models.BooleanField(_('staff status'),default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []

	objects = CollabUserManager()

class Space(models.Model):
	url = models.TextField(_('url'))
	code = models.TextField(_('code'), blank=True)
	submission = models.ManyToManyField('Submission', blank=True)
	participants = models.IntegerField(default=0)
	host = models.ForeignKey(CollabUser, related_name='spaces', on_delete=models.DO_NOTHING)

class Submission(models.Model):
	submission_code = models.TextField(_('submission_code'), blank=True)