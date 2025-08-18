# tests/admin.py
from django.contrib import admin
from .models import Test, Question, Variant, Answer

class VariantInline(admin.TabularInline):
    model = Variant
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    inlines = [VariantInline]
    list_display = ("text", "test")

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ("title", "time_limit", "is_access")
    list_filter = ("is_access",)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Variant)
admin.site.register(Answer)
