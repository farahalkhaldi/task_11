# Generated by Django 2.0.4 on 2018-04-09 12:38

from django.db import migrations, models

#farah
class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
    ]
