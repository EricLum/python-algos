var solveNQueens = function(n) {
    let results = [];
    let board = Array(n);
    for(let i = 0; i < n; i++) {
        board[i] = "";
        for(let j = 0; j < n; j++) {
            board[i] += "." 
        }
    }
    
    findQueens(board, n, results, 0);
    console.log(results)
    return results;
};

function findQueens(board, n, results, col) {
    if (col >= n) {
        let newBoard = [...board];        
        results.push(newBoard);
        return;
    }
    
    for(let i = 0; i < n; i++) {        
        if (isSafeSpace(board, n, i, col)) {
            board[i] = replaceAt(board[i], col, "Q");
            findQueens(board, n, results, col + 1);
            board[i] = replaceAt(board[i], col, ".");
        }
    }
}


function isSafeSpace(board, n, row, col) {
    // check cols
    for(let i = 0; i < col; i++) {
        if (board[row][i] == "Q") {
            return false;
        }
    }
    
    // check upper left diag
    for(let i = row, j = col; i >= 0 && j >= 0; i--, j--) {
        if (board[i][j] == "Q") {
            return false;
        }
    }
    
    // check lower left diag
    for(let i = row, j = col; i < n && j >= 0; i++, j--) {
        if (board[i][j] == "Q") {
            return false;
        }
    } 
    
    return true;
}

function replaceAt(s, index, c) {
    return s.slice(0, index) + c + s.slice(index + 1, s.length);
}

solveNQueens(4)