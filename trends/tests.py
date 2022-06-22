from django.test import TestCase

from trends.views import n_hood

from .models import *

# Create your tests here.
class N_HoodTestClass(TestCase):
    # set up method
    def setUp(self):
        self.n_hood = N_Hood(name = 'N-hood', email='moringa214@gmail.com')

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.n_hood, N_Hood))

    # Testing Save Method
    def test_save_method(self):
        self.n_hood.save_n_hood()
        n_hood = N_Hood.objects.all()
        self.assertTrue(len(n_hood) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.n_hood.delete_n_hood()
        n_hood = N_Hood.objects.all()
        self.assertTrue(len(n_hood) == 0)

    # Testing Update Method
    def test_update_method(self):
        self.n_hood.update_n_hood()
        n_hood = N_Hood.objects.all()
        self.assertTrue(len(n_hood) > 0)

    def test_create_hood_method(self):
        self.n_hood.create_hood()
        n_hood = N_Hood.objects.all()
        self.assertTrue(len(n_hood) > 0)

    def test_update_occupants_method(self):
        self.n_hood.update_occupants()
        n_hood = N_Hood.objects.all()
        self.assertTrue(len(n_hood) > 0)
    

    

class ProfileTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.profile = Profile(name = 'N_Hood', email = 'moringa214@gmail.com')
        self.profile.save()

    # Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.profile.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.profile.delete_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) == 0)

    # Testing Update Method
    def test_update_method(self):
        self.profile.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

        




    


