#Conectar los módulos requeridos
import pygame
from random import randint
pygame.init()
#Crear una ventana de juego
clock = pygame.time.Clock()
back = (255, 255, 255) #color de fondo
mw = pygame.display.set_mode((500, 500)) #ventana principal
mw.fill(back)
#colores
BLACK = (0, 0, 0)
LIGHT_BLUE = (200, 200, 255)
class TextArea():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height)
      self.fill_color = color
      #etiquetas posibles
      self.titles = list()
 
 
  #añadir texto a la lista de etiquetas posibles
  def add_text(self, text):
      self.titles.append(text)
 
 
  #colocar texto
  def set_text(self, number=0, fsize=12, text_color=BLACK):
      self.text = self.titles[number]
      self.image = pygame.font.Font(None, fsize).render(self.text, True, text_color)
 
  #dibujar un rectángulo con texto
  def draw(self, shift_x=0, shift_y=0):
      pygame.draw.rect(mw, self.fill_color, self.rect)
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  
#crear tarjetas
quest_card = TextArea(120, 100, 290, 70, LIGHT_BLUE)
quest_card.add_text('Pregunta')
quest_card.add_text('¿Qué estudias en Algorithmics?')
quest_card.add_text('¿Qué idioma se habla en Francia?')
quest_card.add_text('¿Qué crece en un manzano?')
quest_card.add_text('¿Qué cae del cielo cuando llueve?')
quest_card.add_text('¿Qué van a comer para la cena?')
quest_card.set_text(0, 75)
ans_card = TextArea(120, 240, 290, 70, LIGHT_BLUE)
ans_card.add_text('Respuesta')
ans_card.add_text('Python')
ans_card.add_text('Francés')
ans_card.add_text('Manzanas')
ans_card.add_text('Gotas de lluvia')
ans_card.add_text('Un asado con champiñones')
ans_card.set_text(0, 75)
quest_card.draw(10,10)
ans_card.draw(10,10)
 
 
while 1:
  pygame.display.update()
  for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
              num = randint(1, len(quest_card.titles)-1)   
              quest_card.set_text(num, 25)
 
 
              quest_card.draw(10,25)
          if event.key == pygame.K_a:
              num = randint(1, len(ans_card.titles)-1) 
              ans_card.set_text(num, 25)
 
 
              ans_card.draw(10, 25)
  clock.tick(40)