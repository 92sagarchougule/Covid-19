class student:
    def personal(self, name, address):
        self.name = name
        self.address = address
        print("Name of candidate is {}".format(self.name))
        print("Address of candidate is {}".format(self.address))
    def eduction(self, degree, collage):
        self.degree = degree
        self.collage = collage
        print("He got {} Degreee".format(self.degree))
        print("His collage was {}".format(self.collage))
    def physic(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height
        print("Candidate age is {}".format(self.age))
        print("Candidate weight is {}".format(self.weight))
        print("Candidate heidht is {}".format(self.height))
