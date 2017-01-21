class Iphone:

    color = ''
    is_plus = False 
    touch_home_button = False

    def __init__(self, color, is_plus, button):
        self.color = color
        self.is_plus = is_plus
        self.touch_home_button = button


seung_iphone = Iphone("black", False, True)
cheolseung_ihpone = Iphone("met black", False, True)
cheolseung_ihpone = Iphone("gold", True, False)
