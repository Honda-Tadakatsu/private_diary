import logging

from django.urls import reverse_lazy
from django.views import generic
from .forms import InquiryForm
from django.contrib import messages


# Create your views here.

logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name="diary/index.html"

class InquiryView(generic.FormView):
    template_name = "diary/inquiry.html"
    form_class = InquiryForm
    success_url = url = reverse_lazy('diary:inquiry')

    def form_valid(self, form):
        form.send_email()
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class InquiryView(generic.FormView):
    template_name = 'diary/inquiry.html'
    form_class = InquiryForm
    success_url = reverse_lazy('diary:inquiry')

    def form_valid(self,form):
        form.send_email()
        messages.success(self.request,'メッセージを送信しました。')
        logger.info('Inquiry send by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)