import eel

eel.init('web')

@eel.expose
def regPush(data_pushups):
    print("Number of pushups to be done is : ", data_pushups)

@eel.expose
def regCurl(data_curls):
    print("Number of curls to be done is : ", data_curls)

@eel.expose
def regSit(data_situps):
    print("Number of situps to be done is : ", data_situps)


eel.start('index.html', size=(1000, 600))
