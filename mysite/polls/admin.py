from django.contrib import admin

from .models import Question, Choice


# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):  # 更优雅地显示选项
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    list_filter = ['pub_date']   # 右侧的过滤列表
    search_fields = ['question_text']  # 搜索框
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]  # 在创建问题时就添加几个选项
    list_display = ('question_text', 'pub_date', 'was_published_recently')  # 在模型首页显示更详细关于模型的信息


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
