from django.db import models
from django.utils import timezone
from datetime import timedelta


class Entry(models.Model):
    MORNING = 'M'
    EVENING = 'E'
    ENTRY_TYPE_CHOICES = (
        (MORNING, 'Morning'),
        (EVENING, 'Evening'),
    )
    entry_type = models.CharField(
        max_length=1,
        choices=ENTRY_TYPE_CHOICES,
        default=MORNING)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.date)+' '+str(self.entry_type)


class Question(models.Model):
    text = models.CharField(max_length=200)
    entry = models.ForeignKey(Entry)
    responses_number = models.IntegerField(default=2)


class Response(models.Model):
    text = models.CharField()
    question = models.ForeignKey(Question)


class AdditionalResponse(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question)


class GoalCategory(models.Model):
    text = models.CharField(max_length=200)
    active = models.BooleanField()

    def __str__(self):
        return str(self.text)


class Goal(models.Model):
    category = models.ForeignKey(GoalCategory)
    text = models.CharField(max_length=200)
    start_date = models.DateField(default=timezone.now)
    end_date = models.DateField(default=timezone.now() + timedelta(days=7))

    # TODO: Add logic that makes end_date end of week
    def __str__(self):
        return str(self.text)


class Event(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateField()

    def days_left(self):
        return (self.date - timezone.now().date()).days

    def __str__(self):
        return self.text
