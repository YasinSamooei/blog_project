from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    email=models.EmailField()
    content=models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.email)

