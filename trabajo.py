def hacer_diccionario(lista_diccionario):
    region_dicion={}
    for diccionario in lista_diccionario:
        for i in diccionario:
            if i not in region_dicion:
                region_dicion[i] =[]
            region_dicion[i].append(diccionario[i])
    return region_dicion

def hacer_lista_diccionario(lista):
    Lista_Dicionario =[]
    for i in lista:
        region= i[1]
        mes_año=i[0].split("-")
        porcentaje=int(i[3])*100/int(i[2])
        redondeo=round(porcentaje,2)
        total =int(i[2])
        datos={region:(mes_año,redondeo,total)}
        Lista_Dicionario.append(datos)
    return Lista_Dicionario

def avistamientos_por_región(nombre_archivo):
    Archivo_original=open(nombre_archivo)
    Lista_Lineas=[]
    for i in Archivo_original:
        datos = i.split(";")
        Lista_Lineas.append(datos)
    Lista_Lineas.pop(0)
    Lista_diccionarios =hacer_lista_diccionario(Lista_Lineas)
    Parte_final_dicio =hacer_diccionario(Lista_diccionarios)
    for i in Parte_final_dicio:
        Parte_final_dicio[i].sort(key=lambda porcentaje:porcentaje[1],reverse=True)
    archivos_creados =archivos(Parte_final_dicio)
    Archivo_original.close()
    return archivos_creados

def archivos(diccionario):
    x=0
    for region in diccionario:
        detenerse =False
        archivo=open(region+".txt","w")
        i=0
        if len(diccionario[region]) >=3:
            while i < 3:
                mensaje = "En el mes {} de {} hubo {} % de avistamientos confirmados de un total de {}\n"
                archivo.write(mensaje.format(diccionario[region][i][0][1], diccionario[region][i][0][0], diccionario[region][i][1], diccionario[region][i][2]))
                i = i+1
            archivo.close()
        if len(diccionario[region]) <=2:
            while i < len(diccionario[region]):
                mensaje = "En el mes {} de {} hubo {} % de avistamientos confirmados de un total de {}\n"
                archivo.write(mensaje.format(diccionario[region][i][0][1], diccionario[region][i][0][0], diccionario[region][i][1], diccionario[region][i][2]))
                i = i+1
            archivo.close()
        x = x+1
    return x

print(avistamientos_por_región("ovnis_grande.csv"))
