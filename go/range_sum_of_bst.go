//no. 938
import tree

func rangeSumBST(root *TreeNode, low int, high int) int {
    var queue []*TreeNode
    queue = append(queue, root)
    ans := 0
    for{
        if len(queue) <= 0{
            break
        }
        var curr_node *TreeNode = queue[0]
        queue = queue[1:]
        if (curr_node != nil){
            if curr_node.Val > high{
                queue = append(queue, curr_node.Left)
            }else if curr_node.Val < low{
                queue = append(queue, curr_node.Right)
            }else{
                ans += curr_node.Val
                queue = append(queue, curr_node.Left)
                queue = append(queue, curr_node.Right)
            }
        }
    }
    return ans
}
