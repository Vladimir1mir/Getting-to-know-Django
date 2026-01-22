from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Theme, ArticleTheme


class ArticleThemeInlineFormset(BaseInlineFormSet):
    def clean(self):
        theme_counter = 0
        for form in self.forms:
            form.cleaned_data
            if form.cleaned_data['main'] == 1:
                theme_counter += 1
        if theme_counter != 1:
            raise ValidationError('Количество главных тегов должно раняться 1')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleThemeInline(admin.TabularInline):
    model = ArticleTheme
    formset = ArticleThemeInlineFormset
    extra = 0


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleThemeInline]


@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    model = Theme
    list_display = ['id', 'theme']
