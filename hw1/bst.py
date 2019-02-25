# TODO check over code and functionality

class Node:
    def __init__(self, data):
        self.rightChild = None
        self.leftChild = None
        self.data = data

def insert(root, node):
    if root is None:
        root = node
    else:
        if node.data == root.data:
            return
        elif node.data > root.data:
            if root.rightChild is None:
                root.rightChild = node
            else:
                insert(root.rightChild, node)
        else:
            if root.leftChild is None:
                root.leftChild = node
            else:
                insert(root.leftChild, node)

def search(root, key, output):

    if root is None:
        print("not found")
        return
    if root.data == key:
        if output == "":
            output = "root"
        print("found: " + output)
        return
    else:
        if key > root.data:
            output += "r "
            return(search(root.rightChild, key, output))
        else:
            output += "l "
            return(search(root.leftChild, key, output))



def main():

    treeRoot = None
    i = 0
    #do file input for tree insertion and query
    while (True):
        try:
            line = input().split()
        except EOFError:
            exit(0)
        if line[0] == "i":
            insert(treeRoot, Node(int(line[1])))
            if treeRoot is None:
                treeRoot = Node(int(line[1]))
        elif line[0] == 'q':
            search(treeRoot, int(line[1]), "")
        i+=1

if __name__ == "__main__":
    main()