# Generated by Django 3.1.2 on 2020-10-28 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_remove_user_email_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_vendor',
            field=models.BooleanField(choices=[(1, 'Yes'), (0, 'No')], default=1),
            preserve_default=False,
        ),
    ]
