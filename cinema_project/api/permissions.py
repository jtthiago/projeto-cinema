from rest_framework import permissions

class IsStaffOrReadOnly(permissions.BasePermission):
    """
    Permite acesso de leitura para todos, mas apenas funcionários podem modificar.
    """
    def has_permission(self, request, view):
        # Permite GET, HEAD, OPTIONS para qualquer usuário
        if request.method in permissions.SAFE_METHODS:
            return True
        # Apenas funcionários podem criar, editar ou deletar
        return request.user and request.user.is_staff