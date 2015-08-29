from __future__ import division
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.
class Person(models.Model):
    user = models.ForeignKey(User)
    friends = models.ManyToManyField('self', symmetrical=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    @property
    def picture_questions(self):
        return PictureQuestion.objects.filter(person__id=self.id)

    def get_absolute_url(self):
        return reverse('crowdTell:person_detail', args=(self.id,))

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class PictureQuestion(models.Model):
    person = models.ForeignKey(Person)
    title = models.CharField(max_length=100, verbose_name='Question')
    text = models.TextField(verbose_name='Supplementary Details')
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/')
    upload_time = models.DateTimeField(auto_now_add=True)

    @property
    def get_total_votes(self):
        return Answer.objects.filter(picture_question__id=self.id).count()

    @property
    def get_yes_pct(self):
        yes_answers = Answer.objects.filter(picture_question__id=self.id, vote=True).count()
        total_answers = self.get_total_votes

        if total_answers >= 1:
            return round(yes_answers / total_answers * 100, 2)
        else:
            return 0

    def get_absolute_url(self):
        return reverse('crowdTell:submit_vote_result', args=(self.id,))

    def __unicode__(self):
        return u'picture by %s' % self.person


class Answer(models.Model):
    person = models.ForeignKey(Person)
    picture_question = models.ForeignKey('PictureQuestion')
    vote = models.BooleanField()
    comment = models.TextField()

    def get_absolute_url(self):
        return reverse('crowdTell:submit_vote_result', args=(self.picture_question.id,))

    def __unicode__(self):
        return u'%s on %s with %s' % (self.person, self.question, self.vote)

