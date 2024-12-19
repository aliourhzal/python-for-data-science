from S1E7 import Baratheon, Lannister

class King(Lannister, Baratheon):

    def set_eyes(self, new_eyes):
        self.eyes = new_eyes

    def set_hairs(self, new_hairs):
        self.hairs = new_hairs

    def get_eyes(self):
        return self.eyes
    
    def get_hairs(self):
        return self.hairs