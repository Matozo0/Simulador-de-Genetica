import pygame, pgzero, pgzrun, random, statistics, numpy
from genetica import Pessoa

WIDTH = 1300
HEIGHT = 650
#   Generos: masc, fem
#   Tipos de cabelo MASC: curto, medio, longo, americano
#   Tipos de cabelo FEM: rabo, sidecut, solto, black
#   Cores de cabelo: ruivo, castanho, loiro
#   Cores de olhos: azul, castanho, verde

carlos = Pessoa('masc','azul','curto','castanho',0.6, 0.3)
juliana = Pessoa('fem','castanho','solto','castanho',0.4,0.4)

def draw():
    global filho
    screen.fill((255,255,255))
    desenharpessoa(carlos, WIDTH/2-200, HEIGHT/2)
    desenharpessoa(juliana, WIDTH/2-100, HEIGHT/2)
    dedodeDeus(carlos, juliana)
    desenharpessoa(filho, 800, HEIGHT/2)

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

pgzrun.go()