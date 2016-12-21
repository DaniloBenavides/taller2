import turtle
bob=turtle.Turtle()
a=int(input("ingrese numerod e lados"))
b=180/a

for i in range(1,a):
    bob.forward(50)
    bob.rt(225)
    bob.fd(b)
turtle.getscreen()._root.mainloop()
