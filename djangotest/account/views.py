'''
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth import get_user_model

from djangotest.account.forms import UserForm, UserUpdateForm


@login_required
@permission_required('auth.delete_user', raise_exception=True)
def user_active_or_disable(request, pk):
    user = get_user_model().objects.get(pk=pk)
    if user.pk is not request.user.pk:
        status = not user.is_active
        user.is_active = status
        user.save()
        messages.success(request, 'O usuário {} foi {} com sucesso.'.format(user.username, 'ativado' if status else 'desativado'))
    else:
        messages.error(request, 'Não é possível desativar o próprio usuário.')
    return HttpResponseRedirect(reverse('account:user-list'))


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = 'auth.view_user'
    raise_exception = True
    model = get_user_model()
    template_name = 'account/user/list.html'
    context_object_name = 'users'


class UserCreateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = ('auth.add_user', 'auth.view_user')
    raise_exception = True
    model = get_user_model()
    form_class = UserForm
    template_name = 'account/user/form.html'
    success_url = reverse_lazy('account:user-list')
    success_message = "O usuário %(username)s foi criado com sucesso."

    def form_valid(self, form):
        form.instance.set_password(form.instance.password)
        return super(UserCreateView, self).form_valid(form)


class UserUpdateView(LoginRequiredMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = ('auth.change_user', 'auth.view_user')
    raise_exception = True
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'account/user/form.html'
    success_url = reverse_lazy('account:user-list')
    success_message = "O usuário %(username)s foi atualizado com sucesso."
'''