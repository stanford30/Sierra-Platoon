const helper = (n) => {
  if (!n || n === 1) return 1;
  return n * helper(n - 1);
};

exports.factorial = function (num) {
  return helper(num);
  // return num * exports.factorial(num--);
};
