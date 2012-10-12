from django.forms import ModelForm
from csp.models import Report


class ReportForm(ModelForm):

    class Meta:
        model = Report
        fields = ('document_uri', 'blocked_uri', 'referrer',
                  'violated_directive', 'original_policy',)
