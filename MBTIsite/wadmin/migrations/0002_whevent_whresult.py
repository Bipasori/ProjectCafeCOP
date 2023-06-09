# Generated by Django 3.1.4 on 2020-12-18 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wadmin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WHEvent',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('event_id', models.CharField(db_column='event_id', max_length=50)),
                ('user_answer', models.CharField(db_column='user_answer', max_length=255)),
                ('user_note', models.CharField(db_column='user_note', max_length=4096)),
                ('event_result', models.CharField(db_column='event_result', max_length=255)),
                ('level_max', models.IntegerField(db_column='level_max', default=1)),
            ],
            options={
                'db_table': 'wh_event',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WHResult',
            fields=[
                ('id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('result_code', models.CharField(db_column='result_code', max_length=255)),
                ('result_link', models.CharField(db_column='result_link', max_length=1024)),
                ('image_link', models.CharField(db_column='image_link', max_length=1024)),
                ('result_desc', models.CharField(db_column='result_desc', max_length=1024)),
            ],
            options={
                'db_table': 'wh_result',
                'managed': False,
            },
        ),
    ]
