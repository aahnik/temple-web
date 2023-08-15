from django.db import models
from datetime import date, datetime
from django.utils.html import format_html

# Create your models here.


class ExpenseCategory(models.Model):
    category = models.CharField(max_length=256)
    category_balance = models.IntegerField(
        verbose_name="Balance",
        editable=False,
        default=0,
    )

    def __str__(self):
        return self.category


class Direction(models.TextChoices):
    INCOME = "IN", "🟢 Income"
    EXPENSE = "EX", "🔴 Expense"


class FundRaiser(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name


# for expense
# purchase bill no
# purchase shop details
# approved by


# for income
# bill no
# fund raiser (select from items)
# person address


def generate_invoice_no():
    now = datetime.now()
    return f"IB{now.strftime('%d-%m-%Y')}-{now.strftime('%H-%M-%S')}"


class Transanction(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.SET_NULL, null=True)
    amount = models.PositiveIntegerField(default=0)
    purpose = models.CharField(verbose_name="Purpose/Detail", max_length=512)
    tdate = models.DateField(verbose_name="Date", auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    ttype = models.CharField(
        verbose_name="Transanction Type", max_length=12, choices=Direction.choices
    )
    auto_invoice_id = models.CharField(
        max_length=128, unique=True, default=generate_invoice_no, editable=False
    )
    bill_no = models.CharField(max_length=128, null=True, blank=True)
    approved_by = models.CharField(max_length=256, blank=True, null=True)
    fund_raiser = models.ForeignKey(
        FundRaiser, on_delete=models.SET_NULL, null=True, blank=True
    )
    extra_details = models.TextField(max_length=1024, null=True, blank=True)

    signed_amount = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return f"{self.get_ttype_display()} of Rs. {self.amount} on {self.tdate.strftime('%d %b %Y')}"

    def invoice_link(self):
        return format_html(
            f'<a href="/accounts/invoice?id={self.auto_invoice_id}" target="_blank">{self.auto_invoice_id}</a>'
        )

    def save(self, *args, **kwargs):
        signed_amt = -self.amount if self.ttype == "EX" else self.amount

        diff = signed_amt - self.signed_amount

        self.signed_amount = signed_amt
        print(self.amount)
        print(self.signed_amount)
        print(self.category)
        category = ExpenseCategory.objects.get(id=self.category.pk)

        category.category_balance += diff
        category.save()
        super().save(*args, **kwargs)