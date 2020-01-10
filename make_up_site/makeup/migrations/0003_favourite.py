# Generated by Django 2.2.5 on 2020-01-08 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0002_auto_20200107_2127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice_text', models.CharField(max_length=200)),
                ('votes', models.IntegerField(default=0)),
                ('decorative', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeup.Decorative')),
            ],
        ),
    ]