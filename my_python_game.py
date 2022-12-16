from tkinter import *
from PIL import Image
import time
import pygame
from pygame import mixer

                                                                                                                                                                                                                                                                                                    #Własność Chloe
GAME_WIDTH = 500
GAME_HEIGHT = 500
CHUNK = 10
WALL_COLOR = "#0f0704"
SEARCHER_COLOR = "#479e5e"
HATCH_COLOR = "#983812"

#Main app window

window = Tk()
window.title("What's below? - demo")
window.resizable(False, False)

#Game window

canvas = Canvas(window, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Map nr1

myimage = PhotoImage(file="mapa_filled0.png")
canvas.create_image(0, 0, image=myimage, anchor=NW)

# Go to the bottom

def lvl0():

    # Go down below lvl 1. We will use recursion in order to make our game work start from lvl 0 and follow function calling

    def lvl1():

        def lvl2():

            # lvl2 will work similar only difference is that we have to unbind keys and bind them again

            class Wall:
                def __init__(self):
                    self.wall_body = WALL_BODY
                    self.coordinate_x = []
                    self.coordinate_y = []
                    self.squares = []
                    self.coordinates = []

                    map_structure = Image.open("mapa_mury2.png")
                    px = map_structure.load()
                    for y in range(0, 500, 10):
                        for x in range(0, 500, 10):
                            color = px[x, y]
                            if color == (15, 7, 4, 255):
                                square = canvas.create_rectangle(x, y, x + CHUNK, y + CHUNK, fill=WALL_COLOR)
                                self.squares.append(square)
                                self.coordinate_x.append(x)
                                self.coordinate_y.append(y)
                                self.coordinates.append((x, y))

            class Searcher:

                def __init__(self, x, y):
                    self.x = x
                    self.y = y

                    self.square = canvas.create_rectangle(x, y, x + CHUNK, y + CHUNK, fill=SEARCHER_COLOR)

            class Hatch:

                def __init__(self):

                    self.coordinates = []
                    self.squares = []

                    map_structure = Image.open("mapa_mury2.png")
                    px = map_structure.load()
                    for y in range(0, 500, 10):
                        for x in range(0, 500, 10):
                            color = px[x, y]
                            if color == (152, 56, 18, 255):
                                square = canvas.create_rectangle(x, y, x + CHUNK, y + CHUNK, fill=HATCH_COLOR)
                                self.coordinates.append((x, y))
                                self.squares.append(square)

            class Flashlight:
                def __init__(self):

                    self.coordinates = []
                    self.squares = []
                    self.dictionary_of_darkness = {}

                    map_structure = Image.open("mapa_mury2.png")
                    px = map_structure.load()

                    for y in range(0, 500, 10):
                        for x in range(0, 500, 10):
                            color = px[x, y]
                            if isinstance(color, tuple):
                                square = canvas.create_rectangle(x, y, x + CHUNK, y + CHUNK,fill="#000000")
                                self.squares.append(square)
                                self.coordinates.append((x, y))
                                self.dictionary_of_darkness[(x, y)] = square

            def unbind(event):
                if event.keysym == 'Up':
                    pass
                elif event.keysym == 'Down':
                    pass
                elif event.keysym == 'Left':
                    pass
                elif event.keysym == 'Right':
                    pass

            # After finishing lvl 2 we play end credits

            def game_over2():

                canvas.delete(ALL)
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height()*0.8 / 3, font=("consolas", 18),
                                   text="Pomysł,Grafiki,Python"
                                        , fill="#360000")
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height()*1.2 / 3, font=("consolas", 18),
                                   text=
                                        "script i generalnie wszystko"
                                        , fill="#360000")
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() *1.6/3, font=("consolas", 18),
                                   text=
                                        "- Chloe O.", fill="#360000")
                canvas.config(bg="#6e6e6e")
                window.after(4000, game_over3)

            def game_over3():
                canvas.delete(ALL)
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() * 0.8 / 3, font=("consolas", 18),
                                   text="Dzieki za zagranie"
                                   , fill="#360000")
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() * 1.2 / 3, font=("consolas", 18),
                                   text=
                                   "w demo mojej gierki 🤓"
                                   , fill="#360000")

                canvas.config(bg="#6e6e6e")
                window.after(4000, game_over4)
            def game_over4():
                canvas.delete(ALL)
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() * 0.7 / 3, font=("consolas", 18),
                                   text="Szukam pracy w IT"
                                   , fill="#360000")
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() * 0.9 / 3, font=("consolas", 18),
                                   text=
                                   "python/html/css/ i"
                                   , fill="#360000")
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() * 1.1 / 3, font=("consolas", 18),
                                   text=
                                   "w trakcie nauczania js"
                                   , fill="#360000")
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() * 1.3 / 3, font=("consolas", 18),
                                   text=
                                   "zainteresowanych pracowdawców", fill="#360000")
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() * 1.5 / 3, font=("consolas", 18),
                                   text=
                                   "prosze o kontakt tu:", fill="#360000")
                canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() * 1.7 / 3, font=("consolas", 18),
                                   text=
                                   "chloekontaktb@gmail.com", fill="#360000")
                canvas.config(bg="#6e6e6e")

                # The end

            canvas.bind_all('<KeyPress-Up>', unbind)
            canvas.bind_all('<KeyPress-Down>', unbind)
            canvas.bind_all('<KeyPress-Left>', unbind)
            canvas.bind_all('<KeyPress-Right>', unbind)

            canvas.delete(ALL)

            # Map3

            myimage2 = PhotoImage(file="mapa_filled2.png")
            canvas.create_image(0, 0, image=myimage2, anchor=NW)

            # Music

            mixer.init()
            mixer.music.load("E:\what's below/soundtrack.mp3")
            mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.035)

            # Class objects

            wall = Wall()
            hatch = Hatch()
            flashlight = Flashlight()
            searcher = Searcher(80, 120)

            def move_object2(event):
                if event.keysym == 'Up':

                    id1 = flashlight.dictionary_of_darkness[(searcher.x, searcher.y - CHUNK)]
                    id2 = flashlight.dictionary_of_darkness[(searcher.x, searcher.y - 2 * CHUNK)]
                    canvas.delete(id1)
                    canvas.delete(id2)

                    if (searcher.x, searcher.y - 10) in wall.coordinates:
                        pass
                    elif (searcher.x, searcher.y - 10) in hatch.coordinates:
                        time.sleep(0.1)
                        game_over2()
                    else:
                        canvas.move(searcher.square, 0, -10)
                        searcher.y -= 10
                elif event.keysym == 'Down':

                    id1 = flashlight.dictionary_of_darkness[(searcher.x, searcher.y + CHUNK)]
                    id2 = flashlight.dictionary_of_darkness[(searcher.x, searcher.y + 2 * CHUNK)]
                    canvas.delete(id1)
                    canvas.delete(id2)

                    if (searcher.x, searcher.y + 10) in wall.coordinates:
                        pass
                    elif (searcher.x, searcher.y + 10) in hatch.coordinates:
                        time.sleep(0.1)
                        game_over2()
                    else:
                        canvas.move(searcher.square, 0, 10)
                        searcher.y += 10
                elif event.keysym == 'Left':

                    id1 = flashlight.dictionary_of_darkness[(searcher.x - CHUNK, searcher.y)]
                    id2 = flashlight.dictionary_of_darkness[(searcher.x - 2 * CHUNK, searcher.y)]
                    canvas.delete(id1)
                    canvas.delete(id2)

                    if (searcher.x - 10, searcher.y) in wall.coordinates:
                        pass
                    elif (searcher.x-10, searcher.y) in hatch.coordinates:
                        time.sleep(0.1)
                        game_over2()
                    else:
                        canvas.move(searcher.square, -10, 0)
                        searcher.x -= 10
                elif event.keysym == 'Right':

                    id1 = flashlight.dictionary_of_darkness[(searcher.x + CHUNK, searcher.y)]
                    id2 = flashlight.dictionary_of_darkness[(searcher.x + 2 * CHUNK, searcher.y)]
                    canvas.delete(id1)
                    canvas.delete(id2)

                    if (searcher.x + 10, searcher.y) in wall.coordinates:
                        pass
                    elif (searcher.x+10, searcher.y) in hatch.coordinates:
                        time.sleep(0.1)
                        game_over2()
                    else:
                        canvas.move(searcher.square, 10, 0)
                        searcher.x += 10

            canvas.bind_all('<KeyPress-Up>', move_object2)
            canvas.bind_all('<KeyPress-Down>', move_object2)
            canvas.bind_all('<KeyPress-Left>', move_object2)
            canvas.bind_all('<KeyPress-Right>', move_object2)

            window.mainloop()








        # lvl1 will work similar only difference is that we have to unbind keys and bind them again


        class Wall:
            def __init__(self):
                self.wall_body = WALL_BODY
                self.coordinate_x = []
                self.coordinate_y = []
                self.squares = []
                self.coordinates = []

                map_structure = Image.open("szkielet1mapa.png")
                px = map_structure.load()
                for y in range(0, 500, 10):
                    for x in range(0, 500, 10):
                        color = px[x, y]
                        if color == (15, 7, 4, 255):
                            square = canvas.create_rectangle(x, y, x + CHUNK, y + CHUNK, fill=WALL_COLOR)
                            self.squares.append(square)
                            self.coordinate_x.append(x)
                            self.coordinate_y.append(y)
                            self.coordinates.append((x, y))

        class Searcher:

            def __init__(self, x, y):
                self.x = x
                self.y = y

                self.square = canvas.create_rectangle(x, y, x + CHUNK, y + CHUNK, fill=SEARCHER_COLOR)

        class Hatch:

            def __init__(self):

                self.coordinates = []
                self.squares = []

                map_structure = Image.open("szkielet1mapa.png")
                px = map_structure.load()
                for y in range(0, 500, 10):
                    for x in range(0, 500, 10):
                        color = px[x, y]
                        if color == (152, 56, 18, 255):
                            square = canvas.create_rectangle(x, y, x + CHUNK, y + CHUNK, fill=HATCH_COLOR)
                            self.coordinates.append((x, y))
                            self.squares.append(square)

        class Flashlight:
            def __init__(self):

                self.coordinates = []
                self.squares = []
                self.dictionary_of_darkness = {}

                map_structure = Image.open("szkielet1mapa.png")
                px = map_structure.load()

                for y in range(0, 500, 10):
                    for x in range(0, 500, 10):
                        color = px[x, y]
                        if isinstance(color, tuple):
                            square = canvas.create_rectangle(x, y, x + CHUNK, y + CHUNK,fill="#000000")
                            self.squares.append(square)
                            self.coordinates.append((x, y))
                            self.dictionary_of_darkness[(x, y)] = square

        # We have to unbind old keys and bind them once more

        def unbind(event):
            if event.keysym == 'Up':
                pass
            elif event.keysym == 'Down':
                pass
            elif event.keysym == 'Left':
                pass
            elif event.keysym == 'Right':
                pass

        def game_over1():

            canvas.delete(ALL)
            canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, font=("consolas", 70),
                               text="Floor -2", fill="#360000")
            canvas.config(bg="#6e6e6e")
            window.after(1000, lvl2)


        canvas.bind_all('<KeyPress-Up>',unbind)
        canvas.bind_all('<KeyPress-Down>',unbind)
        canvas.bind_all('<KeyPress-Left>',unbind)
        canvas.bind_all('<KeyPress-Right>',unbind)

        canvas.delete(ALL)

        # Map2

        myimage2 = PhotoImage(file="mapafilled1.png")
        canvas.create_image(0, 0, image=myimage2, anchor=NW)

        # Music

        mixer.init()
        mixer.music.load("E:\what's below/soundtrack.mp3")
        mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.035)

        # Class objects

        wall = Wall()
        hatch = Hatch()
        flashlight = Flashlight()
        searcher = Searcher(330, 480)

        def move_object2(event):
            if event.keysym == 'Up':

                id1 = flashlight.dictionary_of_darkness[(searcher.x, searcher.y - CHUNK)]
                id2 = flashlight.dictionary_of_darkness[(searcher.x, searcher.y - 2 * CHUNK)]
                canvas.delete(id1)
                canvas.delete(id2)

                if (searcher.x, searcher.y - 10) in wall.coordinates:
                    pass
                elif (searcher.x, searcher.y - 10) in hatch.coordinates:
                    time.sleep(0.1)
                    game_over1()
                else:
                    canvas.move(searcher.square, 0, -10)
                    searcher.y -= 10
            elif event.keysym == 'Down':

                id1 = flashlight.dictionary_of_darkness[(searcher.x, searcher.y + CHUNK)]
                id2 = flashlight.dictionary_of_darkness[(searcher.x, searcher.y + 2 * CHUNK)]
                canvas.delete(id1)
                canvas.delete(id2)

                if (searcher.x, searcher.y + 10) in wall.coordinates:
                    pass
                else:
                    canvas.move(searcher.square, 0, 10)
                    searcher.y += 10
            elif event.keysym == 'Left':

                id1 = flashlight.dictionary_of_darkness[(searcher.x - CHUNK, searcher.y)]
                id2 = flashlight.dictionary_of_darkness[(searcher.x - 2 * CHUNK, searcher.y)]
                canvas.delete(id1)
                canvas.delete(id2)

                if (searcher.x - 10, searcher.y) in wall.coordinates:
                    pass
                else:
                    canvas.move(searcher.square, -10, 0)
                    searcher.x -= 10
            elif event.keysym == 'Right':

                id1 = flashlight.dictionary_of_darkness[(searcher.x + CHUNK, searcher.y)]
                id2 = flashlight.dictionary_of_darkness[(searcher.x + 2 * CHUNK, searcher.y)]
                canvas.delete(id1)
                canvas.delete(id2)

                if (searcher.x + 10, searcher.y) in wall.coordinates:
                    pass
                else:
                    canvas.move(searcher.square, 10, 0)
                    searcher.x += 10

        canvas.bind_all('<KeyPress-Up>', move_object2)
        canvas.bind_all('<KeyPress-Down>', move_object2)
        canvas.bind_all('<KeyPress-Left>', move_object2)
        canvas.bind_all('<KeyPress-Right>', move_object2)



        window.mainloop()












    #lvl 0 (first one)


    # I create technology which read colors from png map and create objects like walls on the virtual map
    # We will use it in different places

    class Wall:
        def __init__(self):
            self.wall_body = WALL_BODY
            self.coordinate_x = []
            self.coordinate_y = []
            self.squares = []
            self.coordinates = []


            map_structure = Image.open("mapa_skelet0.png")
            px = map_structure.load()
            for y in range(0, 500, 10):
                for x in range(0, 500, 10):
                    color = px[x, y]
                    if color==(15, 7, 4, 255):
                        square = canvas.create_rectangle(x,y,x+CHUNK,y+CHUNK,fill=WALL_COLOR)
                        self.squares.append(square)
                        self.coordinate_x.append(x)
                        self.coordinate_y.append(y)
                        self.coordinates.append((x,y))

    # Player class

    class Searcher:

        def __init__(self,x,y):

            self.x = x
            self.y = y


            self.square = canvas.create_rectangle(x,y,x+CHUNK,y+CHUNK,fill=SEARCHER_COLOR)

    #Finish point that takes us to another lvl

    class Hatch:

        def __init__(self):

            self.coordinates = []
            self.squares = []


            map_structure = Image.open("mapa_skelet0.png")
            px = map_structure.load()
            for y in range(0, 500, 10):
                for x in range(0, 500, 10):
                    color = px[x, y]
                    if color == (152, 56, 18, 255):
                        square = canvas.create_rectangle(x, y, x + CHUNK, y + CHUNK, fill=HATCH_COLOR)
                        self.coordinates.append((x, y))
                        self.squares.append(square)

    # This idea of mine, covers whole map in black squares, after player goes for example to the right the squares
    # in front of him are deleted this works as if player was exploring the map

    class Flashlight:
        def __init__(self):

            self.coordinates = []
            self.squares = []
            self.dictionary_of_darkness = {}

            map_structure = Image.open("mapa_skelet0.png")
            px = map_structure.load()

            for y in range(0, 500, 10):
                for x in range(0, 500, 10):
                    color = px[x, y]
                    if isinstance(color,tuple):
                        square = canvas.create_rectangle(x, y, x + CHUNK, y + CHUNK, fill="#000000")
                        self.squares.append(square)
                        self.coordinates.append((x, y))
                        self.dictionary_of_darkness[(x, y)] = square




    #funkcja konca poziomu

    def game_over0():

        #transition to lvl 1 and some text between

        canvas.delete(ALL)
        canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=("consolas",70),text="Floor -1",fill="#360000")
        canvas.config(bg="#6e6e6e")
        window.after(1000, lvl1)







    # Music playing in the background

    mixer.init()
    mixer.music.load("E:\what's below/soundtrack.mp3")
    mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.035)

    # Class objects

    wall = Wall()
    hatch = Hatch()
    flashlight = Flashlight()
    searcher = Searcher(330,400)


    # Right there we make it possible for our player to move our "searcher" character

    def move_object(event):
        if event.keysym == 'Up':


            # Right there player deletes 2 black squares in front of him.

            id1 = flashlight.dictionary_of_darkness[(searcher.x,searcher.y-CHUNK)]
            id2 = flashlight.dictionary_of_darkness[(searcher.x,searcher.y-2*CHUNK)]
            canvas.delete(id1)
            canvas.delete(id2)

            # If a player's next move will end up on coordinates where wall was created,he cant move this way.

            if (searcher.x,searcher.y-10) in wall.coordinates:
                pass

            # If a player's next move will end up on coordinates where hatch was created lvl is finished and
            # "game over" function is called (basically transition to lvl1)

            # If none of above happens player move by 10 pixels in direction chosen by pressing arrows on keyboard

            elif (searcher.x,searcher.y-10) in hatch.coordinates:
                time.sleep(0.1)
                game_over0()
            else:
                canvas.move(searcher.square, 0, -10)
                searcher.y -= 10
        elif event.keysym == 'Down':

            id1 = flashlight.dictionary_of_darkness[(searcher.x, searcher.y + CHUNK)]
            id2 = flashlight.dictionary_of_darkness[(searcher.x, searcher.y + 2 * CHUNK)]
            canvas.delete(id1)
            canvas.delete(id2)

            if (searcher.x,searcher.y+10) in wall.coordinates:
                pass
            elif (searcher.x,searcher.y+10) in hatch.coordinates:
                time.sleep(0.1)
                game_over0()
            else:
                canvas.move(searcher.square, 0, 10)
                searcher.y += 10
        elif event.keysym == 'Left':

            id1 = flashlight.dictionary_of_darkness[(searcher.x - CHUNK, searcher.y)]
            id2 = flashlight.dictionary_of_darkness[(searcher.x - 2 * CHUNK, searcher.y)]
            canvas.delete(id1)
            canvas.delete(id2)

            if (searcher.x - 10,searcher.y) in wall.coordinates:
                pass
            else:
                canvas.move(searcher.square, -10, 0)
                searcher.x -= 10
        elif event.keysym == 'Right':

            id1 = flashlight.dictionary_of_darkness[(searcher.x + CHUNK, searcher.y)]
            id2 = flashlight.dictionary_of_darkness[(searcher.x + 2 * CHUNK, searcher.y)]
            canvas.delete(id1)
            canvas.delete(id2)

            if (searcher.x + 10,searcher.y) in wall.coordinates:
                pass
            else:
                canvas.move(searcher.square, 10, 0)
                searcher.x += 10

    canvas.bind_all('<KeyPress-Up>', move_object)
    canvas.bind_all('<KeyPress-Down>', move_object)
    canvas.bind_all('<KeyPress-Left>', move_object)
    canvas.bind_all('<KeyPress-Right>', move_object)


# Function calling


lvl0()


window.mainloop()


