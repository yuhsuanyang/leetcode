class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_linked_list(list_):
    if not len(list_):
        return None
    if len(list_) == 1:
        return ListNode(list_[0])
    else:
        list_ = list_[::-1]
        head = ListNode(list_[1])
        head.next = ListNode(list_[0])
        for i in list_[2:]:
            new_node = ListNode(i)
            new_node.next = head
            head = new_node
        return head

def print_linked_list(head):
    curr = head
    list_of_ele = []
    while curr:
        list_of_ele.append(str(curr.val))
        curr = curr.next
    print('->'.join(list_of_ele))


def insert_tree_node(val, root):
    node_list = [root]
    i = 0
    while True:
        temp = node_list[i]
        if temp.left:
            node_list.append(temp.left)
        else:
            temp.left = TreeNode(val)
            node_list[i] = temp
            break
        if temp.right:
            node_list.append(temp.right)
        else:
            temp.right = TreeNode(val)
            node_list[i] = temp
            break
        i += 1

def insert_binary_search_tree(val, root):
    if not root:
        return TreeNode(val)
    if val == root.val:
        return root
    if val < root.val:
        root.left = insert_binary_search_tree(val, root.left)
    elif val > root.val:
        root.right = insert_binary_search_tree(val, root.right)
    return root


def tree2list(root):
    cache = [root]
    node_list = [root.val]
    while len(cache):
        temp = cache.pop(0)
        if temp.left:
            cache.append(temp.left)
            node_list.append(temp.left.val)
        else:
            node_list.append(None)
        if temp.right:
            cache.append(temp.right)
            node_list.append(temp.right.val)
        else:
            node_list.append(None)
    return node_list


        
if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    linked_list = create_linked_list(sample)
    print_linked_list(linked_list)
    sample_tree = TreeNode(0)
    sample_bst = TreeNode(2)
    for i in range(1, 6):
        insert_tree_node(i, sample_tree)
    for i in [1, 3, 4]:
        sample_bst = insert_binary_search_tree(i, sample_bst)

    print(tree2list(sample_tree))
    print(tree2list(sample_bst))
#    bst = TreeNode(2, TreeNode(1), TreeNode(3))
#    bst = insert_binary_search_tree(4, bst)
#    print(tree2list(bst))
    
