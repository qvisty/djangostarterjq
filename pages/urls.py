from django.urls import path

from .views import (
    HomePageView,
    AboutPageView,
    AllPagesView,
    LetterPagesView,
    LetterPagesViewFunctionBased,
)

urlpatterns = [
    path("home/", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", AllPagesView.as_view(), name="all_pages"),
    path("pages/<str:letter>", LetterPagesView.as_view(), name="LetterPagesView"),
    path(
        "pages/func/<str:letter>",
        LetterPagesViewFunctionBased,
        name="LetterPagesViewFunctionBased",
    ),
]
