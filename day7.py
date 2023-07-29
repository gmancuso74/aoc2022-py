from Models import Solution
from enum import Enum

class Type(Enum):
    D = 'dir'
    F = 'file'

class Node:
    name : str
    type : Type
    children : list
    parent : 'Node|None' 
    size : int

    def __init__(self, name: str, type: Type, parent: 'Node|None'=None):
        self.name = name
        self.type = type
        self.parent=parent
        self.children=list()

    def add(self,child: 'Node'):
        self.children.append(child)
    
    def get_size(self):
        match(self.type):
            case Type.D:
                total=0
                for child in self.children:
                    total=total+child.get_size()
                return total
            case Type.F:
                return self.size

class Day7(Solution):
    pwd : Node
    root : Node

    def __init__(self):
        super().__init__(day=7)
        self.root=Node('/',Type.D)
        self.pwd=self.root

    def process(self,line:str):
        if line.startswith('$ ls'):
            pass
        elif line.startswith('$ cd'):
            (prompt,left,right)=line.split(' ')
            match(right):
                case '..':  
                    if(self.pwd.parent is None): raise Exception(f'No parent directory for {self.pwd.name}')
                    self.pwd=self.pwd.parent
                case '/':
                    self.pwd=self.root
                case _: 
                    new_pwd=None
                    for child in self.pwd.children:
                        if(child.name==right): new_pwd=child
                    if(new_pwd is None): raise Exception(f'No child named {right}')
                    self.pwd=new_pwd
        else:
            (left,right)=line.split(' ')
            if(left=='dir'):
                node=Node(right,Type.D,self.pwd)
                self.pwd.add(node)
            else:
                node=Node(right,Type.F, self.pwd)
                node.size=int(left)
                self.pwd.add(node)

    def node_summary(self,node:Node) -> str:
        match(node.type):
            case Type.D:
                return f'{node.name} (dir, size={node.get_size()})'
            case Type.F:
                return f'{node.name} (file, size={node.size})'

    def print_tree(self,node:Node,depth:int=0):
        """Print out the tree like the example"""
        d_tabs=' '*depth
        print (f'{d_tabs}- {self.node_summary(node)}')
        for child in node.children:
            self.print_tree(child,depth+1)
        
    def dir_print(self,node:Node, depth:int =0):
        if(node.type==Type.D):
            d_tabs=' '*depth
            print (f'{d_tabs}+{node.name}: {node.get_size()}')
        for child in node.children:
            self.dir_print(child,depth+1)

    def part1(self):
        for line in self.input():
            self.process(line)
        self.print_tree(self.root)
        return 0

    def part2(self):
        return 0

if __name__ == '__main__':
    day = Day7()
    day.printResults()
