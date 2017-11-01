from django.db import models


class User(models.Model):
    username = models.CharField(max_length=200, default='')

    def __str__(self):
        return self.username


class Article(models.Model):
    user_creator = models.ForeignKey(User, related_name="user_creator")
    blocked_users = models.ManyToManyField(User, blank=True, related_name="blocked_users")
    title = models.CharField(max_length=400, default='')
    text = models.TextField(default='')
    tags = models.TextField(default='')
    date_add = models.DateTimeField('date of addition', auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    text = models.TextField(default='')
    date_add = models.DateTimeField('date of addition', auto_now_add=True)

    def __str__(self):
        return str(self.user) + self.article.title