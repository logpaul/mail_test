from rest_framework import serializers
import regex

from main.models import *

def is_latin_validator(value):
    result = regex.sub('[^\p{Latin}0-9]', u'', value)
    if result != value:
        raise serializers.ValidationError('This field must only consist latin characters and numbers.')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username','id')

    def validate_username(self, value):
        is_latin_validator(value)
        return value


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    def validate_tags(self, value):
        is_latin_validator(value)
        return value

    class Meta:
        model = Article
        fields = ('user_creator', 'blocked_users', 'title', 'text', 'date_add', 'tags')

        user = models.ForeignKey(User)
        article = models.ForeignKey(Article)
        text = models.TextField(default='')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    def validate_user(self, value):
        print(value)
        return value

    class Meta:
        model = Comment
        fields = ('user', 'article', 'text', 'date_add')
