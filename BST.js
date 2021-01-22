// A BST is a Binary Search Tree
// Its a data structure for quickly being able to perform binary search because it is sorted in a specific way.

const example = [10,7,14,20,1,5,8]

// In this example, the root node is 10.

class Node {
    
    constructor(val, left, right){
        this.val = val;
        this.left = left
        this.right = right
    }

    print() {
        console.log(this.val, this.left, this.right)
    }


}

// const testNode = new Node(3)
// testNode.print()

const buildBST = (arr) => {

    let root = new Node(arr[0])
    for (let i = 1; i < arr.length; i++){
        // build through arr.

        let newNode = new Node(arr[i])

        buildHelper(root, newNode)
    }

    console.log(root)
}

const buildHelper = (root, node) => {

    // given root, just iteratively put it down.

    while(root){
        // decide where 2 go first
        if (!root){
            return;
        }
        if (node.val > root.val){
            // go right
            if (!root.right){
                root.right = node;
                return;
            } else {
                // move root so i don't have to call this recursively
                
                root = root.right;
            }
            
        }

        if (node.val < root.val){
            // go left
            if (!root.left){
                root.left = node;
                return;
            } else {
                root = root.left
            }
            
        }

        
    }
}

buildBST(example)
