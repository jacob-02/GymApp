import eel
from excercises import pushups, curls


eel.init('web')


@eel.expose
def regPush(data_pushups):
    print("Number of pushups to be done is : ", data_pushups)
    pushups.pushups(1)


@eel.expose
def regCurl(data_curls):
    print("Number of curls to be done is : ", data_curls)
    curls.curls(1)


@eel.expose
def regSit(data_situps):
    print("Number of situps to be done is : ", data_situps)


eel.start('index.html', size=(1000, 600))
