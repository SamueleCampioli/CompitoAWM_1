# Generated by Django 2.2.5 on 2019-10-21 13:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('RaspNodeConfig', '0002_node_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('user', models.ForeignKey(null='TRUE', on_delete=django.db.models.deletion.CASCADE, related_name='room', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='node',
            name='room',
            field=models.ForeignKey(null='TRUE', on_delete=django.db.models.deletion.CASCADE, related_name='node', to='RaspNodeConfig.Room'),
            preserve_default='TRUE',
        ),
    ]
