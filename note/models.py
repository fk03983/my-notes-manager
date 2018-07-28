from django.db import models
from django.utils import timezone

class Note(models.Model):
    author  = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    user = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def saved(self):
        self.save()
    
    def __str__(self):
        return self.text


