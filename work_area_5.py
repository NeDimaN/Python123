from car import electrocar


def main():
    e = electrocar.ElectroCar('Tesla', 'T', 2018, 99000)
    e.show_car()
    e.description_battery()


if __name__ == '__main__':
    main()
