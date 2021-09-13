import posixpath
import diary
import logging

from django.urls import reverse_lazy
from django.views import generic
from .forms import DiaryCreateForm, InquiryForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary

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

class DiaryListView(LoginRequiredMixin, generic.ListView):
    model = Diary
    template_name = 'diary_list.html'
    paginate_by = 2

    def get_queryset(self):
        diaries = Diary.objects.filter(user = self.request.user).order_by('-created_at')
        return diaries

class DetailView(generic.DetailView):
    model = posixpathslug_field = "title"
    slug_url_kwarg = "title"

class DiaryDetailView(LoginRequiredMixin, generic.DetailView):
    model = Diary
    template_name = "diary_detail.html"
    pk_url_kwarg = "id"

class DiaryCreateView(LoginRequiredMixin,generic.CreateView):
    model = Diary
    template_name = "diary_create.html"
    

    def get_success_url(self):
        return reverse_lazy('diary:diary_detail',kwargs={'pk':self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request,'日記を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request,"日記の作成に失敗しました。")
        return super().form_invalid(form)