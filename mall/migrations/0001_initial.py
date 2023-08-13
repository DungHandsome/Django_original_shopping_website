# Generated by Django 4.2.3 on 2023-08-13 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('description', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('kind', models.CharField(choices=[('technology', 'Technology'), ('fashion', 'Fashion'), ('healthbeauty', 'Health and Beauty'), ('toy', 'Toy'), ('fitness', 'Fitness'), ('food', 'Food')], default='technology', max_length=100)),
                ('cost', models.IntegerField()),
            ],
        ),
    ]
