# Generated by Django 4.0.4 on 2022-12-03 05:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Tovar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='upload')),
                ('title', models.CharField(blank=True, max_length=300)),
                ('status', models.IntegerField(blank=True, default=0)),
                ('cat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
    ]
