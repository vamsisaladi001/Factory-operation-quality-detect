from django.db import models

# Create your models here.
class Super(models.Model):
    work_order_number=models.CharField(max_length=50,unique=True)
    part_number=models.CharField(max_length=20)
    part_name=models.CharField(max_length=100)
    planned_quantity=models.PositiveIntegerField()
    already_produced=models.PositiveIntegerField(default=0)
    due_date=models.DateField(null=True,blank=True)
    meachine_workstation=models.CharField(max_length=5)
    STATUS_CHOICES = [
        ("PLANNED", "Planned"),
        ("IN_PROGRESS", "In Progress"),
        ("COMPLETED", "Completed"),
        ("ON_HOLD", "On Hold"),
    ]
    initial_type = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="PLANNED"
    )
    def __str__(self):
        return self.work_order_number



class QualityInspection(models.Model):
    INSPECTION_TYPES = [
        ("FIRST_PIECE", "First Piece"),
        ("IN_PROCESS", "In Process"),
        ("FINAL", "Final Inspection"),
    ]

    RESULTS = [
        ("PASS", "Pass"),
        ("FAIL", "Fail"),
    ]

    REVIEW_STATUSES = [
        ("PENDING", "Pending Review"),
        ("APPROVED", "Approved"),
        ("REJECTED", "Rejected"),
        ("REWORK", "Rework Required"),
    ]

    work_order = models.ForeignKey(
        "space.Super",
        on_delete=models.PROTECT,
        related_name="quality_inspections",
    )

    inspection_type = models.CharField(
        max_length=20,
        choices=INSPECTION_TYPES,
        default="IN_PROCESS",
    )

    inspector_name = models.CharField(max_length=100)

    dimension_name = models.CharField(max_length=100)

    nominal_value = models.DecimalField(
        max_digits=12,
        decimal_places=4,
    )

    lower_limit = models.DecimalField(
        max_digits=12,
        decimal_places=4,
    )

    upper_limit = models.DecimalField(
        max_digits=12,
        decimal_places=4,
    )

    measured_value = models.DecimalField(
        max_digits=12,
        decimal_places=4,
    )

    unit = models.CharField(max_length=20, default="mm")

    result = models.CharField(
        max_length=10,
        choices=RESULTS,
        editable=False,
    )

    defect_notes = models.TextField(blank=True)

    review_status = models.CharField(
        max_length=10,
        choices=REVIEW_STATUSES,
        default="PENDING",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.result = (
            "PASS"
            if self.lower_limit <= self.measured_value <= self.upper_limit
            else "FAIL"
        )

        if self.result == "FAIL" and not self.defect_notes.strip():
            raise ValueError(
                "Defect notes are required for failed inspections."
            )

        if self.result == "FAIL":
            self.review_status = "PENDING"

        super().save(*args, **kwargs)

    def __str__(self):
        return (
            f"{self.work_order.work_order_number} - "
            f"{self.dimension_name} - {self.result}"
        )
