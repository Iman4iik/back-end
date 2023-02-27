from django.db import models


class Blog(models.Model):
    owner = models.CharField(max_length=255, null=False)
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, unique=True, null=False)

    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    def __str__(self):
        return 'ID: {}, Name: {}'.format(self.id, self.name)