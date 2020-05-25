# Generated by Django 3.0.6 on 2020-05-25 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeddingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('start', models.DateField()),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='calenders',
            field=models.ManyToManyField(related_name='_cart_calenders_+', to='WeddingApp.Calender'),
        ),
    ]
