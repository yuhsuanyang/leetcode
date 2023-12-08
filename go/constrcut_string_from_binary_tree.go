//no. 606
import tree

func preorder_traverse(root *tree.TreeNode, ans *string)  {
    if root != nil{
        *ans += strconv.Itoa(root.Val)
    }
    if root.Left != nil{
        *ans += "("
        *ans += tree2str(root.Left)
        *ans += ")"
    }
    if root.Right != nil{
        if root.Left == nil{
            *ans += "()"
        }
        *ans += "("
        *ans += tree2str(root.Right)
        *ans += ")"
    }
    if (root.Left != nil) && (root.Right != nil){
        return
    }
}
func tree2str(root *tree.TreeNode) string{
    var ans = ""
    preorder_traverse(root, &ans)
    return ans
}
