print("testando...")

import speech_recognition as sr

import os

#Função para ouvir e reconhecer a fala
def ouvir_microfone():
    #Habilita o microfone do usuario
    microfone = sr.Recognizer()

    #usando o microfone
    with sr.Microphone() as source:

        #chama um algoritimo de redução de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        #Frase para o usuario dizer algo
        print("Diga alguma coisa: ")

        #Armazena o que foi dito numa variavel
        audio = microfone.listen(source)

    try:

        #passa a variavel para o algoritimo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language='pr-BR')

        if "Excel" in frase:
            os.system("start Excel.exe")
            return False
        
        elif "PowerPoint" in frase:
            os.system("start PowerPoint.exe")
            return False

        elif "Fechar" in frase:
            os.system("exit")
            return True
        
        #retorna a frase pronunciada
        print("Você disse :" + frase)

    except sr.UnknownValueError:
        print("Não entendi, pfvg repita")

    return frase

while True:
    if ouvir_microfone():
        break