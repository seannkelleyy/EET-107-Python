# Sean Kelley
# Ch13-2
# 28 July 2021

from guizero import App, Drawing

a = App()

# ----- House ----------
h = Drawing(a, width=400, height=400)
h.rectangle(0, 0, 400, 400, color='deep sky blue')   # sky
h.oval(30, 30, 70, 70, color='dark orange')     # sun
h.rectangle(0, 300, 400, 400, color='green')    # grass
h.rectangle(175, 300, 225, 400, color='gray')   # sidewalk
h.rectangle(100, 200, 300, 300, color='purple')    # house
h.rectangle(120, 200, 150, 150, color='dim gray')   # chimney
h.triangle(90, 200, 200, 150, 310, 200, color='indigo')     # roof
h.rectangle(120, 210, 150, 260, color='blue')   # window left
h.rectangle(250, 210, 280, 260, color='blue')   # window right
h.rectangle(175, 220, 225, 300, color='saddle brown')  # door
h.oval(215, 260, 218, 265, color='black')       # door handle
h.text(165, 200, text='Aalissia', color='red')   # text above door

a.display()
