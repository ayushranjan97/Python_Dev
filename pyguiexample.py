#importing necessary files
from dearpygui.core import *
from dearpygui.simple import *



def add(sender, data):
    input_value1=get_value("Input1")
    input_value2 = get_value("Input1")
    print(input_value1+input_value2)


#creating main window
set_main_window_size(540,720)
set_global_font_scale(1.25)
set_theme("Gold")
set_style_window_padding(30,30)

with window("Simple SMS Spam filter",width=520,height=677,x_pos=1,y_pos=-2):
    set_window_pos("Simple SMS Spam filter",0,0)
    set_main_window_title("Made by Ayush")
    add_drawing("Logo",width=520,height=290)
    add_separator()
    add_spacing(count=12)
    add_text("Please enter SMS of your choice",color=[232, 163, 33])
    add_spacing(count=12)
    add_input_int("Input1")
    add_spacing(count=12)
    add_input_int("Input2")
    add_button("CHECK",callback=add)

draw_image("Logo","logo_spamFilter.png",[0,0],[458,192])




start_dearpygui()