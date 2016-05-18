from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=250)
    content = models.TextField(max_length=90000)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.author


class Comment(models.Model):
    author = models.CharField(max_length=100)
    content = models.TextField(max_length=90000)
    create_date = models.DateTimeField()
    post = models.ForeignKey(Post)
    parent_comment = models.ForeignKey('self', null=True, blank=True, related_name="children")
    like = models.IntegerField()
    dislike = models.IntegerField()
    quality = models.IntegerField()

    def __str__(self):
        return self.author

    def reload(self):
        new_self = self.__class__.objects.get(pk=self.pk)

    class Meta:
        ordering = ['-quality']