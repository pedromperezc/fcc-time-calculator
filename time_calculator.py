def add_time(start, duration,*ars):

    dia_semana = str(ars)
    dia_semana_int = 0
    dia = ["Monday", "Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    dias_adicionales = 0
    dia_imprmo = 1
    meridiano = ''
    if dia_semana != "()":
        print (type(dia_semana))
        dia_semana = dia_semana.upper()
        
        if dia_semana.find("MONDAY") > -1:
            dia_semana_int = 1
        elif dia_semana.find("TUESDAY") >-1:
            dia_semana_int = 2
        elif dia_semana.find("WEDNESDAY") >-1:
            dia_semana_int = 3
        elif dia_semana.find("THURSDAY")>-1:
            dia_semana_int = 3
        elif dia_semana.find( "FRAIDAY")>-1:
            dia_semana_int = 5
        elif dia_semana.find("SATURDAY") >-1:
            dia_semana_int = 6
        elif dia_semana.find("SUNDAY") > -1:
            dia_semana_int = 7
    else:
        dia_imprmo = 0
        
    if start.find('PM') > -1 :
        posicion  = start.find (":")
        s_hora = int(start[:posicion]) + 12
        s_minutos = int(start [posicion+1:posicion+3])
        meridiano = 'PM'
    else:
        posicion  = start.find (":")
        s_hora = int(start[:posicion]) 
        s_minutos = int(start [posicion+1:posicion+3])
        meridiano = 'AM'

    posicion =  duration.find (":")   
    d_hora = int(duration[:posicion])   
    d_minutos = int(duration [posicion+1:posicion+3])
    d_total_minutos = (d_hora * 60) + d_minutos
    
    #sumo el total de minutos a los minutos
    suma_minutos = s_minutos + d_total_minutos
    
    #verifico si tengo que mover la hora
    if suma_minutos > 60:
        #Caulculo el numero de horas a sumar
        horas_sumar = suma_minutos // 60
        hora_final = s_hora + horas_sumar
        
        #calculo el numero minutos a sumar
        minuto_final = suma_minutos % 60
        
        #verifico si tengo que mover el día
        if hora_final >= 24:
            dias_adicionales = hora_final // 24
            hora_final = hora_final % 24
            dia_semana_total = dia_semana_int + dias_adicionales
            if dia_semana_total > 7:
                dia_semana_int = dia_semana_total % 7
            else:
                dia_semana_int = dia_semana_total 
    else:
        hora_final = s_hora
        minuto_final = suma_minutos
    #convierto a formato hora:
    if hora_final == 12  and meridiano =='PM':
        hora_final = str(hora_final)
        meridian = 'AM'
    elif hora_final == 12 and meridiano == 'AM':
        hora_final = str(hora_final)
        meridian = 'PM'
    elif hora_final > 12:
        hora_final = str(hora_final -12)
        meridian = 'PM'
    elif hora_final == 0:
        hora_final = str(hora_final + 12)
        meridian = 'AM'
    else:
        hora_final = str(hora_final)
        meridian = 'AM'
    if minuto_final < 10:
        minuto_final = str(minuto_final).zfill(2)

    string = hora_final + ":" +  str(minuto_final) + " " + meridian
    if dia_imprmo == 1:
        string = string + ", " + dia[dia_semana_int - 1]
    
    if dias_adicionales == 1:
        dias_adicionales = str(dias_adicionales)
        string = string + " (next day)"

    if int(dias_adicionales) > 1:
        dias_adicionales = str(dias_adicionales)
        string = string + " (" + dias_adicionales +" days later)"
    return string

