from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)

class Experience(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    host = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='hosted_experiences')
    participants = models.ManyToManyField(UserProfile, related_name='joined_experiences', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Review(models.Model):
    experience = models.ForeignKey(Experience, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
