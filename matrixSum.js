var matrixBlockSum = function(mat, K) {
    
    
    let addBlock = (xLow, xHigh, yLow, yHigh) => {
        let sum = 0;
        for ( let i = xLow ; i< xHigh+1; i++){
            for (let j = yLow; j<yHigh+1; j++){
                sum+=mat[i][j]
            }
        }       
        return sum
    }
    if (mat.length == 0){
        return 0
    }
    let matrixSum = [...mat]
    for (let r = 0; r < mat.length; r++){
        for (let c = 0; c < mat[0].length; c++){

            console.log(r,c)
            
            let xLow = Math.max(0, r-K)
            let xHigh = Math.min(mat.length-1, r+K)
            
            let yLow = Math.max(0, c-K)
            let yHigh = Math.min(mat[0].length-1, c+K)
 
            matrixSum[r][c] = addBlock(xLow, xHigh, yLow, yHigh)
            console.log(matrixSum)
        }
    }
    
    return matrixSum;
    
};

let mat = [[1,2,3],[4,5,6],[7,8,9]]
console.log(matrixBlockSum(mat, 1))