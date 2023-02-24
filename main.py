from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk
# Pillow     9.4.0


def make_greyscale(canvas, new_tk_image):
    canvas.itemconfig(canvas_person_img, image=new_tk_image)


window = Tk()

main_canvas = Canvas(window, width=400, height=400, highlightthickness=0, bg="lightcyan")
main_canvas.pack()

bg = Image.open("bg2.png")
person = Image.open("person.png")
greyscale_person = person.convert("LA")

# greyscale_person.save("greyscale_image.png")

tk_bg = ImageTk.PhotoImage(bg)
tk_person = ImageTk.PhotoImage(person)
tk_person_greyscale = ImageTk.PhotoImage(greyscale_person)

canvas_bg_img = main_canvas.create_image(0, 0, image=tk_bg, anchor="nw")
canvas_person_img = main_canvas.create_image(100, 100, image=tk_person, anchor="nw")

button = Button(main_canvas, text="make greyscale", command=lambda: make_greyscale(main_canvas, tk_person_greyscale))
button.place(x=20, y=20)

window.mainloop()
