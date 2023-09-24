def makeBank(f=100, w=100, g=100, s=100):
    return {"food":f, "wood":w, "gold":g, "stone":s}

if __name__ == "__main__":
    from Gui import Gui
    from Market import Market
    from Poles import Poles
    from Malay import Malay
    market = Market()
    poles = Poles()
    malay = Malay()
    gui = Gui()
    #while True:
    #user_input = input("Enter something (type 'quit' to exit): ")
    #if user_input == 'quit':
    #    break
    # Do something with the input
    #print("You entered:", user_input)
