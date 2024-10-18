from random import randint, choice

class River():
  def __init__(self, size, num_bears, num_fish):
    self.size = size
    self.river = [["🟦 "]*self.size for i in range(self.size)]
    self.num_bears = num_bears
    self.num_fish = num_fish
    self.animals = []
    self.population = 0
    self.__initial_population()
  
  def __getitem__(self, index):
    return self.river[index]

  def __str__(self):
    self.redraw_cells()
    out = ""
    for i in range(len(self.river)):
      for x in range(len(self.river)):
        out += str(self.river[i][x])
      out += "\n"
    return out

  def __initial_population(self):
    for i in range(self.num_bears):
      self.place_baby(Bear)
    for i in range(self.num_fish):
      self.place_baby(Fish)

  def place_baby(self, animal):
    x = randint(0, len(self.river)-1)
    y = randint(0, len(self.river)-1)
    while self.river[y][x] != "🟦 ":
      x = randint(0, len(self.river)-1)
      y = randint(0, len(self.river)-1)

    if animal == Bear or type(animal) == Bear:
      new = Bear(x,y)
      self.river[y][x] = new
      self.animals.append(new)

    elif animal == Fish or type(animal) == Fish:
      new = Fish(x,y)
      self.river[y][x] = new
      self.animals.append(new)
    self.population += 1
  
  def animal_death(self, animal, River):
    try:
      self.animals.remove(animal)
      self.population -= 1
    except:
      pass

  def redraw_cells(self):
    self.river = [["🟦 "]*self.size for i in range(self.size)]
    for animal in self.animals:
      self.river[animal.y][animal.x] = animal

  def new_day(self):
    for animal in self.animals:
      if type(animal) == Bear:
        animal.starve(self)
      animal.bred_today = False
      animal.move(self)
    

class Animal():
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.bred_today = False

  def death(self, animal, River):
    River.animal_death(animal, River)

  def move(self, River):
    self.x += choice([-1, 0, 1])
    self.y += choice([-1, 0, 1])
    if self.x < 0:
      self.x += 1
    elif self.x > 14:
      self.x -= 1
    if self.y < 0:
      self.y += 1
    elif self.y > 14:
      self.y -= 1
    if River[self.y][self.x] == "🟦 ":
      pass
    else:
      other = River[self.y][self.x]
      self.collision(other, River)

  def collision(self, other, River):
    if type(self) == type(other):
      if self.bred_today == False and other.bred_today == False:
        River.place_baby(self)
        print(f"A {self} was born")
        self.bred_today = True
        other.bred_today = True
      else:
        pass
    elif type(self) != type(other):
      if type(self) == Bear:
        self.consume(other, River)
        print("A 🐟  was eaten")
      else:
        other.consume(self, River)
        print("A 🐟  was eaten")


class Bear(Animal):
  def __init__(self, x, y):
    super().__init__(x,y)
    self.max_lives = 5
    self.lives = self.max_lives
    self.eaten_today = False

  def __str__(self):
    return "🐻 "

  def starve(self, River):
    if self.eaten_today == False:
      self.lives -= 1
      if self.lives <= 0:
        self.death(self, River)
        print(f"A {self} starved")

  def consume(self, fish, River):
    self.eaten_today = True
    self.lives = self.max_lives
    other = River.river[self.y][self.x]
    self.death(other, River)


class Fish(Animal):
  def __init__(self,x,y):
    super().__init__(x,y)
    self.bred_today = False

  def __str__(self):
    return "🐟 "