import djitellopy
 from time import sleep

me = tello.tello()
me.connect()

print(me.get_battery())
