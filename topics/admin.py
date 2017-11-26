from django.contrib import admin

from topics.models import Topic, Course, Comment

admin.site.register(Topic)
admin.site.register(Course)
admin.site.register(Comment)
