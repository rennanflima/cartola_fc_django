from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


# Register your models here.
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff',)
    search_fields = ['first_name', 'last_name', 'username', 'email']
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'groups',)
    actions = ['activate_register', 'deactivate_register']

    def activate_register(self, request, queryset):
        """Ação para ativar usuários selecionados."""
        count = queryset.update(is_active=True)
        if count == 1:
            msg = '{} usuário foi ativado.'
        else:
            msg = '{} usuários foram ativados.'

        self.message_user(request, msg.format(count))

    activate_register.short_description = 'Ativar usuários selecionados'

    def deactivate_register(self, request, queryset):
        """Ação para desativar usuários selecionados."""
        count = queryset.update(is_active=False)

        if count == 1:
            msg = '{} usuário foi desativado.'
        else:
            msg = '{} usuários foram desativados.'

        self.message_user(request, msg.format(count))

    deactivate_register.short_description = 'Desativar usuários selecionados'
