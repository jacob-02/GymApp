import eel
import os
import sys
import click_img

eel.init('web')

@eel.expose
def reg(data):
    print(data)
    os.mkdir("images/" + data)
    click_img.start(data)


eel.start('index.html', size=(1000, 600))
