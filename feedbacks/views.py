from django.shortcuts import render
from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import CreateView
from django.core.mail import mail_admins
from feedbacks.models import Feedback

class FeedbackView(CreateView):
    model = Feedback
    fields = '__all__'
    template_name = 'feedback.html'

    def get_context_data(self, **kwargs):
        context = super(FeedbackView, self).get_context_data(**kwargs)
        context['title'] = "Leave a feedback"
        return context

    def form_valid(self, form):
        data = form.cleaned_data
        mail_admins(data['subject'], data['massage'], fail_silently=True)
        messages.success(self.request, "Thank you for your feedback! We will keep in touch with you very soon!")
        self.success_url = reverse_lazy('feedback')
        return super(FeedbackView, self).form_valid(form)

