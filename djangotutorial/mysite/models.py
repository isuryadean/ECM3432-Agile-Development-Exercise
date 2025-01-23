from django.db import models

class issue(models.Model):
    id = models.IntegerField()
    description = models.TextField()
    stage = models.IntegerField()
    
    def _str_(self):
        return self.title