# Generated by Django 5.0.6 on 2024-07-11 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schools", "0002_alter_schools_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="SchoolTenant",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RenameModel(
            old_name="Schools",
            new_name="School",
        ),
    ]