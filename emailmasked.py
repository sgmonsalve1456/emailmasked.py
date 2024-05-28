def enmascarar_correo(correo):
    # Divide la dirección de correo en nombre de usuario y dominio
    nombre_usuario, dominio = correo.split('@')
    
    # Enmascarar el nombre de usuario
    if len(nombre_usuario) < 3:
        nombre_enmascarado = nombre_usuario[0] + '*' * (len(nombre_usuario) - 1)
    elif len(nombre_usuario) <= 6:
        nombre_enmascarado = nombre_usuario[0] + '*' * (len(nombre_usuario) - 2) + nombre_usuario[-1]
    else:
        nombre_enmascarado = nombre_usuario[:2] + '*' * (len(nombre_usuario) - 4) + nombre_usuario[-2:]
    
    # Reconstruir la dirección de correo enmascarada
    correo_enmascarado = nombre_enmascarado + '@' + dominio
    
    return correo_enmascarado

while True:
    # Solicitar al usuario que ingrese un correo electrónico
    correo = input("Por favor, ingresa el correo electrónico que deseas enmascarar (o 'exit' para salir): ")
    
    if correo.lower() == 'exit':
        print("Saliendo del programa...")
        break
    
    # Enmascarar el correo ingresado
    correo_enmascarado = enmascarar_correo(correo)
    
    # Mostrar el resultado
    print("Correo enmascarado:", correo_enmascarado)
    print()  # Salto de línea para mejor legibilidad en la consola
