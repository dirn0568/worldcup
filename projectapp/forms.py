from django.forms import ModelForm

from projectapp.models import ProjectCreateModel


class ProjectCreateForm(ModelForm):
    class Meta:
        model = ProjectCreateModel
        fields = ['project_img', 'project_title', 'project_text']