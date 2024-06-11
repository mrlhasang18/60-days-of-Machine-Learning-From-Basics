# A heirarchical Tree of a company

# Tree node creation

class TNode:
    def __init__(self,name,des):
        self.name = name
        self.children = []
        self.des = des
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
        
    def get_level(self):
        level = 0
        l = self.parent
        while l:
            level += 1
            l = l.parent
        return level
    
    def print_tree(self,name):
        
        if name == "name":
            value = self.name
        elif name == "both":
            value = self.name + "("+self.des+")"
            
        else:
            value = self.des
            
        space = ' ' * self.get_level() * 3
        prefix = space + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(name)            # Recursion
        
def company_tree():
    ceo = TNode("Lhasang","CEO")
    cto =  TNode("Nirmal","CTO")
    # below Nirmal
    ram = TNode("Ram","Infrastructure Head")
    cto.add_child(ram)
    cto.add_child(TNode("Pasang","Marketing Head"))
    # Below ram
    alex = TNode("Alex","Cloud Manager")
    ram.add_child(alex)
    ram.add_child(TNode("Hira","App Manager"))
    
    # Below Alex
    alex.add_child(TNode("Ritesh","DevOps Engineer"))
    
    # Below ram
    shyam = TNode("Shyam","Website Manager")
    ram.add_child(shyam)
    
    # below shyam
    shyam.add_child(TNode("Sita","Frontend Engineer"))
    shyam.add_child(TNode("Gita","Backend Engineer"))
    
    
    # Below Lhasang
    hr = TNode("Bhuwan","HR Head")
    # Below Bhuwan
    hr.add_child(TNode("Raj","Recruitment Manager"))
    hr.add_child(TNode("Hari","Policy Manager"))
    
    ceo.add_child(cto)
    ceo.add_child(hr) 
    return ceo

if __name__ == '__main__':
    root = company_tree()
    print("\n"+"-"*5+" Akbare.Inc Tree with just name"+"-"*5+"\n")
    root.print_tree("name")
    print("\n"+"-"*5+" Akbare.Inc Tree with just position"+"-"*5+"\n")
    root.print_tree("des")
    print("\n"+"-"*5+" Akbare.Inc Tree with both name and position"+"-"*5+"\n")
    root.print_tree("both")
    pass