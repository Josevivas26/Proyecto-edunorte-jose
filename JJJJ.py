import datetime as dt

def miproblema(num1,num2,num3):
    dim=num1+num2
    potencia=dim**num3
    return potencia

def pensiones(fnac,genero):
    hhh=dt.datetime.now()
    fecha=dt.datetime.strftime(fnac,"%d/%m/%Y")
    edad=hhh-fecha
    edad=round(edad.days)





















