from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.core.exceptions import ValidationError

# validations
def validate_gradelevel(value):
    if value<1 or value>12:
        raise ValidationError('please enter number within range of 1 and 12.')

# Add subjects
class Subject(models.Model):
    subject_name = models.CharField(max_length=80)
    def __str__(self):
        return self.subject_name

class GradeLevel(models.Model):
    grade_level = models.IntegerField(validators=[validate_gradelevel])
    def __str__(self):
        return str(self.grade_level)

# users
# class CustomUserManager(UserManager):
#     def create_superuser(self, username, email=None, password=None, **extra_fields):
#             extra_fields.setdefault("is_staff", True)
#             extra_fields.setdefault("is_superuser", True)
#             extra_fields.setdefault("student_class", 0)
#             extra_fields.setdefault("student_roll", 0)

#             if extra_fields.get("is_staff") is not True:
#                 raise ValueError("Superuser must have is_staff=True.")
#             if extra_fields.get("is_superuser") is not True:
#                 raise ValueError("Superuser must have is_superuser=True.")

#             return self._create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser):
    user_image = models.ImageField(upload_to='userImages')
    role = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    user_slug = models.SlugField(blank=True)
    # student attrs
    student_class = models.ForeignKey(GradeLevel, on_delete=models.CASCADE, related_name='userstudent_class', blank=True, null=True)
    student_roll = models.IntegerField(blank=True, null=True)
    # teacher_attrs
    subjects_taught = models.ManyToManyField(Subject, related_name='customuser_subjects', blank=True)
    assigned_classes = models.ManyToManyField(GradeLevel, related_name='customuser_classes', blank=True)
    
    # objects = CustomUserManager()
    
    class Meta:
        verbose_name='User' 