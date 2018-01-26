/*
class Node
{
	int data;
	Node left,right;

	Node(int d)
	{
		data = d;
		left = right = null;
	}
}
*/

class GfG {
    /**
     * Check if a tree is balanced
     * Return Integer.MIN_VALUE if not balanced
     *
     * @param  Node root
     * @return
     */
    int checkHeight(Node root) {
        if (root == null) {
            return -1;
        }

        // calculate the height of the left child
        int leftHeight = checkHeight(root.left);
        // if left subtree not balanced, return MIN_VALUE
        if (leftHeight == Integer.MIN_VALUE) {
            return Integer.MIN_VALUE;
        }

        // same thing to the right child
        int rightHeight = checkHeight(root.right);
        if (rightHeight == Integer.MIN_VALUE) {
            return Integer.MIN_VALUE;
        }

        // look at the height difference between the left and right substrees
        if (Math.abs(rightHeight - leftHeight) > 1) {
            return Integer.MIN_VALUE;
        }

        return 1 + Math.max(rightHeight, leftHeight);

    }

    /* This function should return tree if passed  tree
    is balanced, else false.  Time complexity should
    be O(n) where n is number of nodes in tree */
    boolean isBalanced(Node root) {
        return checkHeight(root) != Integer.MIN_VALUE;
    }
}
