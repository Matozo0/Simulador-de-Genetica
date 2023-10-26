import pygame, pgzero, pgzrun, random, statistics, os
from genetica import Pessoa, PessoaRANDOM

WIDTH = 1700
HEIGHT = 800
x = 10000
y = 0
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#   Generos: masc, fem
#   Tipos de cabelo MASC: curto, medio, longo, americano
#   Tipos de cabelo FEM: rabo, sidecut, solto, black
#   Cores de cabelo: ruivo, castanho, loiro
#   Cores de olhos: azul, castanho, verde

pessoas_masc = {}
pessoas_fem = {}
frame_m = 0
frame_f = 0

fundo = Actor('fundo.png')
for i in range(0,4):
    pessoas_masc[i] = PessoaRANDOM('masc')
    pessoas_fem[i] = PessoaRANDOM('fem')

def draw():
    global filho
    screen.fill((255,255,255))
    fundo.draw()
    for i in range(0,3):
        desenharpessoa(pessoas_masc[i], 221+(256*i), 339)
        desenharpessoa(pessoas_fem[i], 221+(256*i), 624)
    dedodeDeus(pessoas_masc[2], pessoas_fem[1])
    desenharpessoa(filho, 1400, HEIGHT/2)
    print(frame_f)

def desenharpessoa(pessoa, x, y):
    Olho = Actor('olho_'+pessoa.corolho)
    Olho.pos = (x,y)
    Olho.draw()
    Genero = Actor(pessoa.genero)
    Genero.pos = (x,y)
    Genero.draw()
    Cabelo = Actor(pessoa.genero+'_'+pessoa.tipocabelo+'_'+pessoa.corcabelo)
    Cabelo.pos = (x,y)
    Cabelo.draw()

def dedodeDeus(homem, mulher):
    global filho
    if (homem.p_cabelo > mulher.p_cabelo):
        genero = homem.genero
        tipocabelo = homem.tipocabelo
        corcabelo = homem.corcabelo
    if (mulher.p_cabelo >= homem.p_cabelo):
        genero = mulher.genero
        tipocabelo = mulher.tipocabelo
        corcabelo = mulher.corcabelo
    if (homem.p_olho > mulher.p_olho):
        corolho = homem.corolho
    if (mulher.p_olho >= homem.p_olho):
        corolho = mulher.corolho
    filho = Pessoa(genero, corolho, tipocabelo, corcabelo, 0.0, 0.0)
    
def update():
    pass

def on_mouse_down(pos):
    if pessoas_masc[0].collidepoint(pos):
        frame_m = 1
    if pessoas_masc[1].collidepoint(pos):
        frame_m = 2
    if pessoas_masc[2].collidepoint(pos):
        frame_m = 3
    if pessoas_masc[3].collidepoint(pos):
        frame_m = 4
    if pessoas_fem[0].collidepoint(pos):
        frame_f = 1
    if pessoas_fem[1].collidepoint(pos):
        frame_f = 2
    if pessoas_fem[2].collidepoint(pos):
        frame_f = 3
    if pessoas_fem[3].collidepoint(pos):
        frame_f = 4

pgzrun.go()