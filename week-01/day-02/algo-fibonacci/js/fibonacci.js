const fibonacci = (num) => {
  //recursive solution
  //declare the variables for num
  if (num <= 0) return 0;
  if (num === 1) return 1;
  // return the fibonacci sequence
  return fibonacci(num - 1) + fibonacci(num - 2);
};

module.exports = { fibonacci };
