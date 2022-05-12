# Generated by Django 4.0.4 on 2022-05-12 14:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_profesor_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiantes',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=254),
            preserve_default=False,
        ),
    ]