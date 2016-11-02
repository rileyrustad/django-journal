from django.contrib import admin

from .models import Journal, Question, Goal, GoalCategory, Event

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



admin.site.register(Event)
admin.site.register(GoalCategory, GoalCategoryAdmin)
admin.site.register(Journal, JournalAdmin)
