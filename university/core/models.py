from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

# ---------------------------------------
# Department
# ---------------------------------------
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    head = models.OneToOneField(
        'Professor',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='headed_department'
    )

    def __str__(self):
        return self.name


# ---------------------------------------
# Professor
# ---------------------------------------
class Professor(models.Model):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='professors'
    )
    hire_date = models.DateField()

    def __str__(self):
        return self.name


# ---------------------------------------
# Student
# ---------------------------------------
class Student(models.Model):
    name = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=12, unique=True)
    dob = models.DateField()
    department = models.ForeignKey(
        Department,
        null=True,
        on_delete=models.SET_NULL,
        related_name='students'
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.enrollment_number})"


# ---------------------------------------
# Course
# ---------------------------------------
class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10, unique=True)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='courses'
    )
    professors = models.ManyToManyField(
        Professor,
        related_name='courses'
    )

    def __str__(self):
        return f"{self.code} - {self.name}"


# ---------------------------------------
# Enrollment (Many-to-Many with extra fields)
# ---------------------------------------
class Enrollment(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='enrollments'
    )
    semester = models.CharField(max_length=6)
    grade = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        unique_together = ('student', 'course', 'semester')
        constraints = [
            models.CheckConstraint(
                check=models.Q(grade__in=['A+', 'A', 'B+', 'B', 'C', 'D', 'F', None]),
                name='valid_grade_values'
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.course} - {self.semester}"


# ---------------------------------------
# Classroom
# ---------------------------------------
class Classroom(models.Model):
    room_number = models.CharField(max_length=10)
    building = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )

    def __str__(self):
        return f"{self.building} - Room {self.room_number}"


# ---------------------------------------
# CourseSchedule
# ---------------------------------------
class CourseSchedule(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='schedules'
    )
    classroom = models.ForeignKey(
        Classroom,
        null=True,
        on_delete=models.SET_NULL,
        related_name='schedules'
    )
    day_of_week = models.CharField(max_length=10)  # e.g. Monday
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ('course', 'day_of_week', 'start_time')

    def __str__(self):
        return f"{self.course.code} on {self.day_of_week} from {self.start_time} to {self.end_time}"


##############################################################################################################################
############ NEW MODEL SET ################################################
##############################################################################################################################

# Restaurent
# User
# Rating

class Restaurent(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'Chinese'
        ITALIAN = 'IT', 'Italian'
        GREEK   = 'GR', 'Greek'
        MEXICAN = 'MX', 'Mexican'
        FASTFOOD = 'FF', 'Fast Food'
        OTHER = 'OT', 'Others'
        
    name = models.CharField(max_length=100)
    website = models.URLField(default='')
    date_opened = models.DateField()
    latitute = models.FloatField()
    longitute = models.FloatField()
    restaurent_type = models.CharField(max_length=2,choices=TypeChoices.choices)
    
    def __str__(self):
        return self.name
    
    
class Rating(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    restaurent = models.ForeignKey(Restaurent,on_delete=models.CASCADE,related_name='ratings') # related_name='ratings'
    rating = models.PositiveBigIntegerField()
    
    class Meta:
        unique_together = ('user', 'restaurent')
    
    def __str__(self):
        return f"Rating: {self.rating}"
    
    
class Sale(models.Model):
    restaurent = models.ForeignKey(Restaurent, on_delete=models.SET_NULL, null=True,related_name='sales')
    income = models.DecimalField(max_digits=9, decimal_places=2)
    datetime = models.DateTimeField()
    