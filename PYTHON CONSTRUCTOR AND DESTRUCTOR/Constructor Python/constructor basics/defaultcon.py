"""When we do not include the constructor in the class or
forget to declare it, then 
that becomes the default constructor. It does not perform any task 
but initializes the objects. Consider the following example."""

class default:
    default_val = 5442952
    default_name = "Jones_kwyboardist"
    def display(self):
        print(self.default_name,self.default_val)
de1 = default()
de1.display()