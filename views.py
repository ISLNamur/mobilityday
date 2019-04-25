from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import ObjectDoesNotExist

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import OrderingFilter

from django_filters import rest_framework as filters

from core.email import send_email
from core.models import CoreSettingsModel

from .models import StudentMobilityModel, SchoolMobilityModel
from .forms import StudentMobilityForm
from .serializers import StudentMobilitySerializer, SchoolMobilitySerializer


class MobilityDayTemplate(TemplateView):
    template_name = "mobilityday/mobilityday.html"

    def get_context_data(self, **kwargs):
        context = {'uuid': ''}
        print(self.kwargs)
        if 'model_id' in self.kwargs:
            try:
                student = StudentMobilityModel.objects.get(uuid=self.kwargs['model_id'])
                context['uuid'] = self.kwargs['model_id']

                form = StudentMobilityForm(instance=student)
            except ObjectDoesNotExist:
                form = StudentMobilityForm()
        else:
            form = StudentMobilityForm()
        context['form'] = form
        return context


class ResultsTemplate(LoginRequiredMixin, PermissionRequiredMixin, TemplateView):
    template_name = "mobilityday/results.html"
    permission_required = "mobilityday.add_studentmobilitymodel"


class MobilityFilter(filters.FilterSet):
    class Meta:
        model = StudentMobilityModel
        fields = "__all__"


class MobilityDayViewSet(ModelViewSet):
    queryset = StudentMobilityModel.objects.all()
    serializer_class = StudentMobilitySerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_class = MobilityFilter

    def perform_create(self, serializer):
        email = serializer.validated_data["email"]
        core_settings = CoreSettingsModel.objects.first()
        url = core_settings.root
        send_email(email, "Inscription pour la journée mobilité", email_template="mobilityday/email.html",
                   context={'o': serializer.save, 'url': url})


class SchoolMobilityViewSet(ReadOnlyModelViewSet):
    queryset = SchoolMobilityModel.objects.all()
    serializer_class = SchoolMobilitySerializer
