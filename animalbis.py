'''Creating generation of animals'''
# encoding : utf8

class Animal():
    '''Create Animal class, like a "blueprint" for creating objects'''
    def __init__(self, name, species, age, foot, diet) -> None:
        '''Defining initial attributes that behave like global variables
        for all methods of this class.
        Creating an empty list of children and another containing only their name.
        Initialing the mother related attributes'''
        self.species = species
        self.age = age
        self.diet = diet
        self.foot = foot
        self.name= name
        self.children = []
        self.child_name=[]
        self.mother= None
        self.mother_name= "Unknown"


    def set_species(self, species) :
        '''function enabling to define species'''
        self.species = species

    def set_foot_nb(self, foot) :
        '''function enabling to define number of feet'''
        self.foot = foot

    def set_age(self, age):
        '''function enabling to define age'''
        self.age = age

    def set_diet(self, diet):
        '''function enabling to define diet'''
        self.diet = diet

    def set_name(self, name):
        '''function enabling to define name'''
        self.name = name


    def add_children(self,child_name,child_age) -> None:
        '''function enabling to add children'''
        # create a child that is an animal and who has a given name and age
        # other attributes are inherited from the mother
        child=Animal(child_name,self.species,child_age,self.foot,self.diet)
        # if the created child isn't in children list,
        # add child object and child name in respective list
        if child not in self.children:
            self.children.append(child)
            self.child_name.append(child_name)
            # updating child's mother related attributes
            # using the name of the current object as the child's mother name
            child.mother= self
            child.mother_name=self.name
            # stock in the variable your_mother the mother of the current object:
            # child's grandmother
            your_mother=self.mother
            while your_mother: #while child's grandmother exists
                for kid in self.children:
                    # if the kid and its name not in  grandmother's list of children, add it
                    if str(kid.name) not in your_mother.child_name:
                        your_mother.child_name.append(kid.name)
                        your_mother.children.append(kid)
                # stock in the variable your_mother the mother of the current mother:
                # child's great grandmother
                your_mother=your_mother.mother
        return child

    def remove_children(self,child,child_name) -> None:
        '''function enabling to remove children'''
        # delete the child of the children related lists from the current object
        self.children.remove(child)
        self.child_name.remove(child_name)
        child.mother= self
        child.mother_name=self.name
        your_mother=self.mother
        #for each kid of the removed child
        #if this kid is in children related lists from the current object
        # delete it
        for kid in child.children:
            if str(kid.name) in self.child_name:
                self.child_name.remove(kid.name)
                self.children.remove(kid)
        while your_mother:
            # if the child's name appears in child_name from grandmother, delete it
            if child_name in your_mother.child_name:
                your_mother.child_name.remove(child_name)
                your_mother.children.remove(child)
                for kid in child.children:
                   # if the kid of the remove child appears in child_name
                   # from grandmother, delete it
                    if str(kid.name) in your_mother.child_name :
                        your_mother.child_name.remove(kid.name)
                        your_mother.children.remove(kid)
                    #until your_mother=None
                your_mother=your_mother.mother
        return child

    def __str__(self) -> str:
        if self.child_name:
            return  self.name+ " is a/an " + self.species + " who is " + str(self.age) +\
            " years old," + " her diet is " + self.diet + " and have " + str(self.foot)  +\
            " feet\n " + "Her descendants are:  " + str(self.child_name) +\
            " and her mother is : " + str(self.mother_name)
        else:
            return self.name+ " is a/an " + self.species + " who is " +\
            str(self.age) + " years old, " + " her diet is " +\
            self.diet + " and have " + str(self.foot)  + " feet\n " +\
            "Her mother is " + str(self.mother_name)+ " and she doesn't have kids"


class Homme(Animal):
    '''Create Human class, like a "blueprint" for creating objects'''
    def __init__(self,name, age) -> None:
        # super() allows to access methos of the Animal class
        #incremating certain attributes
        super().__init__(name,"Homme", age, 2, "Ominovre")
    def __str__(self) -> str:
        return super().__str__()

if __name__ == "__main__":

    animal1= Animal("toma","dog",9,4,"carnivore")
    animal2= animal1.add_children("Vincenta",1)
    animal3= animal1.add_children("Eliota",5)
    animal4= animal2.add_children("Kelopsa",8)
    animal5=animal4.add_children("Rolanda",10)
    animal6=animal5.add_children("Gaspera",5)
    print(animal1)
    print(animal2)
    print(animal3)
    print(animal4)
    print(animal5)

    animal4.remove_children(animal5, "Rolanda")

    animal1 = Homme("Olivia", 50)
    animal2 = animal1.add_children("manon",40)
    animal3 = animal1.add_children("ksenija", 23)
    animal4=animal2.add_children("Lou",20)
    animal5=animal4.add_children("olha",2)
    print(animal1)
    print(animal2)
    print(animal3)
    print(animal4)

    animal2.remove_children(animal4,"Lou")
