from django.contrib import admin
from .models import ExpenseCategory, Transanction, FundRaiser

# Register your models here.


@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ["category", "category_balance"]
    pass


@admin.register(FundRaiser)
class FundraiserAdmin(admin.ModelAdmin):
    pass


class AmountRangeFilter(admin.SimpleListFilter):
    title = "Amount Range"
    parameter_name = "amount_range"

    def lookups(self, request, model_admin):
        return (
            ("0-1000", "0 - 1000"),
            ("1000-5000", "1000 - 5000"),
            ("5000-10000", "5000 - 10000"),
            ("10000", "10000 and above"),
        )

    def queryset(self, request, queryset):
        if self.value() == "0-1000":
            return queryset.filter(amount__range=(0, 1000))
        elif self.value() == "1000-5000":
            return queryset.filter(amount__range=(1000, 5000))
        elif self.value() == "5000-10000":
            return queryset.filter(amount__range=(5000, 10000))
        elif self.value() == "10000":
            return queryset.filter(amount__gte=10000)


@admin.register(Transanction)
class TransanctionAdmin(admin.ModelAdmin):
    search_fields = ["amount", "purpose"]
    list_display = [
        "ttype",
        "amount",
        "purpose",
        "tdate",
        "category",
        "invoice_link",
    ]
    list_filter = ["ttype", AmountRangeFilter, "tdate", "category"]
