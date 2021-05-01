from django.forms import ModelForm, TextInput, Textarea, inlineformset_factory

from .models import Position, UserProject, Applicant


class ProjectForm(ModelForm):
    class Meta:
        model = UserProject

        fields = ['title', 'description', 'timeline', 'requirements']
        widgets = {
            'title':TextInput(attrs={'class':'circle--input--h1',
                                     'placeholder':'Project Title'
                                     }),
            'description':Textarea(attrs={'placeholder':'Project description'}),
            'timeline':Textarea(attrs={'class':'circle--textarea--input',
                                       'placeholder':'Time Estimate'
                                       })
            }
        exclude = ['created_by']


class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = ['title', 'description']

        exclude = ['project']


project_position_formset = inlineformset_factory(
    parent_model=UserProject,
    model=Position,
    form=PositionForm,
    fields=['title', 'description'],
    widgets={
        'title':TextInput(attrs={'class':'circle--input--h3',
                                 'placeholder':'Position Title'
                                 }),
        'description':Textarea(attrs={'placeholder':'Position description'})
        },
    extra=1

    )


class ApplicantForm(ModelForm):
    class Meta:
        model = Applicant
        exclude = ['applicant', 'hired','position']