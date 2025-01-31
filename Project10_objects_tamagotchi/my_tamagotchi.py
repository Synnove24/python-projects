#imports classes
import random
import turtle
import time

#creates a class called pet
class Pet:
    def __init__(self,name:str)->None:
        """creates intitial conditions"""
        self.name = name
        self.fullness = 8
        self.happiness = 8
        self.cleanliness = 8
        self.alive = True
        self.stage = "egg"
        self.progress = 1       
    def feed(self)->None:
        """feeds tamagotchi 3 and if it goes over 10, cleanliness goes down 2"""
        self.fullness += 3
        if self.fullness > 10:
            self.fullness = 10
            self.cleanliness = self.cleanliness - 2
            if self.cleanliness < 1:
                self.cleanliness = 1
    def play(self)-> None:
        """plays with tamagotchi, increases happiness by 3 and if it goes over 10, fullness goes down 2"""
        self.happiness += 3
        if self.happiness > 10:
            self.happiness = 10
            self.fullness = self.fullness -2
            if self.fullness <1:
                self.fullness = 1
    def bathe(self)->None:
        """cleans tamagotchi 3 and if it goes over 10, happiness goes down 2"""
        self.cleanliness += 3
        if self.cleanliness > 10:
            self.cleanliness = 10
            self.happiness = self.happiness -2
            if self.happiness <1:
                self.happiness = 1
    def age_up(self)->None:
        """Makes the tamagotchi age up one stage"""
        if self.stage == "egg":
            self.stage = "baby"
        elif self.stage == "baby":
            self.stage = "child"
        elif self.stage == "child":
            self.stage = "adult"
        else:
            self.stage = "adult"   
        self.progress = 1
    def status(self)->str:
        """Tells you the status of the tamagotchi based on its levels"""
        #if statement to find the status range
        if (self.fullness  > 5) and (self.happiness > 5) and (self.cleanliness > 5):
            return "fine"
        elif (self.fullness  == 1) or (self.happiness == 1) or (self.cleanliness == 1):
            return "dead"
            self.alive = False
        else:
            return "distress"
    def time_step(self)->str:
        """increases time by one increment which lowers either happiness, fullness, or cleanliness. Also increases progress by 1"""
        x = random.choice([1,2,3])
        #based on the random choice, one of the three will decrease by 1
        if x == 1:
            self.happiness += -1
        elif x == 2:
            self.cleanliness += -1
        else:
            self.fullness += -1
        self.progress += 1
        if self.progress == 20:
            self.age_up()    
        return self.status()    


def fill_circle(turtle, color, radius, position):
        turtle.up()
        turtle.goto(position)
        turtle.down()
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(radius)
        turtle.end_fill()
        turtle.up()
        turtle.goto(0,0)
        
class TamagotchiGame:
    def __init__(self, name: str):
        """Creates a Tamagotchi Pet with the given name"""
        self.pet = Pet(name)
        self.pen = turtle.Turtle()
        self.pen.up()
        self.pen.hideturtle()

    def draw_egg(self):
        turtle.tracer(0,0)
        fill_circle(self.pen, "green", 20, (0,0))
        fill_circle(self.pen, "white", 5, (10,20))
        fill_circle(self.pen, "white", 5, (-10,20))
        fill_circle(self.pen, "black", 2, (10,22))
        fill_circle(self.pen, "black", 2, (-10,22))
        turtle.update()

    def draw_baby(self):
        turtle.tracer(0,0)
        fill_circle(self.pen, "red", 10, (15,0))
        fill_circle(self.pen, "red", 10, (-15,0))
        fill_circle(self.pen, "red", 30, (0,0))
        fill_circle(self.pen, "white", 8, (15,30))
        fill_circle(self.pen, "white", 8, (-15,30))
        fill_circle(self.pen, "black", 4, (15,34))
        fill_circle(self.pen, "black", 4, (-15,34))
        turtle.update()

    def draw_child(self):
        turtle.tracer(0,0)
        fill_circle(self.pen, "purple", 14, (20,0))
        fill_circle(self.pen, "purple", 14, (-20,0))
        fill_circle(self.pen, "purple", 10, (40,40))
        fill_circle(self.pen, "purple", 10, (-40,40))
        fill_circle(self.pen, "purple", 40, (0,0))
        fill_circle(self.pen, "white", 10, (15,40))
        fill_circle(self.pen, "white", 10, (-15,40))
        fill_circle(self.pen, "black", 5, (15,44))
        fill_circle(self.pen, "black", 5, (-15,44))
        turtle.update()

    def draw_adult(self):
        turtle.tracer(0,0)
        fill_circle(self.pen, "blue", 18, (25,0))
        fill_circle(self.pen, "blue", 18, (-25,0))
        fill_circle(self.pen, "blue", 12, (50,50))
        fill_circle(self.pen, "blue", 12, (-50,50))
        fill_circle(self.pen, "blue", 50, (0,0))
        fill_circle(self.pen, "purple", 5, (0,35))
        fill_circle(self.pen, "white", 12, (15,50))
        fill_circle(self.pen, "white", 12, (-15,50))
        fill_circle(self.pen, "black", 6, (15,55))
        fill_circle(self.pen, "black", 6, (-15,55))
        turtle.update()

    def draw_tombstone(self):
        turtle.tracer(0,0)
        self.pen.fillcolor("gray")
        self.pen.begin_fill()
        self.pen.forward(50)
        for i in range(2):
            self.pen.left(90)
            self.pen.forward(200)
            self.pen.left(90)
            self.pen.forward(100)
        self.pen.end_fill()
        self.pen.up()
        self.pen.goto(0,160)
        self.pen.write("RIP", align = "center", font=("Arial", 20, "normal"))
        self.pen.goto(0,140)
        self.pen.write(self.pet.name, align = "center", font=("Arial", 15, "normal"))
        self.pen.goto(0,0)
        turtle.update()

    def display(self):
        self.pen.clear()
        self.pen.up()
        self.pen.goto(0,-30)
        self.pen.write(self.pet.name, align = "center", font=("Arial", 20, "normal"))
        self.pen.goto(0,0)
        if self.pet.stage == "egg":
            self.draw_egg()
        elif self.pet.stage == "baby":
            self.draw_baby()
        elif self.pet.stage == "child":
            self.draw_child()
        else:
            self.draw_adult()

    def feed(self):
        self.pet.feed()
        self.display()
        self.pen.goto(0,20)
        self.pen.write("NOM NOM NOM", align = "center", font=("Arial", 30, "normal"))
        self.pen.goto(0,0)
        time.sleep(2)
        self.display()

    def play(self):
        self.pet.play()
        self.display()
        self.pen.goto(0,20)
        self.pen.write("WEEEEE!!!!!", align = "center", font=("Arial", 30, "normal"))
        self.pen.goto(0,0)
        time.sleep(2)
        self.display()

    def bathe(self):
        self.pet.bathe()
        self.display()
        self.pen.goto(0,20)
        self.pen.write("SCRUB SCRUB SCRUB", align = "center", font=("Arial", 30, "normal"))
        self.pen.goto(0,0)
        time.sleep(2)
        self.display()

    def run(self) -> None:
        """Runs the Tamagotchi game"""
        self.display()
        time.sleep(2)
        state = self.pet.time_step()
        while state != "dead":
            self.display()
            if state == "distress":
                for i in range(2,5):
                    self.pen.goto(0,30*i)
                    self.pen.write("WWAHHHH!! :(", align = "center", font=("Arial", 30, "normal"))
                self.pen.goto(0,0)
            self.pen.goto(0,-50)
            self.pen.write("Type 1 to feed, 2 to play, 3 to bathe", align = "center", font=("Arial", 15, "normal"))
            self.pen.goto(0,0)
            turtle.listen()
            turtle.onkey(self.feed, "1")
            turtle.onkey(self.play, "2")
            turtle.onkey(self.bathe, "3")
            time.sleep(1)
            state = self.pet.time_step()
        self.pen.clear()
        self.draw_tombstone()
        turtle.exitonclick()    

#creates function to play game
def play_tamagotchi()->None:
    """starts game with name inputed by the user"""
    name = input("What would you like to name your Tamagotchi?")
    game = TamagotchiGame(name)
    game.run()
    
play_tamagotchi()
