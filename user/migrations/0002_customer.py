# Generated by Django 5.1.1 on 2024-09-20 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customerID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6)),
                ('senior_citizen', models.BooleanField()),
                ('partner', models.BooleanField()),
                ('dependents', models.BooleanField()),
                ('tenure', models.IntegerField()),
                ('phone_service', models.BooleanField()),
                ('multiple_lines', models.CharField(choices=[('No', 'No'), ('Yes', 'Yes'), ('No phone service', 'No phone service')], max_length=20)),
                ('internet_service', models.CharField(choices=[('DSL', 'DSL'), ('Fiber optic', 'Fiber optic'), ('No', 'No')], max_length=20)),
                ('online_security', models.BooleanField()),
                ('device_protection', models.BooleanField()),
                ('tech_support', models.BooleanField()),
                ('streaming_tv', models.BooleanField()),
                ('streaming_movies', models.BooleanField()),
                ('contract', models.CharField(choices=[('Month-to-month', 'Month-to-month'), ('One year', 'One year'), ('Two year', 'Two year')], max_length=20)),
                ('paperless_billing', models.BooleanField()),
                ('payment_method', models.CharField(choices=[('Electronic check', 'Electronic check'), ('Mailed check', 'Mailed check'), ('Bank transfer (automatic)', 'Bank transfer (automatic)'), ('Credit card (automatic)', 'Credit card (automatic)')], max_length=50)),
                ('monthly_charges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_charges', models.DecimalField(decimal_places=2, max_digits=10)),
                ('churn', models.BooleanField()),
            ],
        ),
    ]