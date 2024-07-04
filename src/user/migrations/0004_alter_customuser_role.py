# Generated by Django 5.0.6 on 2024-07-04 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_alter_customuser_name_alter_customuser_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user.role",
            ),
        ),
    ]