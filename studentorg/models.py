from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class College(BaseModel):
    college_name = models.CharField(max_length=150)

    def __str__(self):
        return self.college_name

class Program(BaseModel):
    prog_name = models.CharField(max_length=150)
    college = models.ForeignKey(College, on_delete=models.CASCADE)

    def __str__(self):
        return self.prog_name
    
class Organization(BaseModel):
    name = models.CharField(max_length=250)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(BaseModel):
    student_id = models.CharField(max_length=15, unique=True)
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class OrgMember(BaseModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_joined = models.DateField()