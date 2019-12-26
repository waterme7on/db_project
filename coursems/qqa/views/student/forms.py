from django import forms

class CourseSearchForm(forms.Form):
    course_no = forms.CharField(label = "course_no", max_length=12)
    course_name = forms.CharField(label = "course_name", max_length=20)
    teacher_no = forms.CharField(label = "teacher_no", max_length=12)
    teacher_name = forms.CharField(label="teacher_name", max_length=20)
    course_semester =   forms.CharField(label = "course_semester", max_length=15) 
    course_school = forms.CharField(label = "course_school", max_length=20)

