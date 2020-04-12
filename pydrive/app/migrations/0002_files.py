# Generated by Django 3.0.3 on 2020-03-21 06:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_id', models.IntegerField()),
                ('file_title', models.TextField()),
                ('file_size', models.TextField()),
                ('upload_date', models.DateField()),
                ('file_desc', models.TextField()),
                ('file_link', models.TextField()),
                ('file_starred', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.user')),
            ],
        ),
    ]
