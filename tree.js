class Node {
    
    constructor(val, left, right){
        this.val = val;
        this.left = left;
        this.right = right;
    }


}
let test1 = new Node(2)
let test2 = new Node(3)
let test = new Node(1, test1, test2)

function traverse(node){
    
    let nodes = [node]

    while (nodes.length){
        let current = nodes.shift();
        console.log(current.val)
        if (current.left){
            nodes.push(current.left)
        }

        if (current.right){
            nodes.push(current.right)
        }
    }
}


const height = (node) => {
    if(!node){
        return 0
    }
    return Math.max(height(node.left), height(node.right)) + 1
}

let testHeight = height(test)
console.log(testHeight)
// traverse(test)