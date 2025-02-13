from django.db import models
from users.models import CustomUser

# Create your models here.
class Attendance(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='user_attendance', limit_choices_to={'role':'student'})
    todaydate = models.DateTimeField()
    is_present = models.BooleanField(default=False)
    taken_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, limit_choices_to={'is_staff':True})
    student_grade_level = models.IntegerField()
    def __str__(self):
        return self.user.username