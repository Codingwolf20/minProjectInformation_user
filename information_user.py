from kivymd.app  import MDApp
from kivy.core.window import Window
from kivy.lang import Builder

class  TestApp(MDApp):
    id_user=0
    array=[0]
    def see(self,event):
        # self.cou=self.root.ids.count.text=self.array[0]
        self.cou=self.root.ids.count.text=f"{self.array}"

    def  information (self,event):
       if (self.root.ids.text_input_one.text!="" and self.root.ids.text_input_tow.text!=""):

            self.box1=self.root.ids.text_input_one.text
            self.box2=self.root.ids.text_input_tow.text
            self.box_output=self.root.ids.texts_color_change_one.text=f"{self.box1}"
            self.box_output2=self.root.ids.texts_color_change_tow.text=f"{self.box2}"
            self.box_output2=self.root.ids.texts_color_change_one.color=0,1,0,1
            self.box_output2=self.root.ids.texts_color_change_tow.color=0,1,0,1
            self.box_output=self.root.ids.text_input_one.text=""
            self.box_output2=self.root.ids.text_input_tow.text=""
            self.id_user+=1
            self.array[0]=self.id_user

            print(self.id_user)
            print(self.array)


       else:
            self.box_output2=self.root.ids.texts_color_change_one.color=1,0,0,1
            self.box_output2=self.root.ids.texts_color_change_tow.color=1,0,0,1
            self.box_output=self.root.ids.texts_color_change_one.text="Welcom"
            self.box_output2=self.root.ids.texts_color_change_tow.text="Please Enter user and pass"

                 


    #   
    #  print(self.box1)
    #    print(self.box2)

    
    def build(self):
        Window.size=(300,600)
        return Builder.load_file('style_information_user.kv')


if __name__=="__main__":
    TestApp().run()        
