// This is true split search
// const bSearch = (arr, target) => {
//     // assumes array is sorted
//      if (arr.length == 0){
//          return false
//      }
//      if (arr.length == 1){
//          return arr[0] == target
//      }
//      let midpt = Math.floor(arr.length/2);
//      let left = arr.slice(0,midpt);
//      let right = arr.slice(midpt);
//      return bSearch(left, target) || bSearch(right, target)
//  }

// lets try something a little closer

const bSearch = (arr, target) => {

    let searcharr = arr;
    let closest;
    while (searcharr.length > 0){
        console.log(searcharr)
        let midpt = Math.floor(searcharr.length/2)
        if (searcharr[midpt] == target){
            return true;
        }
        if(searcharr.length == 1){
            return searcharr[0]
        }
        if (searcharr[midpt] > target){
            // it has to be to the left
            searcharr = searcharr.slice(0, midpt)
        } else {
            searcharr = searcharr.slice(midpt)
        }
    }
}

 let test = [1,5,10,15,20,25,30]
 let res =bSearch(test, 17)
 console.log(res)