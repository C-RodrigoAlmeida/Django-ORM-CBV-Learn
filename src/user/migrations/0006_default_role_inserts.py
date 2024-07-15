from django.db import migrations


class Migration(migrations.Migration):
    def create_roles(apps, schema_editor):
        Role = apps.get_model('user', 'Role')
        role_list = ['Principal', 'Teacher', 'Student']
        for role in role_list: Role.objects.create(name=role)

    dependencies = [
        ('user', '0005_remove_customuser_name'),        
    ]

    operations = [
        migrations.RunPython(create_roles)
    ]
