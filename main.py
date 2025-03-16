import numpy as np
import pygame
import time

#Ustawienia planszy
width = 200
height = 200
cell_s = 4
sc_width = width*cell_s + 50
sc_height = width*cell_s + 100


def draw_buttons(screen, font):
    buttons = [
        ("Warunek periodyczny", (10, sc_height - 80)),
        ("Warunek odbicia", (160, sc_height - 80)),
        ("Glider", (280, sc_height - 80)),
        ("Niezmienny", (350, sc_height - 80)),
        ("Oscylator Prosty", (450, sc_height - 80)),
        ("Oscylator Zabka", (580, sc_height - 80)),
        ("Losowy", (700, sc_height - 80))
    ]

    #Rysowanie ramki
    for text, pos in buttons:
        pygame.draw.rect(screen, (50, 50, 50), (pos[0] - 2, pos[1] - 2, 154, 54))
        pygame.draw.rect(screen, (200, 200, 200), (pos[0], pos[1], 150, 50))
        #Tekst przycisku
        screen.blit(font.render(text, True, (0, 0, 0)), (pos[0] + 10, pos[1] + 15))

    return buttons


#Sprawdź kliknięcie
def check_button_click(pos, buttons):
    click_x, click_y = pos
    button_width, button_height = 150, 50

    for i, (_, (btn_x, btn_y)) in enumerate(buttons):
        if btn_x <= click_x <= btn_x + button_width and btn_y <= click_y <= btn_y + button_height:
            return i
    return None

def ss_lst(siatka, x, y):
    sum = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue #Omiń 0 0
            pi = x+i
            pj = y + j

            if pi <0:
                pi = 0
            elif pi >= width:
                pi = width -1

            if pj < 0:
                pj = 0
            elif pj >= height:
                pj = height - 1

            sum += siatka[pi, pj]
    return sum

def update_lst(siatka):
    up_siatka = np.copy(siatka)
    for x in range(width):
        for y in range(height):
            sum_sasiedzi = ss_lst(siatka, x, y)

            if siatka[x, y] == 1:
                if sum_sasiedzi < 2 or sum_sasiedzi > 3:
                    up_siatka[x,y] = 0
            elif siatka[x, y] == 0:
                if sum_sasiedzi == 3:
                    up_siatka[x, y] = 1
    return up_siatka


def update_rules(siatka):
    up_siatka = np.copy(siatka)
    for x in range(width):
        for y in range(height):
            #Oblicz liczbę sąsiadów
            sum_sasiedzi = (
                siatka[(x-1) % width, (y-1) % height]+
                siatka[(x)% width, (y-1)% height]+
                siatka[(x+1)%width, (y-1)%height]+
                siatka[(x+1)%width, y%height]+
                siatka[(x+1)%width, (y+1)%height]+
                siatka[(x)%width, (y+1)%height]+
                siatka[(x - 1) % width, (y + 1) % height]+
                siatka[(x - 1) % width, (y) % height]
            )
            if siatka[x,y] == 1:
                if sum_sasiedzi <2 or sum_sasiedzi>3:
                    up_siatka[x,y] = 0
            elif siatka[x,y] == 0:
                if sum_sasiedzi == 3:
                    up_siatka[x,y] = 1
    return up_siatka

def stan_glider(siatka, x, y):
    pozycja = [(x, y), (x+1, y), (x+1, y+1), (x+2,y+1), (x+2, y-1)]
    for i,j in pozycja:
        siatka[i%width,j%height]=1

def stan_niezmienny(siatka, x, y):
    pozycja = [(x,y), (x+1,y+1), (x+2,y+1),(x+3,y),(x+2,y-1),(x+1,y-1)]
    for i,j in pozycja:
        siatka[i%width,j%height]=1

def stan_oscylator_pr(siatka, x, y):
    pozycja = [(x,y), (x,y-1), (x,y-2)]
    for i,j in pozycja:
        siatka[i%width,j%height]=1

def stan_oscylator_zab(siatka, x, y):
    pozycja = [(x, y), (x+1, y), (x+2, y), (x+1, y+1), (x+2, y+1), (x+3, y+1)]
    for i,j in pozycja:
        siatka[i%width,j%height]=1

def stan_losowy(siatka):
    siatka[:] = np.random.choice([0,1], size=siatka.shape)

def main():
    #Inicjalizacja Pygame
    pygame.init()
    sc = pygame.display.set_mode((sc_width, sc_height))
    pygame.display.set_caption("Gra w życie")
    font = pygame.font.SysFont(None, 18)

    siatka = np.zeros((width, height), dtype=int)
    c_up = update_lst
    st_state = stan_glider
    st_state(siatka, 10, 20)

    #Pętla programu
    run = True
    while run:
        sc.fill((255, 255, 255))

        buttons = draw_buttons(sc, font)

        for x in range(width):
            for y in range(height):
                cl = (245, 211, 144) if siatka[x,y] == 1 else (255, 255, 255)
                pygame.draw.rect(sc, cl, (x*cell_s, y*cell_s, cell_s, cell_s))

        siatka = c_up(siatka)

        pygame.display.flip()
        time.sleep(0.0000005)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                index = check_button_click(event.pos, buttons)

                if index == 0:
                    c_up = update_rules
                elif index == 1:
                    c_up = update_lst
                elif index == 2:
                    siatka.fill(0)
                    state = stan_glider
                    state(siatka, 20, 20)
                elif index == 3:
                    siatka.fill(0)
                    state = stan_niezmienny
                    state(siatka, 20, 20)
                elif index == 4:
                    siatka.fill(0)
                    state = stan_oscylator_pr
                    state(siatka, 20, 20)
                elif index == 5:
                    siatka.fill(0)
                    state = stan_oscylator_zab
                    state(siatka, 20, 20)
                elif index == 6:
                    siatka.fill(0)
                    state = stan_losowy
                    state(siatka)
    pygame.quit()

main()
