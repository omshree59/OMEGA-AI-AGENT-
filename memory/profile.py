class Profile:


    def __init__(self):

        self.profile = {}



    def update(self, key, value):

        self.profile[key] = value



    def get_profile(self):

        return self.profile