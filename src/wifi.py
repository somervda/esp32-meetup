import utime
import network

print('Setting up network.')
sta_if = network.WLAN(network.STA_IF)
connection_ms = 10000

if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.active(True)
    sta_if.connect("guest24", "backyard")
    while (not sta_if.isconnected()) and connection_ms > 0:
        print("Waiting for connection", connection_ms)
        connection_ms -= 500
        utime.sleep_ms(500)


print('network config:', sta_if.ifconfig())
