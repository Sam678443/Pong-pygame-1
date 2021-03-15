import pygame, sys, random

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 5

def ball_animation():
    global ball_speed_x, ball_speed_y

    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.top <= 0 or ball.bottom >= screen_height:
     ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= screen_width:
     ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
     ball_speed_x *= -1

def player_animation():
  player.y += player_speed

  if player.top <= 0:
    player.top = 0
  if player.bottom >= screen_height:
    player.bottom = screen_height

def opponent_ai():
  if opponent.top < ball.y:
    opponent.top += opponent_speed

  if opponent.bottom > ball.y:
    opponent.bottom -= opponent_speed
  
  if opponent.top <= 0:
    opponent.top = 0
  
  if opponent.bottom >= screen_height:
    opponent.bottom = screen_height

def ball_restart():
  global ball_speed_y, ball_speed_x

  ball.center = (screen_width/2, screen_height/2,)
  ball_speed_y *= random.choice((1, -1)) 
  ball_speed_x *= random.choice((1, -1)) 

#General Setup
pygame.init()
clock = pygame.time.Clock()

#Setting up Window
screen_width = 800
screen_height = 525
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')

#Game Rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 22,22)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 90)
opponent = pygame.Rect(10, screen_height/2 - 70, 10, 90)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

#Game variables
ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 5

#Text 
player_score = 0
opponent_score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
       pygame.quit
       sys.exit()
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_DOWN:
        player_speed += 7
      if event.key == pygame.K_UP:
        player_speed -= 7
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_DOWN:
        player_speed -= 7
      if event.key == pygame.K_UP:
        player_speed += 7
  
  #Game Logic
  ball_animation()
  player_animation()
  opponent_ai()

   # Game Visuals  
  screen.fill(bg_color)
  pygame.draw.rect(screen,light_grey, player)
  pygame.draw.rect(screen,light_grey, opponent)
  pygame.draw.ellipse(screen, light_grey, ball)
  pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))

  player_text = game_font.render(f"{player_score}", False, light_grey)
  screen.blit(player_text,(400, 300))


  #Updating the window
  pygame.display.flip()
  clock.tick(60)


