// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function (array) {
  //init answer array and length of number
  let ans = [];
  let len;
  // loop through input array
  array.forEach((num) => {
    // work through each number to see if it is an armstrong number
    num = num.toString();
    len = num.length;
    let sum = 0;
    for (a of num) {
      sum += a ** len;
    }
    if (sum === +num) {
      ans.push(+num);
    }
  });
  // return answer array
  return ans;
};
