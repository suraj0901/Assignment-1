from django.db import models


# Create your models here.


class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'),
                                                     ("Non IT", 'Non IT'),
                                                     ('Mobiles Phone', "Mobile Phones"
                                                      )))

    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Client(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    project = models.CharField(max_length=200, choices=(('p1', 'p1'),
                                                    ('p2', 'p2'),('p3', 'p3')))

    user = models.ForeignKey(Users, on_delete=models.CASCADE)


class Project(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    adress = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)

    user_assign = models.CharField(max_length=200, choices=(('U1', 'u1'),
                                                    ('u2', 'u'),('u3', 'u3')))

    user = models.ForeignKey(Users, on_delete=models.CASCADE)


