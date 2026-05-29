class Member:
    BMI_Limit = 50
    def __init__(self , name , height , weight):
        self.name = name
        self.height = height
        self.weight = weight
    def calculation(self):
        bmi =  self.weight - (self.height * self.weight)
        if bmi > Member.BMI_Limit:
            print("FIT")
        else:
            print("UNFIT")
    @classmethod
    def update(cls , new):
        cls.BMI_Limit = new
    @staticmethod
    def check(height , weight):
        return height > 0 and weight > 0