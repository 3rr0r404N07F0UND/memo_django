# Generated by Django 4.2.5 on 2023-10-17 08:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api_app", "0005_memo_memo_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="memo",
            name="memo_id",
            field=models.CharField(default="sia", max_length=20),
        ),
    ]