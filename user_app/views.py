from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from user_app.models import CustomUser
from django.http import HttpResponseRedirect
from django.urls import reverse

class UserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'
    context_object_name = 'users'

class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'user_detail.html'
    context_object_name = 'user'
    
    def get(self, request,pk, *args, **kwargs):
        try:
            CustomUser.objects.get(id=pk)
            return super().get(request, *args, **kwargs)
        except self.model.DoesNotExist:
            return HttpResponseRedirect(reverse('user-list'))
    

class UserCreateView(CreateView):
    model = CustomUser
    template_name = 'user_form.html'
    fields = ('first_name','last_name','email','cnic','dob','username','password',)
    success_url = reverse_lazy('user-list')

class UserUpdateView(UpdateView):
    model = CustomUser
    template_name = 'user_form.html'
    fields = ('first_name','last_name','email','cnic','dob',)
    success_url = reverse_lazy('user-list')

class UserDeleteView(DeleteView):
    model = CustomUser
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user-list')

    def get(self, request,pk, *args, **kwargs):
        try:
            CustomUser.objects.get(id=pk)
            return super().get(request, *args, **kwargs)
        except self.model.DoesNotExist:
            return HttpResponseRedirect(reverse('user-list'))