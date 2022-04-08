from random import choices
from statistics import mode
from django.db import models
import datetime

# Create your models here.
class Admission(models.Model):
    exam_status_choice =(
    ("1", "Passed"),
    ("2", "Appeared")
    )   

    blood_group_choice = (
        ("O+", "O Positive"),
        ("O-", "O Negative"),
        ("A+", "A Positive"),
        ("A-", "A Negative"),
        ("B+", "B Positive"),
        ("B-", "B Negative"),
        ("AB+", "AB Positive"),
        ("AB-", "AB Negative"),
    )

    sub_caste_choice = (
        ("S", "Shwetamber"),
        ("D", "Digamber")
    )

    formally_admitted_choice = (
        ("Y", "Yes"),
        ("N", "No")
    )

    at_present_working_choice = (
        ("Y", "Yes"),
        ("N", "No")
    )

    history_of_medical_illness_choices = (
        ("Y", "Yes"),
        ("N", "No")
    )

    taking_medicines_choices = (
        ("Y", "Yes"),
        ("N", "No")
    )

    EXAM_YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]

    ADMITTED_YEAR_CHOICES = [(r,r) for r in range(1984, datetime.date.today().year+1)]

    exam_status = models.CharField(choices=exam_status_choice, default='1', max_length=9, db_column='exam_status')
    exam_name = models.CharField(max_length=50, db_column='exam_name')
    exam_year = models.IntegerField(('exam year'), choices=EXAM_YEAR_CHOICES, db_column='exam_year')
    board_name = models.CharField(max_length=50, db_column='board_name')
    student_first_name = models.CharField(max_length=20, db_column='student_first_name')
    student_middle_name = models.CharField(max_length=20, db_column='student_middle_name')
    student_last_name = models.CharField(max_length=20, db_column='student_last_name')
    blood_group = models.CharField(choices=blood_group_choice, max_length=12, db_column='blood_group')
    phone_number = models.CharField(max_length=10, db_column='phone_number')
    email_address = models.EmailField(db_column='email_address')
    caste = models.CharField(max_length=50, db_column='caste')
    sub_caste = models.CharField(choices=sub_caste_choice, max_length=11, db_column='sub_caste')
    birth_date = models.DateField(db_column='birth_date')
    age = models.IntegerField(db_column='age')
    formally_admitted = models.CharField(choices=formally_admitted_choice, max_length=3, db_column='formally_admitted')
    if_admitted = models.IntegerField(('admitted year'), choices=ADMITTED_YEAR_CHOICES, db_column='if_admitted')
    father_first_name = models.CharField(max_length=20, db_column='father_first_name')
    father_middle_name = models.CharField(max_length=20, db_column='father_middle_name')
    father_last_name = models.CharField(max_length=20, db_column='father_last_name')
    father_occupation = models.CharField(max_length=50, db_column='father_occupation')
    college_name = models.CharField(max_length=80, db_column='college_name')
    course_name = models.CharField(max_length=50, db_column='course_name')
    semister = models.IntegerField(db_column='semister')
    last_year_appeared_exam_name = models.CharField(max_length=50, db_column='last_year_appeared_exam_name')
    fill_marks = models.FloatField(db_column='fill_marks')
    other_achievements = models.CharField(max_length=80, db_column='other_achievements')
    at_present_working = models.CharField(choices=at_present_working_choice, max_length=4, db_column='at_present_working')
    company_address = models.TextField(db_column='company_address')
    salary = models.IntegerField(db_column='salary')  
    parent_full_name = models.CharField(max_length=100, db_column='parent_full_name')
    pamanent_address = models.TextField(db_column='pamanent_address')
    permanent_city = models.CharField(max_length=20, db_column='permanent_city')
    pincode = models.CharField(max_length=6, db_column='pincode')
    parent_phone_number = models.CharField(max_length=10, db_column='parent_phone_number')
    parent_telephone_number = models.CharField(max_length=10, db_column='parent_telephone_number')
    parent_email_address = models.EmailField(db_column='parent_email_address')
    guardian_email_address = models.EmailField(db_column='guardian_email_address')
    guardian_first_name = models.CharField(max_length=20, db_column='guardian_first_name')
    guardian_middle_name = models.CharField(max_length=20, db_column='guardian_middle_name')
    guardian_last_name = models.CharField(max_length=20, db_column='guardian_last_name')
    guardian_phone_number = models.CharField(max_length=10, db_column='guardian_phone_number', default='')
    local_address = models.TextField(db_column='local_address')
    local_pincode = models.CharField(max_length=6, db_column='local_pincode')
    guardian_telephone_number = models.CharField(max_length=10, db_column='guardian_telephone_number')
    history_of_medical_illness = models.CharField(choices=history_of_medical_illness_choices ,max_length=3, db_column='history_of_medical_illness')
    taking_medicines = models.CharField(choices=taking_medicines_choices ,max_length=3, db_column='taking_medicines')
    medicine_name = models.CharField(max_length=20, db_column='medicine_name')
    student_photo = models.ImageField(upload_to='images/student_photos/')

    class Meta:
        managed = True
        db_table = 'admission'

    def __str__(self) -> str:
        return str(self.student_first_name) + " " + str(self.student_middle_name) + " " + str(self.student_last_name) 