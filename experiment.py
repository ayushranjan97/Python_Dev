from dearpygui import core, simple, demo
from loadsql import load_sql

def save_callback():
    print("Processing")
    load_sql()



def window():
    with simple.window("Example Window"):
        core.add_text("Hello world")
        core.add_button("Save",callback=save_callback)
        core.add_input_text("string",default_value="enter text")
        core.add_slider_float("float")
        core.add_slider_float("coat")

window()
core.start_dearpygui()