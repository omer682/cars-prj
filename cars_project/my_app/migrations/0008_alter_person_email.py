# Generated by Django 4.2.1 on 2023-06-04 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0007_alter_person_person_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
    ]