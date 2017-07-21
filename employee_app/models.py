from django.utils import timezone
from mongoengine import *

# Create your models here.
class EmployeeRole(Document):
    name = StringField(max_length=100, unique=True)

    class Meta:
        verbose_name = 'employee_role'
        verbose_name_plural = 'employee_roles'

class EmployeeLog(EmbeddedDocument):
    created_at = DateTimeField(default=timezone.now())
    detail = StringField(verbose_name="Detail")

class Employee(Document):
    username = StringField(max_length=200, unique=True)
    created_at = DateTimeField(default=timezone.now())
    role = ReferenceField('EmployeeRole')
    logs = ListField(EmbeddedDocumentField('EmployeeLog'))

    class Meta:
        verbose_name = 'employee'
        verbose_name_plural = 'employees'
