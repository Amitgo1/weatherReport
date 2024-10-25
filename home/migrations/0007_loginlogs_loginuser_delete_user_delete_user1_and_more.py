# Generated by Django 5.1.2 on 2024-10-24 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_user2_remove_user1_city'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(max_length=6)),
                ('is_used', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True)),
                ('phoneno', models.CharField(max_length=15, unique=True)),
                ('is_verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='User1',
        ),
        migrations.DeleteModel(
            name='User2',
        ),
        migrations.AddField(
            model_name='loginlogs',
            name='login_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.loginuser'),
        ),
    ]