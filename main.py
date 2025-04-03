temp = 0
hum = 0
pins.digital_write_pin(DigitalPin.P11, 0)
pins.digital_write_pin(DigitalPin.P12, 0)

def on_forever():
    global hum, temp
    dht11_dht22.query_data(DHTtype.DHT11, DigitalPin.P5, True, False, True)
    hum = dht11_dht22.read_data(dataType.HUMIDITY)
    temp = dht11_dht22.read_data(dataType.TEMPERATURE)

    # Αν υπάρχει σφάλμα μέτρησης, μην κάνεις τίποτα — κράτα τα πάντα όπως ήταν
    if temp == 999 or hum == 999:
        return

    # Αν όλα είναι εντάξει, προχώρα κανονικά
    basic.show_number(Math.round(temp))
    basic.pause(2000)
    basic.show_number(hum)
    basic.pause(2000)

    if 20 <= temp <= 26 and 40 <= hum <= 60:
        pins.digital_write_pin(DigitalPin.P12, 0)
        pins.digital_write_pin(DigitalPin.P11, 1)
        basic.show_icon(IconNames.HAPPY)
    else:
        pins.digital_write_pin(DigitalPin.P12, 1)
        pins.digital_write_pin(DigitalPin.P11, 0)
        basic.show_icon(IconNames.SAD)

basic.forever(on_forever)