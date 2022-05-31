calificacion = input("intruduce tu calificacion del AZ 900:")

calificacion=int(calificacion)

if calificacion < 700:
    print("Vees, por no estudiar, ni modo")
    
elif calificacion > 1000:
    print("Mientes!, no puedes sacar mas de mill")

else:
    print("felicidades pasas por tu certificado")
    
    
edad =input("Introduce tu edad")

edad=int(edad)

if edad >= 18 and edad <=100:
    print("Bienvenido al mamitas")
elif edad >100:
    print("Si vienes acompañado de tus abuelitos,si te podemos fiar")
elif edad < 0:
    print("Ni que fueras viajero del tiempo")    
else:
    print("No puedes llevarte esos cigarros")