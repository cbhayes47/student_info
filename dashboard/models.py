from django.db import models


class Course(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=30)
    course_section_code = models.IntegerField()
    course_department = models.CharField(max_length=30)
    instructor = models.CharField(max_length=30)


class Student(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    major = models.CharField(max_length=30)
    year = models.CharField(max_length=30)
    gpa = models.FloatField()
    course1 = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        null=True,
        related_name='student_course1',
    )
    course2 = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        null=True,
        related_name='student_course2',
    )
    course3 = models.ForeignKey(
        Course,
        on_delete=models.PROTECT,
        null=True,
        related_name='student_course3',
    )
