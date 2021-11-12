from django.contrib import admin
from .models import (Administrador,
                          AudAdmin,
                          AudCargo,
                          AudCasos,
                       AudEvaluado,
                      AudEvaluador,
                             Cargo,
                             Casos,
                    EvaluacionCaso,
                          Evaluado,
                         Evaluador,
                         Resultado)
# Register your models here.

admin.site.register(Administrador)
admin.site.register(AudAdmin)
admin.site.register(AudCargo)
admin.site.register(AudCasos)
admin.site.register(AudEvaluado)
admin.site.register(AudEvaluador)
admin.site.register(Cargo)
admin.site.register(Casos)
admin.site.register(EvaluacionCaso)
admin.site.register(Evaluado)
admin.site.register(Evaluador)
admin.site.register(Resultado)