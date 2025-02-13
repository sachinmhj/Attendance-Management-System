from django.core.management.base import BaseCommand
from users.models import CustomUser 
from attendance.factories import AttendanceFactory  # Import the factory

class Command(BaseCommand):
    help = 'Creates attendance records for all users with role "student"'

    def handle(self, *args, **kwargs):
        # Fetch all users with the role 'student'
        students = CustomUser.objects.filter(role="student")

        if not students.exists():
            self.stdout.write("No students found in the database.")
            return

        # Iterate through all the students and create attendance records
        for student in students:
            # You can create attendance records or any other data as needed
            AttendanceFactory.create(user=student)
        
        # Confirm the completion
        self.stdout.write(f"Created attendance records for {students.count()} students.")
