from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
	class Types(models.TextChoices):
		DEPARTMENT_HEAD = "HEAD", "Head"
		SECRETARY = "SECRETARY", "Secretary"

	base_type = Types.SECRETARY
	type = models.CharField(_("Type"), max_length=50, choices=Types.choices)



	def get_absolute_url(self):
		return reverse("users:detail", kwargs={"username": self.username})


	def save(self, *args, **kwargs):
		if not self.id:
			self.type = self.base_type
		return super().save(*args, **kwargs)



class DepartmentManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type=User.Types.DEPARTMENT_HEAD)

class SecretaryManager(models.Manager):
	def get_queryset(self, *args, **kwargs):
		return super().get_queryset(*args, **kwargs).filter(type=User.Types.SECRETARY)


class DepartmentHeadMore(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)



class DepartmentHead(User):
	base_type = User.Types.DEPARTMENT_HEAD
	objects = DepartmentManager

	class Meta:
		proxy = True



class SecretaryMore(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)


class Secretary(User):
	base_type = User.Types.SECRETARY
	objects = SecretaryManager

	# @property
	# def more(self):
	# 	return self.secretarymore
	

	class Meta:
		proxy = True

