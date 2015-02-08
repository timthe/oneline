from django.db import models

class Item(models.Model):
    text = models.TextField()
    user = models.TextField()

    def __str__(self):
        return self.text

# class Item(models.Model):
#     text = models.TextField(default='')
#     user = models.ForeignKey(User, default=None)

#     def __str__(self):
#         return self.text