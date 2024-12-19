from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),    
    path('tutorial/content/<int:id>', views.PythonModuleContentView.as_view(), name='python_module_content'),
    path('tutorial/codeexecajaxcall/', views.exec_python_code, name='python_code_exec_ajax_call'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)