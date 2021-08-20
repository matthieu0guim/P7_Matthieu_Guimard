from exo2_arbres_livres import BinaryTree

actions = ['a', 'b', 'c']
a, b, c = None, None, None
actionsTree = [a, b, c]
for n, action in enumerate(actions):
    actionsTree[n] = BinaryTree(action)
    if n !=0:
        # print(actionsTree[n - 1])
        actionsTree[n].parent = actionsTree[n - 1]
        actionsTree[n - 1].insertRight(actionsTree[n])
        actionsTree[n - 1].insertLeft(actionsTree[n])

        print(f'Enfant: {actionsTree[n].getRootVal()}')
        print(f"Parent: {actionsTree[n].parent.getRootVal()}")

print("deuxième mouvement")
# for n, action in enumerate(actions):
#     print(f"Parent:  {actionsTree[n].getRootVal()}")
#     print(f"Left child: {actionsTree[n].getLeftChild()}")
#     print(f"Right child: {actionsTree[n].getRightChild()}")

print(actionsTree[0].getRootVal())
print(actionsTree[0].leftChild.getRootVal())
print(actionsTree[0].rightChild.getRootVal())
print(f"Config: {actionsTree[2].rightChild.config}")


