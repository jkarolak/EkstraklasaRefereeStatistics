from django.contrib import admin
from .models import Event, Match, Referee, Team




class EventAdmin(admin.ModelAdmin):
    list_display = ['match','minute','additional_minute','type_of_decision', 'type_of_referee', 'referee']
    ordering = ['minute', 'additional_minute']
    readonly_fields=('referee',)

    def get_form(self, request, obj=None, **kwargs):
        form = super(EventAdmin, self).get_form(request, obj, **kwargs)
        form.base_fields['match'].initial = Event.objects.latest('id').match
        form.base_fields['minute'].initial = Event.objects.latest('id').minute
        form.base_fields['additional_minute'].initial = Event.objects.latest('id').additional_minute
        return form

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

class RefereeAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name']
    ordering = ['last_name', 'first_name']

class MatchAdmin(admin.ModelAdmin):
    list_display = [
        'home_team',
        'away_team',
        'date',
        'round',
        'home_goals',
        'away_goals',
        'home_yellow_cards',
        'away_yellow_cards',
        'home_red_cards',
        'away_red_cards',
        'home_penalty',
        'away_penalty',
        'referee_main',
        'referee_as1',
        'referee_as2',
        'referee_tech',
        'referee_var',
        'referee_vara'
    ]
    ordering = ['-date', '-round', 'home_team']

admin.site.register(Match, MatchAdmin)
admin.site.register(Referee, RefereeAdmin)
admin.site.register(Team,TeamAdmin)
admin.site.register(Event, EventAdmin)

