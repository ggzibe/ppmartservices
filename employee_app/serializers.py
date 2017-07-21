from rest_framework_mongoengine.serializers import DocumentSerializer, EmbeddedDocumentSerializer
from employee_app.models import EmployeeRole, EmployeeLog, Employee

class EmployeeRoleSerializer(DocumentSerializer):
    class Meta:
        model = EmployeeRole
        fields = '__all__'

class EmployeeLogSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = EmployeeLog
        fields = '__all__'

class EmployeeSerializer(DocumentSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

    def update(self, instance, validated_data):
        logs = validated_data.pop('logs')
        updated_instance = super(EmployeeSerializer, self).update(instance, validated_data)

        for log in logs:
            updated_instance.logs.append(EmployeeLog(**log))

        updated_instance.save()
        return updated_instance

class EmployeeReadOnlySerializer(DocumentSerializer):
    role = EmployeeRoleSerializer(many=False, read_only=True)
    logs = EmployeeLogSerializer(many=True)

    class Meta:
        model = Employee
        fields = '__all__'
