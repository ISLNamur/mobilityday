from django import forms
from django.utils.translation import gettext_lazy as _

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div, Field, Hidden, HTML, Button
from crispy_forms.bootstrap import FormActions, Tab, TabHolder, Alert

from .models import StudentMobilityModel


class StudentMobilityForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentMobilityForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper(self)
        self.helper.attrs = {'autocomplete': 'off'}
        self.helper.html5_required = True

        self.helper.layout = Layout(
            TabHolder(
                Tab("Identification",
                    Field("school"),
                    Field("year"),
                    Field("classe"),
                    Field("first_name"),
                    Field("last_name"),
                    Field("email"),
                    Field("by_bike"),
                    Div(
                        HTML("Problème"),
                        css_class="alert alert-danger",
                        css_id="identification-error",
                        role="alert",
                        style="display:none;margin-top:15px"
                    ),
                    Button("from_ident", "Suivant"),
                    ),
                Tab("En vélo",
                    Field("address_start"),
                    Field("no_meeting"),
                    HTML("<label id='maplabel'>Cliquez sur les différents points pour sélectionner le lieu de rencontre</label>"),
                    Div(
                        css_id="mapid",
                        style="height:490px;width:100%"
                    ),
                    Field("meeting_point"),
                    Field("custom_return"),
                    Field("modality_return"),
                    Field("contact_return"),
                    Field("contact_phone_return"),
                    Div(
                        HTML("Problème"),
                        css_class="alert alert-danger",
                        css_id="bike-error",
                        role="alert",
                        style="display:none;margin-top:15px"
                    ),
                    Button("from_bike", "Suivant"),
                    ),
                Tab("Autrement",
                    Field("transportation"),
                    Div(
                        HTML("Problème"),
                        css_class="alert alert-danger",
                        css_id="other-error",
                        role="alert",
                        style="display:none;margin-top:15px"
                    ),
                    Button("from_other", "Suivant"),
                    ),
                Tab("Enregistrement",
                    Alert(content="Un email de confirmation sera envoyé. Un lien sera mis à votre disposition afin de modifier les données de l'inscription. Si vous ne voyez pas l'email, merci de regarder dans le dossier des courriers indésirables.",
                          css_class="alert-info"),
                    Submit('submit', 'Soumettre'),
                    Div(
                        HTML("Problème"),
                        css_class="alert alert-danger",
                        css_id="all-error",
                        role="alert",
                        style="display:none;margin-top:15px"
                    ),
                    Div(
                        HTML("La demande a bien été envoyé. Merci ! Un email vous a été envoyé."),
                        css_class="alert alert-success",
                        css_id="success",
                        role="alert",
                        style="display:none;margin-top:15px"
                    ),
                    ),
            ),
        )

    class Meta:
        model = StudentMobilityModel
        fields = '__all__'
        labels = {
            "school": _("École"),
            "year": _("Année d'étude"),
            "classe": _("Classe (lettre)"),
            "first_name": _("Prénom"),
            "last_name": _("Nom"),
            "email": _("Email (pour la confirmation et modification de votre enregistrement)"),
            "by_bike": _("Je viens en vélo pour 9h20 à l'Institut Notre-Dame derrière le théâtre"),
            "address_start": _("Adresse du domicile de départ"),
            "no_meeting": _("Trajet personnel (sans la responsabilité de l'école)"),
            "custom_return": _("Retour différent"),
            "modality_return": _("Modalité de retour"),
            "meeting_point": _("Lieu de rencontre"),
            "contact_return": _("Personne de contact"),
            "contact_phone_return": _("Téléphone de contact"),
            "transportation": _("Moyen de transport"),
            "workshop": _("Atelier"),
        }
