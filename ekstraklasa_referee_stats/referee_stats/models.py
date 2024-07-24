from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

TYPE_OF_DECISION = (
    ("1",'GOOD_PENALTY'),
    ("2",'BAD_PENALTY'),
    ("3",'MISS_PENALTY'),
    ("4",'GOOD_RED_CARD'),
    ("5",'BAD_RED_CARD'),
    ("6",'MISS_RED_CARD'),
    ("7",'OFFSIDE_GOAL'),
    ("8",'ONSIDE_GOAL'),
    ("9",'OTHER'),
)

TYPE_OF_REFEREE = (
    ("1",'GŁÓWNY'),
    ("2",'ASYSTENT 1'),
    ("3",'ASYSTENT 2'),
    ("4",'TECHNICZNY'),
    ("5",'VAR'),
    ("6",'VAR ASYSTENT'),
)

class Team(models.Model):
    name = models.CharField(max_length=30,verbose_name="Nazwa", unique=True)
   
    def __str__(self):
        return self.name


class Referee(models.Model):
    first_name = models.CharField(max_length=50,verbose_name="Imię")
    last_name = models.CharField(max_length=50,verbose_name="Nazwisko")
    
    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Match(models.Model):
    home_team = models.ForeignKey(Team,verbose_name="Gospodarze",on_delete=models.RESTRICT, related_name="home_team")
    away_team = models.ForeignKey(Team,verbose_name="Goście",on_delete=models.RESTRICT, related_name="away_team")
    date = models.DateField(blank=True, null=True,verbose_name="Data")
    round = models.IntegerField(verbose_name="Kolejka", validators=[MinValueValidator(1), MaxValueValidator(34)])
    home_goals = models.IntegerField(blank=True, null=True,verbose_name="Bramki gospodarze")
    away_goals = models.IntegerField(blank=True, null=True,verbose_name="Bramki goście")
    home_yellow_cards = models.IntegerField(blank=True, null=True,verbose_name="ŻK gospodarze")
    away_yellow_cards = models.IntegerField(blank=True, null=True,verbose_name="ŻK goście")
    home_red_cards = models.IntegerField(blank=True, null=True,verbose_name="CK gospodarze")
    away_red_cards = models.IntegerField(blank=True, null=True,verbose_name="CK goście")
    home_penalty = models.IntegerField(blank=True, null=True,verbose_name="Karne gospodarze")
    away_penalty = models.IntegerField(blank=True, null=True,verbose_name="Karne goście")
    referee_main = models.ForeignKey(Referee, on_delete=models.RESTRICT,verbose_name="Sędzia główny", related_name="referee_main", null=True, blank=True)
    referee_as1 = models.ForeignKey(Referee, on_delete=models.RESTRICT,verbose_name="Sędzia asystent 1", related_name="referee_as1", null=True, blank=True)
    referee_as2 = models.ForeignKey(Referee, on_delete=models.RESTRICT,verbose_name="Sędzia asystent 2", related_name="referee_as2", null=True, blank=True)
    referee_tech = models.ForeignKey(Referee, on_delete=models.RESTRICT,verbose_name="Sędzia techniczny", related_name="referee_tech", null=True, blank=True)
    referee_var = models.ForeignKey(Referee, on_delete=models.RESTRICT,verbose_name="Sędzia VAR", related_name="referee_var", null=True, blank=True)
    referee_vara = models.ForeignKey(Referee, on_delete=models.RESTRICT,verbose_name="Sędzia VAR asystent", related_name="referee_vara", null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.pk:
            update_referee_on_events_by_match(self, Match.objects.get(id=self.pk))
        super().save(*args, **kwargs)  # Call the "real" save() method.
    
    def __str__(self):
        return self.home_team.name + ' - ' + self.away_team.name + ' (' + str(self.round) + ')'

class Event(models.Model):
    match = models.ForeignKey(Match, on_delete=models.RESTRICT,verbose_name="Mecz", related_name="match")
    minute = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(90)])
    additional_minute = models.IntegerField(null=True, blank=True,validators=[MinValueValidator(1)])
    type_of_decision = models.CharField(choices=TYPE_OF_DECISION,verbose_name="Decyzja", max_length=50)
    type_of_referee = models.CharField(choices=TYPE_OF_REFEREE, verbose_name="Rola sędziego", max_length=50)
    referee = models.ForeignKey(Referee, on_delete=models.RESTRICT,verbose_name="Sędzia", related_name="referee", null=True, blank=True)
    link = models.URLField(max_length=200, verbose_name="Link", null=True, blank=True)
    notes = models.TextField(blank=True,null=True,verbose_name="Uwagi")

    def save(self, *args, **kwargs):
        self.referee = get_referee_by_type_and_match(self.type_of_referee,self.match)
        super().save(*args, **kwargs)  # Call the "real" save() method.

    def __str__(self):
        if self.referee:
            return self.referee.first_name + ' '+ self.referee.last_name + ' ' + self.type_of_decision
        else:
            return self.type_of_decision
        
def get_referee_by_type_and_match(type_of_referee, match: Match):
    print(type_of_referee)
    match type_of_referee:
        case "1":
            return match.referee_main
        case "2":
            return match.referee_as1
        case "3":
            return match.referee_as2
        case "4":
            return match.referee_tech
        case "5":
            return match.referee_var
        case "6":
            return match.referee_vara
        case _:
            return None
        
def update_referee_on_events_by_match(new_match: Match, old_match: Match):
    if new_match.referee_main != old_match.referee_main:
        Event.objects.filter(match=new_match, type_of_referee=1).update(referee=new_match.referee_main)
    if new_match.referee_as1 != old_match.referee_as1:
        Event.objects.filter(match=new_match, type_of_referee=2).update(referee=new_match.referee_as1)
    if new_match.referee_as2 != old_match.referee_as2:
        Event.objects.filter(match=new_match, type_of_referee=3).update(referee=new_match.referee_as2)
    if new_match.referee_tech != old_match.referee_tech:
        Event.objects.filter(match=new_match, type_of_referee=4).update(referee=new_match.referee_tech)
    if new_match.referee_var != old_match.referee_var:
        Event.objects.filter(match=new_match, type_of_referee=5).update(referee=new_match.referee_var)
    if new_match.referee_vara != old_match.referee_vara:
        Event.objects.filter(match=new_match, type_of_referee=6).update(referee=new_match.referee_vara)
