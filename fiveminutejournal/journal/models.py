from django.db import models
from django.utils import timezone
from datetime import timedelta
from django.contrib.auth.models import User


class Journal(models.Model):
    FIRST = 'F'
    LAST = 'L'
    MIDDLE = 'M'
    JOURNAL_TYPE_CHOICES = (
        (FIRST, 'First'),
        (LAST, 'Last'),
        (MIDDLE, 'Middle'),
    )
    journal_type = models.CharField(
        max_length=1,
        choices=JOURNAL_TYPE_CHOICES,
        default=MIDDLE,
    )
    name = models.CharField(max_length=50, default='New')
    user = models.ForeignKey(User)

    def __str__(self):
        return self.name


class Question(models.Model):
    text = models.CharField(max_length=200)
    journal = models.ForeignKey(Journal)
    responses_number = models.IntegerField(default=2)

    def __str__(self):
        return self.text


class GoalCategory(models.Model):
    text = models.CharField(max_length=200)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User)


    def __str__(self):
        return str(self.text)


class Goal(models.Model):
    category = models.ForeignKey(GoalCategory)
    text = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.text)


class Event(models.Model):
    text = models.CharField(max_length=200)
    date = models.DateField()
    user = models.ForeignKey(User)


    def days_left(self):
        return (self.date - timezone.now().date()).days

    def __str__(self):
        return self.text


class Response(models.Model):
    journal_type = models.ForeignKey(Journal)
    date = models.DateField()
    user = models.ForeignKey(User)

    def __str__(self):
        return str(self.date) + ' ' + str(self.journal_type)


class Answer(models.Model):
    class Meta:
        ordering = ['question']
    text = models.CharField(max_length=200)
    question = models.ForeignKey(Question)
    response = models.ForeignKey(Response)

    def __str__(self):
        return self.text


class AdditionalAnswer(models.Model):
    text = models.TextField()
    response = models.ForeignKey(Response)

    def __str__(self):
        return self.text


class JournalSettings(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    goals = models.BooleanField(default=True)
    events = models.BooleanField(default=True)
    user = models.OneToOneField(User)
    #TODO: settings created for new user upon registration, right now, not automatic

    def __str__(self):
        return self.user.username




# class GoalAnswer(models.Model):
#     GREEN = 'G'
#     YELLOW = 'Y'
#     RED = 'R'
#     GOAL_CHOICES = (
#         (GREEN, 'Green'),
#         (YELLOW, 'Yellow'),
#         (RED, 'Red'),
#     )
#     journal_type = models.CharField(
#         max_length=1,
#         choices=GOAL_CHOICES,
#         default=GREEN)
#
#     goal = models.ForeignKey(Goal)
#     response = models.ForeignKey(Response)
