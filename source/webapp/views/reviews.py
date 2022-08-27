from django.contrib.auth.mixins import UserPassesTestMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView

from webapp.forms import ReviewForm
from webapp.models import Product, Review


class CreateReview(CreateView):
    form_class = ReviewForm
    template_name = "reviews/create.html"

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get("pk"))
        user = self.request.user
        form.instance.product = product
        form.instance.author = user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("webapp:product_view", kwargs={"pk": self.object.product.pk})


class UpdateReview(PermissionRequiredMixin, UpdateView):
    form_class = ReviewForm
    template_name = "reviews/update.html"
    model = Review

    # def test_func(self):
    #     return self.get_object().author == self.request.user or\
    #            self.request.user.has_perm('webapp.change_review')

    def get_success_url(self):
        return reverse("webapp:product_view", kwargs={"pk": self.object.product.pk})

    def has_permission(self):
        return self.request.user.has_perm("webapp.change_review") or self.request.user == self.get_object().user


class DeleteReview(PermissionRequiredMixin, DeleteView):
    model = Review

    def get(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse("webapp:product_view", kwargs={"pk": self.object.ptoduct.pk})

    def has_permission(self):
        return self.request.user.has_perm("webapp.delete_review") or self.request.user == self.get_object().user