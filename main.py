import threading
import turtle
import tkinter as tk
from pynput import keyboard

# Create a turtle instance
t = turtle.Turtle()


# Create a turtle screen and set the window size
screen = turtle.Screen()
screen.setup(width=1000, height=1000)


# Define the turtle's movement functions
def move_forward():
    t.forward(100)
    print("Forward")


def move_backward():
    t.backward(100)
    print("Backward")


def turn_left():
    t.left(45)
    print("Left")


def turn_right():
    t.right(45)
    print("Right")


def restart():
    t.home()
    t.clear()
    print("Restart")


def exit_game():
    screen.bye()
    control_window.destroy()
    print("Exit")

def toggle_eraser():
    if t.pencolor() == "black":
        t.pencolor("white")
        print('Turtle eraser is ON')
    else:
        t.pendown()  # Set the eraser size
        t.pencolor("black")  # Set the eraser color
        print('Turtle eraser is OFF')

def controls_popup():
    # Create the tkinter window
    control_window = tk.Tk()
    # Exit button
    exit_button = tk.Button(control_window, text="OK", command=control_window.destroy)
    control_window.title("Controls")
    exit_button.pack()
    # Label
    exit_button_text = tk.Label(control_window, text="WASD to move around, R to restart, X to exit, E to toggle eraser and . to call this window.")
    exit_button_text.pack()
    control_window.mainloop()
    print("Called the Control Window")


# Thread target function to capture keyboard events
def on_press(key):
    try:
        if key.char == "w":
            move_forward()
        elif key.char == "s":
            move_backward()
        elif key.char == "a":
            turn_left()
        elif key.char == "d":
            turn_right()
        elif key.char == "r":
            restart()
        elif key.char == "x" or key == keyboard.Key.esc:
            exit_game()
        elif key.char == ".":
            controls_popup()
        elif key.char == "e":
            toggle_eraser()
    except AttributeError:
        if key == keyboard.Key.esc:
            exit_game()


# Collect events until released
def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


keyboard_thread = threading.Thread(target=start_keyboard_listener)
keyboard_thread.start()

try:
    # Create the tkinter window
    control_window = tk.Tk()

    # Exit button
    exit_button = tk.Button(control_window, text="OK", command=control_window.destroy)
    control_window.title("Controls")
    exit_button.pack()

    # Label
    exit_button_text = tk.Label(control_window, text="WASD to move around, R to restart and X to exit")
    exit_button_text.pack()

    # Run the turtle graphics
    turtle.mainloop()

    # Quit the tkinter window
    control_window.quit()
except KeyboardInterrupt:
    pass
