# Generated by Django 5.1.4 on 2024-12-27 09:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='assigned_classes',
            field=models.ManyToManyField(blank=True, null=True, related_name='customuser_classes', to='users.gradelevel'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='student_class',
            field=models.ForeignKey(blank=True, limit_choices_to={'role': 'student'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userstudent_class', to='users.gradelevel'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='subjects_taught',
            field=models.ManyToManyField(blank=True, null=True, related_name='customuser_subjects', to='users.subject'),
        ),
    ]
