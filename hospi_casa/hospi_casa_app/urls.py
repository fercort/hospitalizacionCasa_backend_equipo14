from django.urls import path
from .  import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
   path('newPaciente/', views.newPaciente),
   path('newMedico/', views.newMedico),
   path('newSigno/', views.newSigno),
   path('newHistoriaClinica/', views.newHistoriaClinica),
   path('newHistoriaSigno/', views.newHistoriaSigno),
   path('getAllPacientes/', views.getAllPacientes),
   path('getAllMedicos/', views.getAllMedicos),
   path('getAllSignos/', views.getAllSignos),
   path('updatePaciente/<int:id_paciente>', views.updatePaciente),
   path('updateMedico/<int:id_medico>', views.updateMedico),
   path('updateSigno/<int:id_signo>', views.updateSigno),
   path('deletePaciente/<int:id_paciente>', views.deletePaciente),
   path('deleteMedico/<int:id_medico>', views.deleteMedico),
   path('deleteSigno/<int:id_signo>', views.deleteSigno),
   path('getOnePaciente/<int:id_paciente>', views.getOnePaciente),
   path('login/', views.login),
   
   
]
