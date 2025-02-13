import factory
from faker import Faker
from factory import LazyAttribute
import random
import uuid
from datetime import datetime, timedelta
from django.utils.text import slugify
from django.utils import timezone
from users.models import CustomUser, Subject, GradeLevel
from .models import Attendance

fake = Faker('en_US')

# ___________ for creating random user ___________
class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = CustomUser
    username = username = LazyAttribute(lambda _: fake.name())
    first_name = factory.LazyAttribute(lambda _: fake.first_name())
    last_name = factory.LazyAttribute(lambda _: fake.last_name())
    email = factory.LazyAttribute(lambda _: fake.email())
    user_image = LazyAttribute(lambda x: '/userimages/6c1e85d96b6c37916773934e8a433360_5zNH5uh.jpg_300x0q75.webp')
    role = LazyAttribute(lambda x: random.choice(['student', 'admin', 'teacher']))
    date_of_birth = factory.Faker('date_of_birth', minimum_age=20, maximum_age=60)
    user_slug = LazyAttribute(lambda obj: slugify(f'{uuid.uuid4()}'))
    student_class = factory.LazyAttribute(
        lambda _: random.choice(GradeLevel.objects.all()) 
    )
    student_roll = factory.Faker('random_int', min=1, max=1000)
    subjects_taught = factory.LazyAttribute(
        lambda obj: random.sample(list(Subject.objects.all()), random.randint(1, 5))
    )
    assigned_classes = factory.LazyAttribute(
        lambda obj: random.sample(list(GradeLevel.objects.all()), random.randint(1, 3))
    )
    @factory.post_generation
    def subjects_taught(self, create, extracted, **kwargs):
        if extracted:
            self.subjects_taught.set(extracted)
        else:
            random_subjects = random.sample(list(Subject.objects.all()), random.randint(1, 5))
            self.subjects_taught.set(random_subjects)

    @factory.post_generation
    def assigned_classes(self, create, extracted, **kwargs):
        if extracted:
            self.assigned_classes.set(extracted)
        else:
            random_classes = random.sample(list(GradeLevel.objects.all()), random.randint(1, 3))
            self.assigned_classes.set(random_classes)



# ___________ for creating random attendance ___________
# Specific start and end dates for generating random dates
START_DATE = datetime(2023, 1, 1)  # Start date
END_DATE = datetime(2023, 12, 31)  # End date

# Function to generate a random date between the start and end dates
def random_date_between(start_date, end_date):
    delta = end_date - start_date
    random_days = random.randint(0, delta.days)
    random_date = start_date + timedelta(days=random_days)
    # Make the generated date timezone-aware
    return timezone.make_aware(random_date, timezone.get_current_timezone())

randomdate = random_date_between(START_DATE, END_DATE)

class AttendanceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Attendance

    # Only create attendance for users whose role is 'student'
    user = factory.SubFactory(
        UserFactory,
        # Ensure we only pick a user whose role is 'student'
        _create=False  # Prevent creating a new user here, we'll filter them later
    )
    
    todaydate = randomdate
    is_present = factory.Faker('boolean')  # Random boolean value (True or False)
    taken_by = factory.LazyAttribute(lambda _: random.randint(1, 10))  # Random number for 'taken_by'
    
    # Set grade level, ensuring we only assign the grade level if the user has a student class
    student_grade_level = factory.LazyAttribute(
        lambda obj: obj.user.student_class.grade_level if obj.user.student_class else random.randint(1, 12)
    )

    @factory.lazy_attribute
    def user(self):
        # Fetch a random student (role='student')
        return CustomUser.objects.filter(role="student").order_by("?").first()