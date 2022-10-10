function bottleSong() {
  // Write your code here!
  // init variables
  let bottles = 99;
  let arr = [];
  for (bottles; bottles > 1; bottles--) {
    let str = `
    ${bottles} bottles of beer on the wall, ${bottles}  bottles of beer.
    Take one down and pass it around, ${bottles - 1} ${
      bottles === 2 ? 'bottle' : 'bottles'
    } of beer on the wall.`;

    arr = [...arr, str];
  }
  let ending = `
  1 bottle of beer on the wall, 1 bottle of beer.
  Take one down and pass it around, no more bottles of beer on the wall.
  No more bottles of beer on the wall, no more bottles of beer.
  Go to the store and buy some more, 99 bottles of beer on the wall.`;
  arr.push(ending);
  console.log(arr.join('\n'));
}
bottleSong();
