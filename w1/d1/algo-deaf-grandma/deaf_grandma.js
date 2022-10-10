function deafGrandma() {
  let running = true;
  let goodbye = 0;
  while (running) {
    let x = prompt();
    x = x.toString();

    if (x === 'GOODBYE!') {
      if (goodbye < 1) {
        console.log('LEAVING SO SOON?');
        goodbye++;
      } else {
        console.log('LATER, SKATER!');
        running = false;
      }
    } else if (x == '') {
      console.log('WHAT?!');
    } else if (x.toUpperCase() === x && !Number.isInteger(+x)) {
      console.log('NO, NOT SINCE 1964!');
    } else {
      console.log('SPEAK UP, KID!');
    }
  }
}

deafGrandma();
