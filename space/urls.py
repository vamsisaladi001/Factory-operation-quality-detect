from django.urls import path
from .views import listall
from.views import postall
from.views import delete
from .views import update
from .views import QualityInspectionListCreateView
from .views import QualityInspectionDetailView
urlpatterns=[
    path("show/", listall.as_view()),
    path("add/", postall.as_view()),
    path("<int:pk>/delete/", delete.as_view()),
    path("<int:pk>/update", update.as_view(),name="work-order-update"),
    path(
        "quality/",
        QualityInspectionListCreateView.as_view(),
        name="quality-inspection-list-create",
    ),
    path(
        "quality/<int:pk>/",
        QualityInspectionDetailView.as_view(),
        name="quality-inspection-detail",
    ),
]