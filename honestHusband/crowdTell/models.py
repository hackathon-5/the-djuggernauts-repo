from __future__ import division
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User)
    friend = models.ForeignKey("self")
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Picture(models.Model):
    person = models.ForeignKey(Person)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    upload_time = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('crowdTell:picture_detail', args=(self.id,))

    def __unicode__(self):
        return u'picture by %s' % self.person


class Answer(models.Model):
    person = models.ForeignKey(Person)
    question = models.ForeignKey('Question')
    vote = models.BooleanField()
    comment = models.TextField()

    def get_absolute_url(self):
        return reverse('crowdTell:submit_vote_result', args=(self.question.id,))

    def __unicode__(self):
        return u'%s on %s with %s' % (self.person, self.question, self.vote)


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    picture = models.ForeignKey(Picture)

    @property
    def get_total_votes(self):
        return Answer.objects.filter(question__id=self.id).count()

    @property
    def get_yes_pct(self):
        yes_answers = Answer.objects.filter(question__id=self.id, vote=True).count()
        total_answers = self.get_total_votes

        return round(yes_answers / total_answers * 100, 2)


    @property
    def person(self):
        return self.picture.person

    def __unicode__(self):
        return u'By %s' % self.picture.person