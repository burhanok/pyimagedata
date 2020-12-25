# Generated by Django 3.0.5 on 2020-04-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DatasciencePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('publishing_date', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeepLearningPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('publishing_date', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MachineLearningPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('publishing_date', models.TimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='RFLearningPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('publishing_date', models.TimeField(auto_now_add=True)),
            ],
        ),
    ]