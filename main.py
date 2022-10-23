from random import *

class cat:
  def __init__(self, name):
    self.name = name
    self.gladness = 50
    self.sadness = 0
    self.alive = True

  def food (self):
    print('you are eating') #ты ешь
    self.sadness -= 5
    self.gladness += 5


  def sleep(self):
    print('Sleep time') 
    self.gladness += 5
    self.sadness -= 2

  
  def punished (self): 
    print('the owner is punished') #хозяин наказал
    self.gladness -= 5
    self.sadness += 5

  def is_alive(self):
    if self.sadness < -40:
      print('So bad')
      self.alive = False
    elif self.gladness <= 0:
      print('Depression...')
      self.alive = False
    elif self.gladness > 150:
      print('Mission passed')
      self.alive = False

  def end(self):
    print('Gladness:', self.gladness)
    print('sadness:', self.sadness)
    
  def live(self, day):
    print('Day:',day)
    live_cube = randint(1,3)
    if live_cube == 1:
      self.food()
    elif live_cube == 2:
      self.sleep()
    elif live_cube == 3:
      self.punished()
    self.end()
    self.is_alive()

obj = cat('Bob')

for day in range(100):
	if obj.alive == False:
		break
	obj.live(day)