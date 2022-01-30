from typing import Text


class Generic:

    def __init__(self, name, year):
        self._name = name.tittle()
        self.year = year
        self._likes = 0
    
    def __str__(self):
        print(f"Name: {self.name} - likes: {self.likes}")

    @property
    def likes(self):
        return self._likes

    def give_like(self):
        self._likes += 1

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name.title()

#-----------------------------------------------------------------------------#

class Film(Generic):
    def __init__(self, name, year, minutes):
        super().__init__(name, year)
        self.minutes = minutes
    
    def __str__(self):
        return (f"Name: {self.name} - {self.minutes} min - likes: {self.likes}")

#-----------------------------------------------------------------------------#

class Series(Generic):
    def __init__(self, name, year, temp, eps):
        super().__init__(name, year)
        self.temp = temp
        self.eps = eps
    
    def __str__(self):
        return (f"Name: {self.name} - {self.temp} temp - {self.eps} episodes - likes: {self.likes}")

#-----------------------------------------------------------------------------#

class Playlist():
    def __init__(self, name, programs):
        self.name = name
        self._programs = programs

    def __gettitem__(self,item):
        return self._programs[item]

    def __len__(self):
        return len(self._programs)
#-----------------------------------------------------------------------------#

Lucifer = Series("Lucifer", 2016, 6, 120)
The_Witcher = Series("The Witcher", 2020, 2, 50)
Dog = Series("The 4 life from a dog", 2000, 1, 20)
Cars = Film("Cars 1", 2006, 120)
Totoro = Film("My friend Totoro", 1988, 90)
Avengers = Film("Avengers - infinity war", 2019, 160)
legend = Film("I am the legend", 2007, 100)

i = 0
while i == 20:
    Totoro.give_like()
    i += 1

i = 0
while i == 10:
    Cars.give_like()
    i += 1

Avengers.give_like()
Avengers.give_like()
Avengers.give_like()

Lucifer.give_like()
Lucifer.give_like()

The_Witcher.give_like()


list = [Cars, Avengers, Lucifer, The_Witcher,legend,Dog]
end_weak = Playlist("films and series", list)

print(f"Playlist size is: {len(end_weak)}")

for i in end_weak:
    print(i)

