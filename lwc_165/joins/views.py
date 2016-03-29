from django.shortcuts import render

# Create your views here.
from .forms import EmailForm, JoinForm
from .models import Join


def home(request):

    # THIS IS USING REGULAR DJANGO FORMS
    # ==================================
    # form = EmailForm(request.POST or None)
    # if form.is_valid():
    #     email = form.cleaned_data['email']
    #     new_join, created = Join.objects.get_or_create(email=email)
    #     print(new_join, created)
    #     print(new_join.timestamp)

    # THIS IS USING MODEL FORMS
    # =========================
    form = JoinForm(request.POST or None)
    if form.is_valid():
        new_join = form.save(commit=False)
        # don't save it yet, might do something here
        email = form.cleaned_data['email']
        new_join_old, created = Join.objects.get_or_create(email=email)
        # new_join.save()

    context = {'form': form}
    template = "home.html"
    return render(request, template, context)
