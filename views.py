from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import ObjectDoesNotExist, Q

from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework.filters import OrderingFilter
from rest_framework.pagination import PageNumberPagination

from django_filters import rest_framework as filters

from core.email import send_email
from core.models import CoreSettingsModel

from .models import StudentMobilityModel, SchoolMobilityModel, MeetingMobilityModel
from .forms import StudentMobilityForm
from .serializers import StudentMobilitySerializer, SchoolMobilitySerializer, MeetingMobilitySerializer


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
    meeting = filters.NumberFilter(method="meeting_by")

    class Meta:
        model = StudentMobilityModel
        fields = ("school", "meeting_point__track", "meeting_point",)

    def meeting_by(self, queryset, name, value):
        return queryset.filter(Q(meeting_point__pk=value) | Q(meeting_return__pk=value))


class PageNumberSizePagination(PageNumberPagination):
    page_size_query_param = "page_size"
    max_page_size = 1000


class MobilityDayViewSet(ModelViewSet):
    queryset = StudentMobilityModel.objects.all()
    serializer_class = StudentMobilitySerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter,)
    filter_class = MobilityFilter
    pagination_class = PageNumberSizePagination
    ordering_fields = ('by_bike', 'meeting_point__track', 'meeting_point','no_meeting',)

    def perform_create(self, serializer):
        email = serializer.validated_data["email"]
        core_settings = CoreSettingsModel.objects.first()
        url = core_settings.root
        send_email([email], "Inscription pour la journée mobilité", email_template="mobilityday/email.html",
                   context={'o': serializer.save, 'url': url})


class SchoolMobilityViewSet(ReadOnlyModelViewSet):
    queryset = SchoolMobilityModel.objects.all()
    serializer_class = SchoolMobilitySerializer


class MeetingFilter(filters.FilterSet):
    class Meta:
        model = MeetingMobilityModel
        fields = ("track",)


class MeetingMobilityViewSet(ReadOnlyModelViewSet):
    queryset = MeetingMobilityModel.objects.all()
    serializer_class = MeetingMobilitySerializer
    pagination_class = PageNumberSizePagination
    filter_backends = (filters.DjangoFilterBackend,)
    filter_class = MeetingFilter

