# Generated by Django 4.1.4 on 2022-12-29 19:30

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("library_app", "0005_instancebook_instance_hall"),
    ]

    operations = [
        migrations.AddField(
            model_name="instancebook",
            name="who_reads",
            field=models.ManyToManyField(
                through="library_app.BooksOnHands",
                to=settings.AUTH_USER_MODEL,
                verbose_name="Читатель",
            ),
        ),
        migrations.AlterField(
            model_name="booksonhands",
            name="date_register",
            field=models.DateField(
                blank=True,
                default=datetime.datetime.today,
                null=True,
                verbose_name="Дата выдачи",
            ),
        ),
    ]
