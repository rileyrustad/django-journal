from django.contrib import admin

from .models import AdditionalAnswer, Journal, Question, Goal, GoalCategory, Event, Answer, Response, JournalSettings


# from .models import Entry, EntryResponse, Question, QuestionResponse, Goal, GoalResponse
#
#
# class QuestionInline(admin.StackedInline):
#     model = Question
#     extra = 3
#
#
#
#
# class EntryAdmin(admin.ModelAdmin):
#     inlines = [GoalInline, QuestionInline]
#
#
# class QuestionResponseInline(admin.StackedInline):
#     model = QuestionResponse
#     extra = 3
#
#
# class GoalResponseInline(admin.StackedInline):
#     model = GoalResponse
#     extra = 3
#
#
# class EntryResponseAdmin(admin.ModelAdmin):
#     inlines = [GoalResponseInline, QuestionResponseInline]
#
#
# admin.site.register(Entry, EntryAdmin)
# admin.site.register(EntryResponse, EntryResponseAdmin)

class GoalInline(admin.StackedInline):
    model = Goal
    extra = 1


class GoalCategoryAdmin(admin.ModelAdmin):
    inlines = [GoalInline]


class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2


class JournalAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 0
    ordering = ('question',)


class AdditionalAnswerInline(admin.StackedInline):
    model = AdditionalAnswer
    extra = 0


class ResponseAdmin(admin.ModelAdmin):
    inlines = [AnswerInline, AdditionalAnswerInline]


admin.site.register(Event)
admin.site.register(Answer)
admin.site.register(JournalSettings)
admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(Journal, JournalAdmin)
admin.site.register(Response, ResponseAdmin)
