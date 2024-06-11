# General Tree node creation

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None
        
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
    
    # Know the level of your current node
    def get_level(self):
        level = 0
        a = self.parent
        while a:
            level += 1
            a = a.parent
        return level
    
    def print_tree(self,level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""     # Ternary operator in python
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)
        
def build_product_tree():
    root = TreeNode("----- Khwopa Engineering College -----\nEngineering")
    department = TreeNode("Department")
    
    computer = TreeNode("Computer Science")
    department.add_child(computer)
    computer.add_child(TreeNode("Lakpa Sherpa(Student)"))
    
    department.add_child(TreeNode("Civil"))
    department.add_child(TreeNode("Electronics and Communication"))
    department.add_child(TreeNode("Architecture"))
    
    section = TreeNode("Section")
    
    section.add_child(TreeNode("Exam Section"))
    section.add_child(TreeNode("College Administration"))
    section.add_child(TreeNode("Account Section"))
    section.add_child(TreeNode("Library Section"))
    section.add_child(TreeNode("Technical Section"))
    section.add_child(TreeNode("Jinsi Section"))
    
    root.add_child(department)
    root.add_child(section)
    
    return root
    
if __name__ == '__main__':
    root = build_product_tree()
    #printing according to tree level
    root.print_tree(0)
    root.print_tree(1)
    root.print_tree(2)
    root.print_tree(3)
    pass



