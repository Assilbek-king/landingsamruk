# Generated by Django 4.0.4 on 2022-12-05 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_feedback_categoriya'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
