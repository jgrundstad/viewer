from django.contrib.admin.widgets import AdminFileWidget
from django import forms
from models import Project, Bnid, Sample, Caller, Report, Study, SharedData, Contact
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']

class ProjectForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Project
        fields = ['name', 'description']
        widgets = {'description': forms.Textarea(attrs={'cols': 30,
                                                        'rows': 6,
                                                        'style': 'resize:none'}),}


class BnidForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BnidForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Bnid
        fields = ['sample', 'bnid', 'description']
        widgets = {'description': forms.Textarea(attrs={'cols': 30,
                                                        'rows': 6,
                                                        'style': 'resize:none'}),}


class SampleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SampleForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        # self.fields['study'].queryset = Project.objects.get(pk=kwargs['project_pk']).study_set.all()


    class Meta:
        model = Sample
        fields = ['study', 'name', 'description', 'cellularity']
        widgets = {'description': forms.Textarea(attrs={'cols': 30,
                                                        'rows': 6,
                                                        'style': 'resize:none'}),}


class CallerForm(forms.ModelForm):
    class Meta:
        model = Caller
        fields = ['name']


class ReportForm(forms.ModelForm):
    report_file = forms.FileField(widget=AdminFileWidget, required=False)

    def __init__(self, *args, **kwargs):
        super(ReportForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        self.fields['report_file'].label = 'Report file (must be .csv or .tsv):'
       # self.fields['bnids'] = forms.SelectMultiple()

    class Meta:
        model = Report
        fields = ['name', 'study', 'bnids', 'genome', 'caller', 'report_file']
        widgets = {
            'bnids': forms.SelectMultiple(attrs={
                'size': '10'
            })
        }


class StudyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudyForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = Study
        fields = ['project', 'name', 'description']
        widgets = {'description': forms.Textarea(attrs={'cols': 30,
                                                        'rows': 6,
                                                        'style': 'resize:none'}),
                   'project': forms.HiddenInput()
                  }

class StudySelectorForm(forms.Form):

    study = forms.ModelChoiceField(
        queryset=Study.objects.all(),
        widget=forms.Select(attrs={'class': 'study_name form-control'}),
    )

    class Meta:
        fields = ['study']
        widgets = {'study': forms.Select()}


class SharedDataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SharedDataForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = SharedData
        fields = ['name', 'description', 'inactive_date', 'shared_recipient', 'field_lookup']
        widgets = {
            'field_lookup': forms.HiddenInput(),
            'inactive_date': forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD'})
        }


class ContactForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })
        # self.fields['study'].queryset = Project.objects.get(pk=kwargs['project_pk']).study_set.all()


    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'project']
        widgets = {
            'project': forms.HiddenInput()
        }
