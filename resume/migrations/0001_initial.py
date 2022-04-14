# Generated by Django 4.0.4 on 2022-04-14 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('url', models.URLField(max_length=400)),
                ('image', models.ImageField(upload_to='images/')),
                ('technologies_used', models.CharField(blank=True, max_length=200)),
            ],
        ),
    ]
