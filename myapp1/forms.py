from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TeamSelectionForm(forms.Form):
    home_team = forms.ChoiceField(choices=[], label='Home Team')
    away_team = forms.ChoiceField(choices=[], label='Away Team')

    def __init__(self, *args, **kwargs):
        team_names = kwargs.pop('team_names', None)
        super(TeamSelectionForm, self).__init__(*args, **kwargs)
        if team_names:
            choices = [(team, team) for team in sorted(team_names)]
            self.fields['home_team'].choices = choices
            self.fields['away_team'].choices = choices
