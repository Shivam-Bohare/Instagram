from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from django.forms import modelformset_factory
from .forms import UserModelForm


def userDetails(request):

    if request.method == "POST":
        form = UserModelForm(request.POST)
        if form.is_valid():

            u = form.save()
            users = User.objects.all()

            return render(request, "display.html", {"users": users})

    else:
        form_class = UserModelForm

    return render(request, "social/userdetails.html", {"form": form_class})


def index(request):
    """View function for home page of site"""

    num_users = User.objects.all().count()  # pylint: disable=no-member

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {"num_users": num_users, "num_visits": num_visits}

    return render(request, "index.html", context=context)


class UserListView(LoginRequiredMixin, generic.ListView):
    model = User
    context_object_name = "user_list"
    queryset = User.objects.all()  # pylint: disable=no-member
    template_name = "social/user_list.html"
    # paginate_by = 2


class UserInfoDetailView(LoginRequiredMixin, generic.DetailView):
    model = User
    template_name = "social/user_detail.html"


class SearchResultsView(LoginRequiredMixin, generic.ListView):
    model = User
    template_name = "social/search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query == None:
            object_list = User.objects.all()[:5]
        else:
            object_list = User.objects.filter(
                Q(username__icontains=query)
                | Q(first_name__icontains=query)
                | Q(last_name__icontains=query)
            )
        return object_list
