import RPi.GPIO as GPIO
import time
import random

#ruan é a maior baitola desse universo! 😁

# Setup
GPIO.setmode(GPIO.BCM)

# GPIOs dos LEDs
LED_VERDE = 18
LED_VERMELHO = 23
LED_AZUL = 24
LED_AMARELO = 25

# GPIOs dos Botões
BTN_VERDE = 4
BTN_VERMELHO = 17
BTN_AZUL = 27
BTN_AMARELO = 22

# Configurar LEDs
GPIO.setup(LED_VERDE, GPIO.OUT)
GPIO.setup(LED_VERMELHO, GPIO.OUT)
GPIO.setup(LED_AZUL, GPIO.OUT)
GPIO.setup(LED_AMARELO, GPIO.OUT)

# Configurar Botões
GPIO.setup(BTN_VERDE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_VERMELHO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_AZUL, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(BTN_AMARELO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Acende o LED correspondente à cor
def acende_led(cor):
    if cor == "verde":
        GPIO.output(LED_VERDE, True)
    elif cor == "vermelho":
        GPIO.output(LED_VERMELHO, True)
    elif cor == "azul":
        GPIO.output(LED_AZUL, True)
    elif cor == "amarelo":
        GPIO.output(LED_AMARELO, True)

# Apaga todos os LEDs
def apaga_leds():
    GPIO.output(LED_VERDE, False)
    GPIO.output(LED_VERMELHO, False)
    GPIO.output(LED_AZUL, False)
    GPIO.output(LED_AMARELO, False)

# Pisca LED de uma cor
def pisca_led(cor):
    acende_led(cor)
    time.sleep(0.5)
    apaga_leds()
    time.sleep(0.3)

# Gera uma cor aleatória
def gerar_cor():
    numero = random.randint(1, 4)
    if numero == 1:
        return "verde"
    elif numero == 2:
        return "vermelho"
    elif numero == 3:
        return "azul"
    else:
        return "amarelo"

# Lê a cor pressionada pelo jogador
def ler_cor():
    while True:
        if GPIO.input(BTN_VERDE) == 0:
            pisca_led("verde")
            return "verde"
        elif GPIO.input(BTN_VERMELHO) == 0:
            pisca_led("vermelho")
            return "vermelho"
        elif GPIO.input(BTN_AZUL) == 0:
            pisca_led("azul")
            return "azul"
        elif GPIO.input(BTN_AMARELO) == 0:
            pisca_led("amarelo")
            return "amarelo"
        time.sleep(0.05)

# Mostra sequência
def mostrar_sequencia(cor1, cor2, cor3, tamanho):
    if tamanho >= 1:
        pisca_led(cor1)
    if tamanho >= 2:
        pisca_led(cor2)
    if tamanho >= 3:
        pisca_led(cor3)

# Compara sequências
def comparar(cor_digitada1, cor_digitada2, cor_digitada3, cor1, cor2, cor3, tamanho):
    if tamanho >= 1 and cor_digitada1 != cor1:
        return False
    if tamanho >= 2 and cor_digitada2 != cor2:
        return False
    if tamanho >= 3 and cor_digitada3 != cor3:
        return False
    return True

# Programa principal
try:
    print("Bem-vindo ao SIMON!")
    cor1 = gerar_cor()
    cor2 = gerar_cor()
    cor3 = gerar_cor()
    rodada = 1

    while True:
        print("Rodada:", rodada)
        mostrar_sequencia(cor1, cor2, cor3, rodada)

        print("Sua vez...")
        cor_digitada1 = ""
        cor_digitada2 = ""
        cor_digitada3 = ""

        if rodada >= 1:
            cor_digitada1 = ler_cor()
        if rodada >= 2:
            cor_digitada2 = ler_cor()
        if rodada >= 3:
            cor_digitada3 = ler_cor()

        resultado = comparar(cor_digitada1, cor_digitada2, cor_digitada3, cor1, cor2, cor3, rodada)

        if resultado == True:
            print("Correto!")
            rodada = rodada + 1
            if rodada > 3:
                print("Parabéns, você venceu!")
                break
        else:
            print("Errado! Fim de jogo.")
            break

        time.sleep(1)

except KeyboardInterrupt:
    print("Jogo interrompido.")

finally:
    GPIO.cleanup()
    print("GPIO liberado.")