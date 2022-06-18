from django.db import models
from django.contrib.auth.models import User



# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,primary_key=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile_pics/', null=True)
    bio = models.TextField()
    email=models.EmailField(null=True)
    

    def __str__(self):
        return self.user.username


    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(self):
        
        self.update()

class N_Hood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupants = models.IntegerField()
    

    def __str__(self):
        return self.name

    def save_hood(self):
        self.save()

    def delete_hood(self):
        self.delete()

    def update_hood(self):
        self.update()

    def create_hood(self):
        self.create()

    def update_occupants(self): 
        self.occupants += 1
        self.save()

    

    def __str__(self):
        return self.name


class Business(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def __str__(self):
        return self.name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()

    def search_business(self):
        return Business.objects.filter(name__icontains=self.name)


class User_Business(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business = models.ForeignKey(Business, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def save_user_business(self):
        self.save()

    def delete_user_business(self):
        self.delete()

    def update_user_business(self):
        self.update()

    