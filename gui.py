import tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
root =Tk()

from tkinter import Tk, Button, Frame, Entry, END
root.title("Story Generator")

root['background'] = '#ff9999'
label0 = Label(root,bg='#6cf5c5',text="Click the button below to generate a random story",borderwidth=2)
label0.pack(pady=20)
import random


def display():
    Sentence_starter = ['About 100 years ago', ' In the 10 BC', 'Once upon a time']
    character = [' there lived a king.\n',' there was a man named Dwight\n',
             ' there lived a farmer.\n']
    time = [' One day', ' One full-moon night']
    story_plot = [' he was passing by\n',' he was going for walk to\n ']
    place = [' the mountains', ' the garden']
    second_character = [' he saw a man\n', ' he saw a young lady\n']
    age = [' who seemed to be in late 20s', ' who seemed very old and feeble']
    work = [' searching something.', ' digging a well on roadside.']
    label1 = Label(
        root,
        relief="solid",
        background='#0AF0F3',
        text=(random.choice(Sentence_starter) + random.choice(character) +
              random.choice(time) + random.choice(story_plot) +
              random.choice(place) + random.choice(second_character) +
              random.choice(age) + random.choice(work)))
    label1.pack(padx=30,pady=5)
def jfk():
    label2=Label(root,text=('John Fitzgerald Kennedy (May 29, 1917 – November 22, 1963), often referred to by his initials JFK,\n was an American politician who served as the 35th president of\n the United States from 1961 until his assassination near the end of his third year in office. \n A Democrat, Kennedy represented Massachusetts in both houses of the U.S. Congress prior to his presidency.'))
    label2.pack(padx=30, pady=10)


def ron():
    label3 = Label(
        root,border=2,
        text=
        ('Cristiano Ronaldo dos Santos Aveiro GOIH ComM ( born 5 February 1985) is a Portuguese professional\n footballer who plays as a forward for Premier League club \nManchester United and captains the Portugal national team. Often considered the best player in the world \nand widely regarded as one of the greatest players of all time, Ronaldo has won five Ballon dOr awards'
         ))
    label3.pack(padx=30,pady=10)


image=PhotoImage(file='click.png')
photoimage = image.subsample(3,4)
button = Button(root,
                image=photoimage,
                fg="red",
                activebackground='#ff9999',
                command=display,
                borderwidth=0,
                background='#ff9999')
button.pack(pady=20)
label0 = Label(root,
               bg='#6cf5c5',
               text="Click image to display their story",
               borderwidth=2)
label0.pack(pady=10)
frame1=Frame(root,background='#ff9999')
frame1.pack(pady=5)
image1 = PhotoImage(
    file='555px-John_F._Kennedy,_White_House_color_photo_portrait.png')
photoimage2=image1.subsample(5,5)
b1=Button(frame1,image=photoimage2,command=jfk)
b1.grid(row=0,column=0,padx=20)
image1 = PhotoImage(
    file='ron.png')
photoimage3 = image1.subsample(6, 6)
b2 = Button(frame1, image=photoimage3,command=ron)
b2.grid(row=0, column=1, padx=20)

def myClick():
    if len(e1.get()) == 0:
        messagebox.showwarning("Story Generator", "Please fill name")
    if len(e2.get()) == 0:
        messagebox.showwarning("Story Generator", "Please fill quality")

    if len(e1.get()) != 0:

        k = random.randint(1, 2)
        k2 = str(random.randint(1, 8))

        Noun = [
            "is a good person ", "is a brave person ", "lives in New Delhi ",
            "lives in Mumbai ", "lives in Phagwara "
        ]

        Setup = [
            "There was a cruel Ork King",
            "A Red dragon was terrorizing the kingdom",
            "A princess was trapped in magical kingdom by a Red Dragon",
            "The enemy of Orks were at kingdom's door",
            "Kingdom was fighting a loosing battle"
        ]
        Noun2 = {
            "1": " struggling to get by ",
            "2": " the proud owner of a small textile mill ",
            "3": " who worked as a small tailor ",
            "4": " tending to his farm ",
            "5": " a common man ",
            "6": " and was a successful student ",
            "7": " a middle class salaryman ",
            "8": " a son to a small bussinessman "
        }
    if k == 2 and len(e2.get()) != 0:
        myLabel4 = Label(root,
                         text="Once upon a time, " + random.choice(Setup) +
                         " and " + e1.get()+',' + Noun2[k2] +
                         "magically summoned to the resuce!")
        myLabel4.pack(padx=30)
    if k == 1 and len(e2.get()) != 0:
        myLabel4 = Label(
            root,
            text=e1.get() + " " + Noun[k] + Noun2[k2] +
            "Suddenly, all went awry when they were summoned to the magical kingdom!"
        )
        myLabel4.pack(padx=30)


    if k > 0:
        Adjective = [
            "However didnt let go of their ",
            "was great confusion and they let go of ",
            " were mesmerised and felt ",
            " However felt nothing like a hero should, "
        ]

    if k > 0 and len(e2.get()) != 0:

        MonologueIntro = [
            "Upon reaching the kingdom, ",
            "Upon reaching the kingdom's court, ",
            "Upon being summoned to the kingdom, ",
            "Upong being summoned in the middle of dark winter night to the kingdom, ",
            "Upon being summoned to the kingdom's church ",
            "It was warm sunny morning when our hero appeared ",
            "Warm sun shinning on the vast green grassland when our hero touched the soil of magic kingdom the first time"
        ]

        MonologueResponsible = [
            "The King was thrilled.", "The King's Court was thrilled.",
            "The King Kingdom was filled with up hope.",
            "The king asked them to help them with fighting the dragon.",
            "The King pleaded them to join them in conquest against the dragon.",
            "The Kingdom was rejoyed with arrival of the new hero.",
            "Suddenly the whole kingdom was filled with joy for now they had a fighting chance"
        ]

        MonologueHero = [
            "To be the hero of the story,",
            "The hero of our story,",
            "Once a common mam now hero,",
            "Our hero,",
            " Magic Kingdom last hero",
        ]

        MonologueFight = [
            "went into the deep redwood forest",
            "went deep to save the day",
            "Charged the battle that was knocking at the kingdom's door",
            "listening to the problem found the courage and charged the battle!",
            "went out to the battle on the Great Mount Volca",
            "Our common man now hero lead the kingdom army to the warfield of King Doom",
            "air was warm and night dark but hero feared none and charged the Dargon Mount"
        ]

        MonologueEnd = [
            "Hero passing through dense kingdom forest to the battlefield was suddenly attacked",
            "Suddenly the hero was attacked by magic casters with fireballs",
            "The oracks surrounded our hero", "The dragon flew over our hero",
            "Enemies hidden in thick forest surrounded our hero passing by to the battlefield",
            "enemies arhers shot some arrows at our hero",
            "Our hero party shot their warning shot at the dragon lair"
        ]
        myLabel5 = Label(root,
                         text=random.choice(MonologueIntro) + " " +
                         random.choice(MonologueResponsible)+e1.get() + " " + random.choice(Adjective) +
                         e2.get() + " in their heart.")
        myLabel5.pack(padx=30)

        myLabel6 = Label(root,
                         text=random.choice(MonologueHero) + ", " +
                         random.choice(MonologueFight)+" "+random.choice(MonologueEnd))
        myLabel6.pack(padx=30)


label0 = Label(root,
               bg='#6cf5c5',
               text="Story based on character and quality",
               borderwidth=2)
label0.pack(pady=15)
myLabel2 = Label(root,bg='#6cf5c5', text="Enter a Character Name",borderwidth=2)
myLabel2.pack()

e1 = Entry(root, width=18,border=5)
e1.pack()

myLabel3 = Label(root,bg='#6cf5c5', text="Enter an Character Trait",borderwidth=2)
myLabel3.pack()

e2 = Entry(root, width=18,border=5)
e2.pack()

myButton = Button(root, text="generate", command=myClick)
myButton.pack()

myLabel2.pack(padx=(30), pady=(5))
myLabel3.pack(padx=(30), pady=(5))
myButton.pack(padx=(30), pady=(20))

root.mainloop()