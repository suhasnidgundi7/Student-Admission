from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView
from requests import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from admission.models import Admission
import requests
from .serializers import AddmissionSerializer

# Create your views here.

class AddStudent(APIView):
    def get(self, request):
        try:
            request_data = request.data
            student_output = Admission.objects.all()
            student_output = AddmissionSerializer(student_output, many=True).data
            return Response({'Success':True, 'Message': student_output})
        except Exception as err:
            import os, sys
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            return Response({'Success': False, 'Message':str(err)}, status=200)


    def post(self, request):
        try:
            request_data = request.data

            addmissionObj = Admission.objects.create(
                exam_status = request_data.get('exam_status', '1'),
                exam_name = request_data.get('exam_name', ''),
                exam_year = request_data.get('exam_year', 0000-00-00),
                board_name = request_data.get('board_name', ''),
                student_first_name = request_data.get('student_first_name', ''),
                student_middle_name = request_data.get('student_middle_name', ''),
                student_last_name = request_data.get('student_last_name', ''),
                blood_group = request_data.get('blood_group', ''),
                phone_number = request_data.get('phone_number', ''),
                email_address = request_data.get('email_address', ''),
                caste = request_data.get('caste', ''),
                sub_caste = request_data.get('sub_caste', ''),
                birth_date = request_data.get('birth_date', 0000-00-00),
                age = request_data.get('age', 0),
                formally_admitted = request_data.get('formally_admitted', ''),
                if_admitted = request_data.get('if_admitted', ''),
                father_first_name = request_data.get('father_first_name', ''),
                father_middle_name = request_data.get('father_middle_name', ''),
                father_last_name = request_data.get('father_last_name', ''),
                father_occupation = request_data.get('father_occupation', ''),
                college_name = request_data.get('college_name', ''),
                course_name = request_data.get('course_name', ''),
                semister = request_data.get('semister', 0),
                last_year_appeared_exam_name = request_data.get('last_year_appeared_exam_name', ''),
                fill_marks = request_data.get('fill_marks', 0.0),
                other_achievements = request_data.get('other_achievements', ''),
                at_present_working = request_data.get('at_present_working', ''),
                company_address = request_data.get('company_address', ''),
                salary = request_data.get('salary', 0),
                parent_full_name = request_data.get('parent_full_name', ''),
                pamanent_address = request_data.get('pamanent_address', ''),
                permanent_city = request_data.get('permanent_city', ''),
                pincode = request_data.get('pincode', ''),
                parent_phone_number = request_data.get('parent_phone_number', ''),
                parent_telephone_number = request_data.get('parent_telephone_number', ''),
                parent_email_address = request_data.get('parent_email_address', ''),
                guardian_email_address = request_data.get('guardian_email_address', ''),
                guardian_first_name = request_data.get('guardian_first_name', ''),
                guardian_middle_name = request_data.get('guardian_middle_name', ''),
                guardian_last_name = request_data.get('guardian_last_name', ''),
                guardian_phone_number = request_data.get('guardian_phone_number', ''),
                local_address = request_data.get('local_address', ''),
                local_pincode = request_data.get('local_pincode', ''),
                guardian_telephone_number = request_data.get('guardian_telephone_number', ''),
                history_of_medical_illness = request_data.get('history_of_medical_illness', ''),
                taking_medicines = request_data.get('taking_medicines', ''),
                medicine_name = request_data.get('medicine_name', ''),
                student_photo = request_data.get('student_photo', ''),
            )

            message = "Student Added Successfull"
            return Response({'Success': True, 'Message': message}, status=200)
        except Exception as err:
            return Response({'Success': False, 'Message':str(err)}, status=200)