from django.views.generic import TemplateView, ListView

from .models import Page


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "pages/about.html"


class AllPagesView(ListView):
    model = Page
    template_name = "pages/pages_index.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = Page.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["besked"] = "Demo til Lone"
        return context


class LetterPagesView(ListView):
    model = Page
    template_name = "pages/pages_index.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(title__startswith=self.kwargs["letter"])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["letter"] = self.kwargs["letter"]
        context["besked"] = f'... that begins with {self.kwargs["letter"]}'
        return context
