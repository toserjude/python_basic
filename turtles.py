import turtle

def tobbszinu_negyzet_rajzolas(t, h):
    for i in ["red", "purple", "hotpink", "blue"]:
        t.color(i)
        t.forward(h)
        t.left(90)


a = turtle.Screen()
a.bgcolor("grey")


teknos = turtle.Turtle()
teknos.pensize(3)

# A legkisebb négyzet mérete
meret = 20

for i in range(15):
    tobbszinu_negyzet_rajzolas(teknos, meret)
    meret = meret + 10 # Növeljük a következő négyzet méretét
    teknos.forward(10) # Kicsit arrébb léptetjük a tekn˝ocöt
    teknos.right(18) # és kicsit elfordítjuk

a.mainloop()
