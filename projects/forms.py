from django.forms import ModelForm, inlineformset_factory

from .models import Position, UserProject


class ProjectForm(ModelForm):
    class Meta:
        model = UserProject

        fields = ['title', 'description', 'timeline', 'requirements']
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
    extra=1, can_delete=True
    )
