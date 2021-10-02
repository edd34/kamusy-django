# Generated by Django 3.2.7 on 2021-10-02 15:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('language', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Translation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_destination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='l_destination', to='language.language')),
                ('language_source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='l_source', to='language.language')),
            ],
        ),
    ]
