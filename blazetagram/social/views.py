from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
from .models import UserInfo, Picture, PictureLike
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template import loader
from django.forms import modelformset_factory
#from .forms import UserModelForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import FormView
#from social.forms import UserInfoForm
from social.forms import UserForm, PictureForm
from django.urls import reverse
from django.views.generic import UpdateView
from django.shortcuts import render, redirect 

# def userDetails(request, pk):
#     userinfo = get_object_or_404(UserInfo, pk=pk)
#     if request.method == "POST":
#         form = UserModelForm(request.POST, instance = request.user)
#         if form.is_valid():
            
#             u = form.save()
#             #user = UserInfo.objects.all() 
            
#             userinfo.website = form.cleaned_data['website']
#            # book_instance.save()

#             return render(request, "social/profile.html", {"user": u})

#     else:
#         u2 = UserModelForm(instance = request.user)
#         args ={}
#         args["u2"]= u2

#     return render(request, "social/edit_profile.html", args)

class NewUserView(FormView):
    template_name = "social/edit_profile.html"
    form_class = UserForm

    def form_valid(self, form):
        form.save(self.request.user)
        return super(NewUserView, self).form_valid(form)

    def get_success_url(self, *args, **kwargs):
        return reverse("search")
    
class EditUserView(UpdateView):
    model = User
    form_class = UserForm
    template_name = "social/index.html"

    def get_object(self, *args, **kwargs): #*args, **kwargs):
        #user = get_object_or_404(User, pk=self.kwargs['pk'])
        obj, created = User.objects.get_or_create(pk=self.kwargs['pk'])
        # We can also get user object using self.request.user  but that doesnt work User, pk=self.kwargs['pk']
        # for other models.

        return obj

    def get_success_url(self, *args, **kwargs):
        return reverse("index")

def picture_view(request): 
  
    if request.method == 'POST': 
        #instance = UserInfo.objects.filter(user=request.user).first()
        form = PictureForm(request.POST, request.FILES) 
  
        if form.is_valid():
            instance = form.save(commit=False)
            instance.picture_user_id=request.user
            instance.save()
            return redirect('index') 
    else:
        form = PictureForm() # pylint: disable=no-member
    return render(request, 'social/add_picture.html', {'form' : form}) 
  
  
def success(request): 
    return HttpResponse('successfuly uploaded') 


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


# class UserInfoDetailView(LoginRequiredMixin, generic.DetailView):
#     model = User
#     template_name = "social/user_detail.html"
    

def userInfoDetailView(request , pk):

    user_detail = User.objects.get(id=pk)
    pictures = Picture.objects.filter(picture_user_id=pk) # pylint: disable=no-member

    context = {"user" : user_detail , "pictures" : pictures}

    return render(request, "social/user_detail.html", context=context)


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
