from django.contrib import admin

from .models import Morning, Evening

# from .models import Entry, EntryResponse, Question, QuestionResponse, Goal, GoalResponse
#
#
# class QuestionInline(admin.StackedInline):
#     model = Question
#     extra = 3
#
#
# class GoalInline(admin.StackedInline):
#     model = Goal
#     extra = 3
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

admin.site.register(Morning)
admin.site.register(Evening)
