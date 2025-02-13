# Generated by Django 5.1.4 on 2024-12-27 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_assigned_classes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='assigned_classes',
            field=models.ManyToManyField(blank=True, related_name='customuser_classes', to='users.gradelevel'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='subjects_taught',
            field=models.ManyToManyField(blank=True, related_name='customuser_subjects', to='users.subject'),
        ),
    ]
