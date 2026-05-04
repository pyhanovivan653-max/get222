import RPi.GPIO as GPIO

leds = [16,20,21,25,26,17,27,22]
GPIO.setmode(GPIO.BCM)
GPIO.setup(leds, GPIO.OUT)
dynamic_range = 3.158

def voltage_to_number(voltage):
    if not (0.0 <= voltage <= dynamic_range):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 -{dynamic_range:.2f} B")
        print("Устанавливаем 0.0 В")
        return 0

    return int(voltage / dynamic_range * 255)


def number_to_dac(number):
    return [int(bit) for bit in bin(int(number))[2:].zfill(8)]

try:
    while True:
        try:
            voltage = float(input("Введите ваше напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            bit_list = number_to_dac(number)
            print(f"{voltage} Вольт,{number} после перевода , {bit_list} лист")
            GPIO.output(leds, bit_list)

        except ValueError:
            print("Вы ввели не числою Попробуйте еще раз\n")

finally:
    GPIO.output(leds, 0)
    GPIO.cleanup()
