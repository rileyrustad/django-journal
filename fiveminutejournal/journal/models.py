from django.db import models
from django.utils import timezone


class Morning(models.Model):
    date = models.DateField(default=timezone.now)
    grateful1 = models.CharField('I am grateful for...', max_length=100)
    grateful2 = models.CharField('I am grateful for...', max_length=100)
    grateful3 = models.CharField('I am grateful for...', max_length=100)
    great1 = models.CharField('What would make today great?', max_length=100)
    great2 = models.CharField('What would make today great?', max_length=100)
    great3 = models.CharField('What would make today great?', max_length=100)
    affirm1 = models.CharField('Daily Affirmations, I am...', max_length=100)
    affirm2 = models.CharField('Daily Affirmations, I am...', max_length=100)
    more = models.TextField('Additional Reflection', default='')

    def __str__(self):
        return str(self.date)