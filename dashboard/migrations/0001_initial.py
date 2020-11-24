# Generated by Django 3.1.3 on 2020-11-24 16:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('course_section_code', models.IntegerField()),
                ('course_department', models.CharField(max_length=30)),
                ('instructor', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('major', models.CharField(max_length=30)),
                ('year', models.CharField(max_length=30)),
                ('gpa', models.FloatField()),
                ('course1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='student_course1', to='dashboard.course')),
                ('course2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='student_course2', to='dashboard.course')),
                ('course3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='student_course3', to='dashboard.course')),
            ],
        ),
    ]