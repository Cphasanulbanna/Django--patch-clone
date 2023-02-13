from distutils.command.upload import upload
from django.db import models


FAQ_TYPE = (
    ("rent_tracking","Rent Tracking"),
    ("new_deposit","New Deposit"),
    ("existing_deposit","Existing Deposit"),
)


class Testimonial(models.Model):
    name = models.CharField(max_length=255,default="Benna(default)")
    designation = models.CharField(max_length=255)
    image = models.ImageField(upload_to="testimonilas/")
    description = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name


class Promoter(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="promoters/")

    def __str__(self):
        return self.name


class Faq(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    faq_type = models.CharField(max_length=128,choices=FAQ_TYPE)

    def __str__(self):
        return self.title


class Subscribe(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
