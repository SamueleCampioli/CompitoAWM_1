# Generated by Django 2.1.5 on 2019-04-23 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenericCapabilityEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Node',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='ButtonCapabilityEntry',
            fields=[
                ('genericcapabilityentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='RaspNodeConfig.GenericCapabilityEntry')),
                ('descrizione', models.CharField(max_length=255)),
                ('pin', models.CharField(max_length=10)),
            ],
            bases=('RaspNodeConfig.genericcapabilityentry',),
        ),
        migrations.CreateModel(
            name='SwitchCapabilityEntry',
            fields=[
                ('genericcapabilityentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='RaspNodeConfig.GenericCapabilityEntry')),
                ('descrizione', models.CharField(max_length=255)),
                ('pin', models.CharField(max_length=255)),
            ],
            bases=('RaspNodeConfig.genericcapabilityentry',),
        ),
        migrations.CreateModel(
            name='TapparelleCapabilityEntry',
            fields=[
                ('genericcapabilityentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='RaspNodeConfig.GenericCapabilityEntry')),
                ('descrizione', models.CharField(max_length=255)),
                ('timeout', models.IntegerField()),
                ('pinUp', models.CharField(max_length=10)),
                ('pinDown', models.CharField(max_length=10)),
            ],
            bases=('RaspNodeConfig.genericcapabilityentry',),
        ),
        migrations.CreateModel(
            name='TemperaturaCapabilityEntry',
            fields=[
                ('genericcapabilityentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='RaspNodeConfig.GenericCapabilityEntry')),
                ('descrizione', models.CharField(max_length=255)),
                ('update', models.IntegerField()),
                ('pin', models.CharField(max_length=10)),
                ('sensor', models.CharField(max_length=10)),
            ],
            bases=('RaspNodeConfig.genericcapabilityentry',),
        ),
        migrations.AddField(
            model_name='genericcapabilityentry',
            name='node',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RaspNodeConfig.Node'),
        ),
        migrations.AddField(
            model_name='buttoncapabilityentry',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RaspNodeConfig.SwitchCapabilityEntry'),
        ),
    ]
