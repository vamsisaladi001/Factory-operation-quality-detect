
from rest_framework import serializers
from .models import Super, QualityInspection



class SuperSerializer(serializers.ModelSerializer):
    produced_quantity = serializers.IntegerField(
        source="already_produced",
        required=False
    )
    machine_name = serializers.CharField(
        source="meachine_workstation",
        required=False,
        allow_blank=True
    )
    status = serializers.ChoiceField(
        source="initial_type",
        choices=Super.STATUS_CHOICES,
        required=False
    )

    class Meta:
        model = Super
        fields = [
            "id",
            "work_order_number",
            "part_number",
            "part_name",
            "planned_quantity",
            "produced_quantity",
            "due_date",
            "machine_name",
            "status",
        ]


class QualityInspectionSerializer(serializers.ModelSerializer):
    work_order_number = serializers.CharField(
        source="work_order.work_order_number",
        read_only=True
    )

    class Meta:
        model = QualityInspection
        fields = [
            "id",
            "work_order",
            "work_order_number",
            "inspection_type",
            "inspector_name",
            "dimension_name",
            "nominal_value",
            "lower_limit",
            "upper_limit",
            "measured_value",
            "unit",
            "result",
            "defect_notes",
            "review_status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "result",
            "review_status",
            "created_at",
            "updated_at",
        ]

    def validate(self, attrs):
        lower = attrs.get("lower_limit")
        upper = attrs.get("upper_limit")
        measured = attrs.get("measured_value")
        defect_notes = attrs.get("defect_notes", "")

        if lower is not None and upper is not None and lower > upper:
            raise serializers.ValidationError({
                "upper_limit": "Upper limit must be greater than or equal to lower limit."
            })

        if lower is not None and upper is not None and measured is not None:
            if not lower <= measured <= upper and not defect_notes.strip():
                raise serializers.ValidationError({
                    "defect_notes": "Defect notes are required when a measurement fails."
                })

        return attrs
