# Generated by Django 4.2.1 on 2023-07-21 21:36

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ExpenseCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.CharField(max_length=256)),
                (
                    "category_balance",
                    models.PositiveIntegerField(
                        default=0, editable=False, verbose_name="Balance"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FundRaiser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name="Transanction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField(default=0)),
                (
                    "purpose",
                    models.CharField(max_length=512, verbose_name="Purpose/Detail"),
                ),
                ("tdate", models.DateField(auto_now_add=True, verbose_name="Date")),
                ("last_updated", models.DateTimeField(auto_now=True)),
                (
                    "ttype",
                    models.CharField(
                        choices=[("IN", "🟢 Income"), ("EX", "🔴 Expense")],
                        max_length=12,
                        verbose_name="Transanction Type",
                    ),
                ),
                (
                    "auto_invoice_id",
                    models.CharField(
                        default=accounts.models.generate_invoice_no,
                        editable=False,
                        max_length=128,
                        unique=True,
                    ),
                ),
                ("bill_no", models.CharField(blank=True, max_length=128, null=True)),
                (
                    "approved_by",
                    models.CharField(blank=True, max_length=256, null=True),
                ),
                (
                    "extra_details",
                    models.TextField(blank=True, max_length=1024, null=True),
                ),
                ("signed_amount", models.IntegerField(editable=False)),
                (
                    "category",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.expensecategory",
                    ),
                ),
                (
                    "fund_raiser",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="accounts.fundraiser",
                    ),
                ),
            ],
        ),
    ]