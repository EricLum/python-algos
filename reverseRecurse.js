var reverseString = function(s) {
    
    return reverse(s)
};

var reverse = (s) => {
    if (s.length == 0 || s.length == 1){
        return s;
    }
    
    return s[s.length-1] + reverse(s.slice(1, s.length-1)) + s[0]
}


// in place
var reverseString = function(s) {
    var helper = function(left, right) {
        if (left < right){
            
            let temp = s[left]
            s[left] = s[right]
            s[right] = temp
            
            helper(left + 1, right -1)
        }
    }
    
    helper(0, s.length-1)
    
};


console.log(reverseString(['h', 'e', 'l', 'l', 'o']))