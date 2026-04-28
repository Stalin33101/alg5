from collections import deque

# Узел дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#Вставка
def insert(root, value):
    if root is None:
        return TreeNode(value)
    
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    # если равны — не вставляем (в BST обычно без дубликатов)
    return root


#Поиск
def search(root, target):
    if root is None or root.value == target:
        return root is not None  
    if target < root.value:
        return search(root.left, target)
    else:
        return search(root.right, target)


#Симметричный обход 
def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(root.value)
        inorder(root.right, result)
    return result


def bfs(root):
    """Возвращает список значений узлов по уровням (слева направо)"""
    result = []
    if root is None:
        return result
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.value)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result



if __name__ == "__main__":
    root = None
    numbers = [50, 30, 70, 20, 40, 60, 80, 10, 35]
    
    for num in numbers:
        root = insert(root, num)
    
    print("Inorder (отсортированный):", inorder(root))
    print("Поиск 60:", search(root, 60))
    print("Поиск 100:", search(root, 100))
    print("BFS (обход в ширину):", bfs(root))
