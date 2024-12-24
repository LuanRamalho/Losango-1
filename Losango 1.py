import turtle
import random

def desenha_losango(tamanho):
    # Gera uma cor aleatória (valores RGB entre 0 e 1)
    cor = (random.random(), random.random(), random.random())
    
    # Configura a cor de preenchimento
    turtle.fillcolor(cor)
    turtle.begin_fill()
    
    # Desenha o losango
    for _ in range(2):
        turtle.forward(tamanho)
        turtle.left(60)
        turtle.forward(tamanho)
        turtle.left(120)
    
    turtle.end_fill()

def main():
    # Configura a tela
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Desenhando um Losango Aleatório")
    
    # Configura a tartaruga
    turtle.speed(5)
    
    # Desenha o losango
    desenha_losango(100)
    
    # Finaliza o programa ao clicar na tela
    screen.mainloop()

if __name__ == "__main__":
    main()
