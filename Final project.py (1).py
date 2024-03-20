from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar

class BINARYCONVERTERApp(MDApp): 
    #Toolbar
    def convert (self,temp): # need to create 2 diff. arguments for button one is self must and then we need to fetch the user entered number
        #as user entered is string converted into integer
        result = int(self.input.text,2) #Not gonna work in flip func. #result with self prefix can be accessed from multiple func like convert and build
        #self.input.text is user entered value we need to convert string to int
        self.converted.text = str(result)
    def build(self):
        screen = MDScreen()
        self.theme_cls.primary_palette = "Indigo" #For color of toolbar
        self.toolbar = MDTopAppBar(title="Binary Converter")
        self.toolbar.pos_hint = {"top": 1}
        #Placing toolbar widget on the screen
        screen.add_widget(self.toolbar)

        #collect User input
        self.input = MDTextField(text="Enter a binary number",halign="center",size_hint = (0.8,1),pos_hint = {"center_x":0.5,"center_y":0.45},font_size = 32)
        screen.add_widget(self.input)  #halign is user value place and attribute
        #In decimal is label
        self.label =  MDLabel(text="In decimal is",halign="center",size_hint = (0.8,1),pos_hint = {"center_x":0.5,"center_y":0.35})
        self.converted =  MDLabel(text=" ",halign="center",size_hint = (0.8,1),pos_hint = {"center_x":0.5,"center_y":0.3})
        screen.add_widget(self.label)
        screen.add_widget(self.converted)
        #Convert Button
        screen.add_widget(MDFillRoundFlatButton(
            text = "CONVERT",
            font_size = 20,pos_hint = {"center_x":0.5,"center_y":0.15},on_press = self.convert))
        return screen

BINARYCONVERTERApp().run()

#by convintion we call the instance self and after that we can specify what other arguments that we want to accept

#In Decimal system we are using 10 digits(0,1,2,3,4,5,6,7,8,9) so we call it as base 10 
#Example- 1024 is made of 1*1000+0*100+2*10+4*1 where 1000=10^3 also others are 10^
#In binary system we have (0,1) digits so we call it base 2
#In base 10 multiplied by 10 raise to the power so in base 2 we multiply by 2 raise to the power
#Example= 1110 is 1 * 2^3 + 1 * 2^2 + 1 * 2^1 + 0 * 2^0 = 14 in decimal


