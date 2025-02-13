from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,GradeLevel,Subject
from django import forms
from django.contrib.auth.forms import UserChangeForm

# for admin register form
class AdminCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','user_image' ,'email', 'date_of_birth']
        labels = {'email':'Email'}
        error_messages = {
            'username': {'required':'Please Tapaiko Naam Lekhnuhos.'}
        }
        widgets = {'date_of_birth': forms.DateInput(attrs={'placeholder':'YYYY-MM-DD'})}
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].label_suffix = ' '
        self.fields['password2'].label = 'Confirm Password'

# for student register form
class StudentCreateForm(AdminCreateForm):
    student_class = forms.ModelChoiceField(queryset=GradeLevel.objects.all(), required=True)
    student_roll = forms.IntegerField(required=True)
    class Meta(AdminCreateForm.Meta):
        fields = ['username','user_image' ,'email', 'date_of_birth', 'student_class', 'student_roll']

# for teacher register form
class TeacherCreateForm(AdminCreateForm):
    assigned_classes = forms.ModelMultipleChoiceField(queryset=GradeLevel.objects.all(), required=True)
    subjects_taught = forms.ModelMultipleChoiceField(queryset=Subject.objects.all(), required=True)
    class Meta(AdminCreateForm.Meta):
        fields = ['username','user_image' ,'email', 'date_of_birth', 'assigned_classes', 'subjects_taught']
    
# for editing user info form
class UserEditFrom(UserChangeForm):
    password = None
    class Meta:
        model = CustomUser
        fields = ['username', 'user_image', 'first_name', 'last_name', 'email', 'date_of_birth']