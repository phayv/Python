from django.views import generic
from products.models import Product


class IndexView(generic.list.ListView):
    template_name = 'frontend/index.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Product.objects.order_by("sku")[:5]
