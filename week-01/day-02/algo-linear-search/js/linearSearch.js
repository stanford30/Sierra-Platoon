const arrayToSearchThrough = [];
for (let i = 1; i <= 1000; i++) {
  arrayToSearchThrough.push(i);
}

exports.linearSearch = function (valueToFind, arrayToSearchThrough) {
  // returns undefined if array === -1 (unfound)
  return arrayToSearchThrough.indexOf(valueToFind) === -1
    ? undefined
    : // else returns index if value is found in array.
      arrayToSearchThrough.indexOf(valueToFind);
};

exports.linearSearchGlobal = function (valueToFind, arrayToSearchThrough) {
  // initiate the array.
  let arr = [];
  // use forEach function
  arrayToSearchThrough.forEach((val, idx) => {
    // if value === valueToFind
    if (val === valueToFind) {
      // push idx into array
      arr.push(idx);
    }
  });
  // return array with all idx
  return arr;
};
