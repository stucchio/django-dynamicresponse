from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import View
from response import SerializeObject

class SerializeDetailView(SingleObjectMixin, View):
    def get(self, request, **kwargs):
        return SerializeObject(context=self.get_object())

