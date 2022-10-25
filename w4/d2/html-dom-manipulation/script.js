const replaceImages = async () => {
  // console.log('Hello World');
  imgs = document.body.getElementsByTagName('img');
  // console.log(imgs);
  // for (let i = 0; i < imgs.length; i++) {
  //   console.log(imgs[i]);
  // }
  for (let i = imgs.length - 1; i >= 0; i--) {
    console.log(imgs[i]);

    let image = imgs[i];

    if (image.alt) {
      // let text = document.createTextNode(image.alt);
      p = document.createElement('p');
      p.textContent = image.alt;
      p.classList.add('text');
      image.parentNode.replaceChild(p, image);
      // console.log(p);

      // image.parentNode.replaceChild(text, image);
    }
  }
};
