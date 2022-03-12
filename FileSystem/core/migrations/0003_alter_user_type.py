# Generated by Django 4.0.3 on 2022-03-12 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(blank=True, choices=[('HEAD', 'Head'), ('SECRETARY', 'Secretary')], max_length=50, null=True, verbose_name='Type'),
        ),
    ]
