
class BackView:
    
    def back(self):
        self.controller.show_frame("main")
        
class GoTo:
    
    def show_frame(self):
        self.controller.show_frame(self.name)
        

class Helper(BackView,GoTo):
    pass