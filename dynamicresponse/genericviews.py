from django.views.generic.detail import SingleObjectMixin
from django.views.generic.list import MultipleObjectMixin
from django.views.generic.base import View
from response import SerializeObject, CR_NOT_FOUND

class SerializeDetailView(SingleObjectMixin, View):
    def get(self, request, **kwargs):
        return SerializeObject(context=self.get_object())


class SerializeListView(MultipleObjectMixin, View):
    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        allow_empty = self.get_allow_empty()
        if not allow_empty and len(self.object_list) == 0:
            raise Serialize(context = { "error" : _(u"Empty list and '%(class_name)s.allow_empty' is False.") % {'class_name': self.__class__.__name__} },
                            status = CR_NOT_FOUND)
        return SerializeObject(self.object_list)
