// const helper = (n) => {
//   if (!n || n === 1) return 1;
//   return n * helper(n - 1);
// };

exports.factorial = function (num) {
  // return helper(num);
  if (!num || num === 1) return 1;
  return num * this.factorial(num - 1);
  // return num * exports.factorial(num--);
};
