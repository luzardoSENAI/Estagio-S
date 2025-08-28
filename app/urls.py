from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from accounts.views import register_view, login_view, logout_view, home_redirect


from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),

       # Redireciona home dinâmica
    path('', home_redirect, name='home'),

    # Accounts
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', include('accounts.urls')), 

    
    # Livros (inclui urls do app livro)
    path('livros/', include('livro.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
