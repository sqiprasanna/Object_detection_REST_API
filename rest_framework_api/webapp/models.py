from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.
# class Employees(models.Model):
# 	firstname = models.CharField(max_length = 10)
# 	lastname = models.CharField(max_length = 10)
# 	emp_id = models.AutoField(primary_key  =True)

# 	def __str__(self):
# 		return self.firstname

class UserManager(BaseUserManager):
	use_in_migrations = True

	def _create_user(self,email, password, **extra_fields):
		if not email:
			raise ValueError("Given email must be set")
		email = self.normalize_email(email)
		user = self.model(email = email, **extra_fields)
		user.set_password(password)
		user.save(using= self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault("is_staff",False)
		extra_fields.setdefault("is_superuser", False)
		return self._create_user(email,password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault("is_staff",True)
		extra_fields.setdefault("is_superuser",True)

		if extra_fields.get("is_staff") is not True:
			raise ValueError("SuperUser must have is_staff = True")
		if extra_fields.get("is_superuser") is not True:
			raise ValueError("Superuser must have is_superuser=True.")

		return self._create_user(email,password, **extra_fields)

class User(AbstractUser):
	username = None
	first_name = models.CharField(_("first name"),max_length = 250)
	last_name = models.CharField(_("last name"),max_length=250)
	email = models.EmailField(_("email"), unique = True)

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["first_name","last_name"]

	objects = UserManager()
	def  __str__(self):
		return "%s" %(self.email)

	def save(self, *args, **kwargs):
		if self.email:
			self.email = self.email.lower()
		return super(User, self).save(*args, **kwargs)