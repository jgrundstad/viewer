from django.contrib.admin.widgets import AdminFileWidget
from django import forms
from models import Bnid, Sample, Caller, Report, Study
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']


class BnidForm(forms.ModelForm):
    class Meta:
        model = Bnid
        fields = ['sample', 'bnid', 'description']
        widgets = {'description': forms.Textarea(attrs={'cols': 30,
                                                        'rows': 4}),}


class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ['study', 'name', 'description', 'cellularity']
        widgets = {'description': forms.Textarea(attrs={'cols': 30,
                                                        'rows': 4}),}


class CallerForm(forms.ModelForm):
    class Meta:
        model = Caller
        fields = ['name']


class ReportForm(forms.ModelForm):
    report_file = forms.FileField(widget=AdminFileWidget, required=False)

    class Meta:
        model = Report
        fields = ['study', 'bnids', 'caller', 'report_file']


class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ['name', 'description']
        widgets = {'description': forms.Textarea(attrs={'cols': 30,
                                                        'rows': 4}),}

class StudySelectorForm(forms.Form):

    study = forms.ModelChoiceField(
        queryset=Study.objects.all(),
        widget=forms.Select(attrs={'class': 'study_name'}),
    )

    class Meta:
        fields = ['study']
        widgets = {'study': forms.Select()}

