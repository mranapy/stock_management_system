# Generated by Django 4.0.3 on 2022-07-29 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.IntegerField(choices=[(1, 'Active'), (0, 'Inactive')], default=0)),
                ('cat_name', models.CharField(max_length=264)),
                ('cat_brand', models.CharField(max_length=264)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
