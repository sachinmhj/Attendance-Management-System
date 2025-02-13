from django.core.management.base import BaseCommand
from attendance.factories import UserFactory

class Command(BaseCommand):
    help = 'Generates random user instances using Faker'

    def handle(self, *args, **kwargs):
        count = int(input('Enter the number of records you want to generate: '))

        # Generate the random users
        users = [UserFactory() for _ in range(count)]

        self.stdout.write(f"Generated {count} random users.")
