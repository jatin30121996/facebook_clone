from django.db import models

# Create your models here.
class Person(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=50, default="")
    dob = models.DateField(default="")
    school = models.CharField(max_length=200, default="")
    college = models.CharField(max_length=200, default="")
    company = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.first_name + " " + self.last_name


class Loginto(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=20, default="")

    def __str__(self):
        return self.username


class Suggestion(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    suggestion = models.TextField()

    def __str__(self):
        return self.phone


class FriendRequest(models.Model):
    id = models.AutoField(primary_key=True)
    to = models.CharField(max_length=100)
    state = models.BooleanField(default=False)
    frm = models.CharField(max_length=100)

    def __str__(self):
        return self.frm


class Friends(models.Model):
    id = models.AutoField(primary_key=True)
    friend = models.CharField(max_length=100, default="")
    of = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.friend + " of " + self.of


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    textField = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images", default="")

    def __str__(self):
        return self.phone
