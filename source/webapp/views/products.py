from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView

from webapp.forms import ProductForm
from webapp.models import Product
from webapp.views.base_view import SearchView


class IndexView(SearchView):
    model = Product
    template_name = 'product/index.html'
    ordering = ['category', 'name']
    search_fields = ['name__icontains']
    paginate_by = 3
    context_object_name = 'products'

    # def get_queryset(self):
    #     return super().get_queryset().filter(amount__gt=0)


class ProductView(DetailView):
    model = Product
    template_name = 'product/product_view.html'
    # queryset = Product.objects.filter(amount__gt=0)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.object.id
        context['reviews'] = Product.objects.filter(id=id)
        return context


class ProductCreate(PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_create.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return self.request.user.has_perm("webapp.add_product")


class ProductUpdate(PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_update.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return self.request.user.has_perm("webapp.change_product")


class ProductDelete(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'product/product_delete.html'
    success_url = reverse_lazy('webapp:index')

    def has_permission(self):
        return self.request.user.has_perm("webapp.delete_product")