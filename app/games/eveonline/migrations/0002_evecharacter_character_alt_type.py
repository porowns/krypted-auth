# Generated by Django 2.0.1 on 2018-01-25 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eveonline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evecharacter',
            name='character_alt_type',
            field=models.CharField(choices=[('PvP Alt', 'PvP Alt'), ('Capital Alt', 'Capital Alt'), ('Industry Alt', 'Industry Alt'), ('Useless Alt', 'Useless Alt')], max_length=255, null=True),
        ),
    ]
