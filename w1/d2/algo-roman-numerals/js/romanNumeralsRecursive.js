const toRoman = function (num) {
  let rn = {
    M: 1000,
    CM: 900,
    D: 500,
    CD: 400,
    C: 100,
    XC: 90,
    L: 50,
    XL: 40,
    X: 10,
    IX: 9,
    V: 5,
    IV: 4,
    I: 1,
  };

  let str = '';
  const recursive = (num, romanNumerals) => {
    if (num === 0) return;
    for (let [key, value] of Object.entries(rn)) {
      if (num >= value) {
        num -= value;
        str += key;
      }
    }
    recursive(num, romanNumerals);
  };
  recursive(num, rn);
  return str;
};
console.log(toRoman(1));

console.log(toRoman(1) === 'I');
console.log(toRoman(3) === 'III');
console.log(toRoman(4) === 'IV');
console.log(toRoman(999) === 'CMXCIX');
