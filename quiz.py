#!/usr/bin/env python3
#By perlaa.rmn@gmail.com
#GNU/GLP License

#Simple quiz
def validate_True_False(text):
    text=text.lower()
    if ("falso" in text) or ("verdadero" in text):
        return True
        #print("Respuesta valida")
    else:
        return False

print("¿El sol y la luna tienen el mismo radio aparente en un eclipse total del Sol?")
print("[Falso/Verdadero]")

answer=False

while not answer:
    text=input(">")
    text=text.lower()
    if validate_True_False(text):
        answer=True
        if "verdadero" in text:
            print("¡Respuesta correcta!")
        else:
            print("¡Respuesta incorrecta!")
    else:
        answer=False