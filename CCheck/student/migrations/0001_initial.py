# Generated by Django 2.1.7 on 2019-03-28 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('teacher', '0003_assignment_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='AssignmentDone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='')),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='teacher.Assignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]