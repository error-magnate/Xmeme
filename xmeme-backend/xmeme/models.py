from django.db import models

# Model to store the meme posts
class MemePost(models.Model):
    name = models.CharField(max_length=30)
    url = models.URLField()
    caption = models.TextField()

    def __str__(self):
        return self.name

# Model to store HashTags
class HashTags(models.Model):
    post = models.ForeignKey(MemePost, on_delete=models.CASCADE)
    tags = models.TextField()

    def __str__(self):
        return self.tags
