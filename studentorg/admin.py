from django.contrib import admin
from .models import College, Program, Organization, Student, OrgMember

@admin.register(College)
class CollegeAdmin(admin.ModelAdmin):
    list_display = ('college_name', 'created_at', 'updated_at') # Task A [cite: 1718]
    search_fields = ('college_name',) # Task A [cite: 1721]
    list_filter = ('created_at',) # Task A [cite: 1721]

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ('prog_name', 'college') # Task B [cite: 1726]
    search_fields = ('prog_name', 'college__college_name') # Task B [cite: 1728]
    list_filter = ('college',) # Task B [cite: 1730]

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'college', 'description') # Task C [cite: 1736]
    search_fields = ('name', 'description') # Task C [cite: 1738]
    list_filter = ('college',) # Task C [cite: 1740]

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("student_id", "lastname", "firstname", "middlename", "program") # [cite: 1543, 1544]
    search_fields = ("lastname", "firstname") # [cite: 1545]

@admin.register(OrgMember)
class OrgMemberAdmin(admin.ModelAdmin):
    list_display = ("student", "get_member_program", "organization", "date_joined") # [cite: 1548]
    search_fields = ("student__lastname", "student__firstname") # [cite: 1549, 1554]

    def get_member_program(self, obj): # [cite: 1550]
        try:
            return obj.student.program # [cite: 1551]
        except Student.DoesNotExist:
            return None # [cite: 1553]