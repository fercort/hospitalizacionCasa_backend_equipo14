import datetime
import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseBadRequest
from . models import pacientes , medicos , signos_vitales , historias_clinicas, historias_signos

# Create your views here.


# vista de prueba
def inicio(request):
    return HttpResponse("inicio de las vistas")

#---------------------------------------------------------------------------------------    
########################## VISTAS PARA AGREGAR DATOS  (CREATE) ########################
#---------------------------------------------------------------------------------------    

#pacientes
def newPaciente(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            paciente = pacientes(
            id_paciente = data['id_paciente'], #?
            nombre = data['nombre'],
            direccion= data['direccion'],
            telefono= data['telefono'],
            contacto = data['contacto'],
            telefono_contacto = data['telefono_contacto']
            )
            paciente.save()
            return HttpResponse("nuevo paciente agregado")
        except:
            HttpResponseBadRequest ("error en los datos enviados")
    else:
        HttpResponseNotAllowed (['POST'], 'metodo invalido')

# medicos

def newMedico(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            medico = medicos(
            id_medico = data['id_medico'], #?
            nombre = data['nombre'],
            direccion= data['direccion'],
            telefono= data['telefono'],
            especialidad = data['especialidad']
            )
            medico.save()
            return HttpResponse("nuevo medico agregado")
        except:
            HttpResponseBadRequest ("error en los datos enviados")
    else:
        HttpResponseNotAllowed (['POST'], 'metodo invalido')   

# signos vitales

def newSigno(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            signo_vital = signos_vitales(
            descripcion = data['descripcion'],
            valor_maximo= data['valor_maximo'],
            valor_minimo= data['valor_minimo'],
            recomendacion = data['recomendacion']
            )
            signo_vital.save()
            return HttpResponse("nuevo signo vital agregado")
        except:
            HttpResponseBadRequest ("error en los datos enviados")
    else:
        HttpResponseNotAllowed (['POST'], 'metodo invalido')          


#historia clinica

def newHistoriaClinica(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pac = pacientes.objects.filter(id_paciente = data["id_paciente"]).first() # se trae el id del paciente que queremos
            med = medicos.objects.filter(id_medico = data["id_medico"]).first() # se trae el id del paciente que queremos
            historia_clica = historias_clinicas(
            fecha= datetime.datetime.now(), #?
            id_paciente = pac,
            id_medico= med,          
            observaciones = data['observaciones'],
            recomendaciones = data['recomendaciones']
            )
            historia_clica.save()
            return HttpResponse("nuevo historia clinica agragada")
        except:
            HttpResponseBadRequest ("error en los datos enviados")
    else:
        HttpResponseNotAllowed (['POST'], 'metodo invalido')          

# historia signos

def newHistoriaSigno(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            pac = pacientes.objects.filter(id_paciente = data["id_paciente"]).first() # se trae el id del paciente que queremos
            sig = signos_vitales.objects.filter(id_signo = data["id_signo"]).first() # se trae el id de signo que queremos
            historia_signo = historias_signos(
            fecha= datetime.datetime.now(), #?
            id_paciente = pac,
            id_signo= sig,            
            valor_signo = data['valor_signo']            
            )
            historia_signo.save()
            return HttpResponse("nuevo historia signo agragada")
        except:
            HttpResponseBadRequest ("error en los datos enviados")
    else:
        HttpResponseNotAllowed (['POST'], 'metodo invalido')               



#---------------------------------------------------------------------------------------    
########################### VISTAS PARA LEER DATOS  (READ) #############################
#---------------------------------------------------------------------------------------    

# pacientes
def getAllPacientes(request):
    if request.method == 'GET':
        paciente = pacientes.objects.all()
        if (not paciente):
            return HttpResponseBadRequest("No hay clientes en la base de datos.")

        allCustData = []
        for x in paciente:
            data = {"id_paciente": x.id_paciente, "nombre": x.nombre, "direccion": x.direccion, 
            "telefono": x.telefono, "contacto":x.contacto, "telefono_contacto":x.telefono_contacto }
            allCustData.append(data)
        dataJson = json.dumps(allCustData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")

# medicos
def getAllMedicos(request):
    if request.method == 'GET':
        medico = medicos.objects.all()
        if (not medico):
            return HttpResponseBadRequest("No hay clientes en la base de datos.")
        allCustData = []
        for x in medico:
            data = {"id_medico": x.id_medico, "nombre": x.nombre, "direccion": x.direccion, 
            "telefono": x.telefono, "especialidad":x.especialidad }
            allCustData.append(data)
        dataJson = json.dumps(allCustData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


# medicos
def getAllSignos(request):
    if request.method == 'GET':
        signo_vital = signos_vitales.objects.all()
        if (not signo_vital):
            return HttpResponseBadRequest("No hay clientes en la base de datos.")
        allCustData = []
        for x in signo_vital:
            data = {"id_signo": x.id_signo, "descripcion": x.descripcion, "valor_maximo": x.valor_maximo, 
            "valor_minimo": x.valor_minimo, "recomendacion":x.recomendacion }
            allCustData.append(data)
        dataJson = json.dumps(allCustData)
        #print(dataJson)
        resp = HttpResponse()
        resp.headers['Content-Type'] = "text/json"
        resp.content = dataJson
        return resp
    else:
        return HttpResponseNotAllowed(['GET'], "Método inválido")


  

#---------------------------------------------------------------------------------------    
########################### VISTAS PARA ACTUALIZAR DATOS  (UPDATE) #############################
#---------------------------------------------------------------------------------------    

# pacientes

def updatePaciente(request, id_paciente):
    if request.method == 'PUT':
        try:
            paciente = pacientes.objects.filter(id_paciente = id_paciente).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe el paciente con este id_paciente.")

            data = json.loads(request.body)
            paciente.nombre = data["nombre"]
            paciente.direccion = data["direccion"]
            paciente.telefono = data["telefono"]
            paciente.contacto = data["contacto"]
            paciente.telefono_contacto = data["telefono_contacto"]
            paciente.save()
            return HttpResponse("paciente actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

# medicos 

def updateMedico(request, id_medico):
    if request.method == 'PUT':
        try:
            medico = medicos.objects.filter(id_medico = id_medico).first()
            if (not medico):
                return HttpResponseBadRequest("No existe el medico con este id_medico.")

            data = json.loads(request.body)
            medico.nombre = data["nombre"]
            medico.direccion = data["direccion"]
            medico.telefono = data["telefono"]
            medico.especialidad = data["especialidad"]
            medico.save()
            return HttpResponse("medico actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

# signos vitales 

def updateSigno(request, id_signo):
    if request.method == 'PUT':
        try:
            signo = signos_vitales.objects.filter(id_signo = id_signo).first()
            if (not signo):
                return HttpResponseBadRequest("No existe el signo vital con este id_signo.")

            data = json.loads(request.body)
            signo.descripcion = data["descripcion"]
            signo.valor_maximo = data["valor_maximo"]
            signo.valor_minimo = data["valor_minimo"]
            signo.recomendacion = data["recomendacion"]
            signo.save()
            return HttpResponse("signo vital actualizado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['PUT'], "Método inválido")

#---------------------------------------------------------------------------------------    
######################## VISTAS PARA ELIMINAR DATOS  (DELETE) ###########################
#---------------------------------------------------------------------------------------    

# pacientes
def deletePaciente(request, id_paciente):
    if request.method == 'DELETE':
        try:
            paciente = pacientes.objects.filter(id_paciente = id_paciente).first()
            if (not paciente):
                return HttpResponseBadRequest("No existe no existe el paciente con este id_paciente.")
            paciente.delete()
            return HttpResponse("paciente eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")


# medicos
def deleteMedico(request, id_medico):
    if request.method == 'DELETE':
        try:
            medico = medicos.objects.filter(id_medico = id_medico).first()
            if (not medico):
                return HttpResponseBadRequest("No existe no existe el medico con este id_medico.")
            medico.delete()
            return HttpResponse("medico eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")


# signos vitales
def deleteSigno(request, id_signo):
    if request.method == 'DELETE':
        try:
            signo = signos_vitales.objects.filter(id_signo = id_signo).first()
            if (not signo):
                return HttpResponseBadRequest("No existe no existe el signo con este id_signo.")
            signo.delete()
            return HttpResponse("signo eliminado")
        except:
            return HttpResponseBadRequest("Error en los datos enviados")
    else:
        return HttpResponseNotAllowed(['DELETE'], "Método inválido")