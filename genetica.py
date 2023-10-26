import pygame, random

class Pessoa:
   def __init__(self, genero, corolho, tipocabelo, corcabelo, p_cabelo, p_olho):
    self.genero = genero
    self.corolho = corolho
    self.tipocabelo = tipocabelo
    self.corcabelo = corcabelo
    self.p_cabelo = p_cabelo
    self.p_olho = p_olho
   
class PessoaRANDOM:
   def __init__(self, genero):
    self.genero = genero
    if genero == 'masc':
       tipocabelo = random.choice(['curto', 'medio', 'longo', 'americano'])
    else:
       tipocabelo = random.choice(['rabo', 'sidecut', 'solto', 'black'])
    self.corolho = random.choice(['azul', 'castanho','verde'])
    self.tipocabelo = tipocabelo
    self.corcabelo = random.choice(['ruivo', 'castanho','loiro'])
    self.p_cabelo = random.uniform(0.2,0.6)
    self.p_olho = random.uniform(0.2,0.6)