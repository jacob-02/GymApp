import eel
from excercises import pushups, situps, curls


eel.init('web')


@eel.expose
def regPush(data_pushups):
    print("Number of pushups to be done is : ", data_pushups)
    pushups.pushups(data_pushups, 'videos/Pushups.mpg')


@eel.expose
def regCurl(data_curls):
    print("Number of curls to be done is : ", data_curls)
    curls.curls('videos/curls.mp4')


@eel.expose
def regSit(data_situps):
    print("Number of situps to be done is : ", data_situps)
    situps.situps('videos/situps.mp4')


eel.start('index.html', size=(1000, 600))
