# Generated by Django 4.2.5 on 2023-09-18 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_delete_choice_delete_question'),
    ]

    operations = [
        migrations.AddField(
            model_name='washroom',
            name='unique_id',
            field=models.IntegerField(default=334455),
            preserve_default=False,
        ),
    ]
