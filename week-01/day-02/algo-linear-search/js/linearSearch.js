const arrayToSearchThrough = [];
for (let i = 1; i <= 1000; i++) {
  arrayToSearchThrough.push(i);
}

exports.linearSearch = function (valueToFind, arrayToSearchThrough) {
  // your code here

  return arrayToSearchThrough.indexOf(valueToFind) === -1
    ? undefined
    : arrayToSearchThrough.indexOf(valueToFind);
};

exports.linearSearchGlobal = function (valueToFind, arrayToSearchThrough) {
  // your code here
  let arr = [];
  arrayToSearchThrough.forEach((val, idx) => {
    if (val === valueToFind) {
      arr.push(idx);
    }
  });
  return arr;
};
