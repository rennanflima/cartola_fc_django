
from django.contrib import admin

from .models import Action, Match, Player, Team


# Register your models here.
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'initial_price')


admin.site.register(Team)


class ActionInline(admin.TabularInline):
    model = Action
    extra = 1


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('match_date', '__str__')
    inlines = [ActionInline,]
