from django.db import models
from django.utils import timezone


class Morning(models.Model):
    date = models.DateField(default=timezone.now)
    grateful1 = models.CharField('I am grateful for...', max_length=200)
    grateful2 = models.CharField('I am grateful for...', max_length=200)
    grateful3 = models.CharField('I am grateful for...', max_length=200)
    great1 = models.CharField('What would make today great?', max_length=200)
    great2 = models.CharField('What would make today great?', max_length=200)
    great3 = models.CharField('What would make today great?', max_length=200)
    affirm1 = models.CharField('Daily Affirmations, I am...', max_length=200)
    affirm2 = models.CharField('Daily Affirmations, I am...', max_length=200)
    more = models.TextField('Additional Reflection', default='')

    def __str__(self):
        return str(self.date)


class Evening(models.Model):
    date = models.DateField(default=timezone.now)
    amazing1 = models.CharField('3 Amazing things that happened today are...', max_length=200)
    amazing2 = models.CharField('3 Amazing things that happened today are...', max_length=200)
    amazing3 = models.CharField('3 Amazing things that happened today are...', max_length=200)
    better1 = models.CharField('How could I have made today better?', max_length=200)
    better2 = models.CharField('How could I have made today better?', max_length=200)
    more = models.TextField('Additional Reflection', default='')
    def __str__(self):
        return str(self.date)