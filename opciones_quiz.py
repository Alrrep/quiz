#!/usr/bin/env python3
#By perlaa.rmn@gmail.com
#GNU/GLP License

#Simple quiz
def validate_True(text):
    text=text.lower()
    if ("morado" in text) or ("verde" in text) or ("rosa" in text) or ("azul" in text):
        return True
    else:
        return False

print("¿Cuál es tu color favorito?")
print("Morado")
print("Verde")
print("Rosa")
print("Azul")

answer=False

while not answer:
    text=input(">")
    text=text.lower()
    if validate_True(text):
        answer=True
        if "morado" in text:
            print("¡Respuesta correcta!")
        else:
            print("¡Respuesta incorrecta!")
    else:
        answer=False