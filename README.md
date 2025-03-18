Go to [English version](#english-version)
# Ogólne informacje
Projekt realizuje implementację "Gry w życie" Conwaya, z interfejsem graficznym Pygame. 
Aplikacja umożliwia symulację automatu komórkowego z różnymi predefiniowanymi wzorcami (glider, oscylator, 
niezmienny, oscylator prosty, oscylator zabka, losowy), dwoma warunkami brzegowymi (periodyczny oraz 
odbicia). Całość jest interaktywna, w czasie działania programu można ciągłe zmieniać wzorzec oraz warunki 
brzegowe.

# Technologie
W kodzie użyto:
* Python 3.12
* NumPy 2.2.2
* Pygame 2.6.0
* moduł `time`
	
# Wykorzystanie
Kod był uruchamiany i napisany w środowisku PyCharm. Struktura kodu składa się 
z funkcji `draw_buttons` odpowiedzialnej za przyciski interaktywne, `check_button_click` 
obsługującej kliknięcie przycisków, `ss_lst`, `update_lst`, `update_rules` odpowiadających 
za obliczanie liczby sąsiadów oraz aktualizację stanu planszy w zależności od bieżacych warunków 
brzegowych, `stan_glider`, `stan_niezmienny`, `stan_oscylator`, `stan_oscylator_zab`, `stan_losowy` 
definiujących kształty struktur (stan losowy wypełnia planszę losowymi wartościami) oraz `main` 
gdzie ma miejsce inicjalizacja Pygame, aktualizacja stanu planszy, konstrukcja interfejsu graficznego, 
obsługa zdarzeń.

## Wzorzec glider
<img width="852" alt="image" src="https://github.com/user-attachments/assets/552a661d-7873-4e34-a037-933ed73ec944" />

## Wzorzec niezmienny
<img width="845" alt="image" src="https://github.com/user-attachments/assets/695ddb18-060e-4187-8373-4315098cbf63" />

## Stan losowy z warunkiem brzegowym periodycznym
<img width="847" alt="image" src="https://github.com/user-attachments/assets/75e8db90-b0ee-48b1-b4d5-f3211e233bc6" />



# English version

# General Information   
The project implements the implementation of Conway's "Game of Life" with a Pygame graphical interface. 
The application enables simulation of a cellular automaton with various predefined patterns (glider, oscillator, 
static, simple oscillator, toad oscillator, random), two boundary conditions (periodic and reflection). The 
entire system is interactive; during program execution, patterns and boundary conditions can be continuously changed.  


# Technologies  
The code uses:  
* Python 3.12
* NumPy 2.2.2
* Pygame 2.6.0
* `time` module

# Usage 
The code was run and written in the PyCharm environment. The code structure consists of the function `draw_buttons` 
responsible for interactive buttons, `check_button_click` handling button clicks, `ss_lst`, `update_lst`, `update_rules` 
responsible for calculating the number of neighbors and updating the board state based on current boundary conditions, 
`stan_glider`, `stan_niezmienny`, `stan_oscylator`, `stan_oscylator_zab`, `stan_losowy` defining the shapes of structures 
(the random state fills the board with random values), and `main` where Pygame initialization, board state updates, 
graphical interface construction, and event handling take place.  

## Glider pattern
<img width="852" alt="image" src="https://github.com/user-attachments/assets/552a661d-7873-4e34-a037-933ed73ec944" />

## Unchanging pattern
<img width="845" alt="image" src="https://github.com/user-attachments/assets/695ddb18-060e-4187-8373-4315098cbf63" />

## Random state with periodic boundary condition
<img width="847" alt="image" src="https://github.com/user-attachments/assets/75e8db90-b0ee-48b1-b4d5-f3211e233bc6" />
