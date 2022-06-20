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
    n_id = models.AutoField(primary_key=True, null = True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupants = models.IntegerField()
    admin = models.ForeignKey(User, on_delete=models.CASCADE, null= True)
    

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
    n_hood = models.ForeignKey(N_Hood, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField(null=True)
    n_hood=models.ForeignKey(N_Hood,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def create_business(self):
        self.create()

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    def update_business(self):
        self.update()

    def search_business(self):
        return Business.objects.filter(name__icontains=self.name)




class Post(models.Model):
    n_hood = models.ForeignKey(N_Hood, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    post = models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    email=models.EmailField(null=True)
    

    def __str__(self):
        return self.title

    def create_post(self):
        self.create()

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    def update_post(self):
        self.update()

    def search_post(self):
        return Post.objects.filter(title__icontains=self.title)

    