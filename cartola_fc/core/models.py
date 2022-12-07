from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Player(models.Model):
    name = models.CharField(verbose_name="nome", max_length=150)
    initial_price = models.DecimalField(verbose_name="preço inicial", max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal('0.00'))])

    class Meta:
        verbose_name = 'jogador'
        verbose_name_plural = 'jogadores'

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(verbose_name="nome", max_length=150)

    class Meta:
        verbose_name = 'time'
        verbose_name_plural = 'times'

    def __str__(self):
        return self.name


class Match(models.Model):
    match_date = models.DateTimeField()
    team_a = models.ForeignKey('Team', verbose_name='time A', on_delete=models.PROTECT, related_name="team_a_matches")
    team_a_goal = models.PositiveSmallIntegerField(verbose_name='gol(s) do time A', default=0)
    team_b = models.ForeignKey('Team', verbose_name='time B', on_delete=models.PROTECT, related_name="team_b_matches")
    team_b_goal = models.PositiveSmallIntegerField(verbose_name='gol(s) do time B', default=0)

    class Meta:
        verbose_name = 'partida'
        verbose_name_plural = 'partida'

    def __str__(self):
        return f'{self.team_a} x {self.team_b}'

    def times(self):
        return [self.team_a, self.team_b]


class Action(models.Model):
    player = models.ForeignKey('Player', verbose_name='jogador', on_delete=models.PROTECT, related_name='actions')
    team = models.ForeignKey('Team', verbose_name='time', on_delete=models.PROTECT, related_name="actions")
    minutes = models.PositiveSmallIntegerField(verbose_name='minutos')
    match = models.ForeignKey('Match', verbose_name='partida', on_delete=models.PROTECT, related_name='actions')

    class Actions(models.TextChoices):
        GOAL = 'GOAL', 'Goal'
        ASSIST = 'ASSIST', 'Assist'
        YELLOW_CARD = 'YELLOW_CARD', 'Yellow Card'
        RED_CARD = 'RED_CARD', 'Red Card'

    action = models.CharField(max_length=50, choices=Actions.choices)

    class Meta:
        verbose_name = 'ação'
        verbose_name_plural = 'ações'

    def __str__(self):
        return f"{self.minutes}' - {self.player} - {self.action}"
