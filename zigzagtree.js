var test = function(label) {
  let results = [];
  let nodes = 1;
  let level = 1;
  // uses min per level rule implicitly since tree increases by a power of 2 each level.
  // funny enough this is the valence shell calculation in atoms.
  // 0                               - 1
  // 0 0                             - 2
  // 0 0 0  0                        - 4 
  // 0 0 0 0 0 0 0 0                 - 8
  // 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 - 16
  while (label >= nodes*2){
      nodes *=2
      level+=1
  }
  while (label > 0) {
      results.unshift(label)
      let maxNodes = 2 **(level) - 1
      let minNodes = 2 ** (level-1);
      label = Math.floor((maxNodes+minNodes - label)/2)
      level -=1
  }

  return results;
};

let res = test(14);

console.log(res);

// key results