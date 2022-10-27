console.log('hello world');

const pokemonTypeDiv = document.getElementById('pokemon-type'); // only works for grabbing HTML id's
const pokemonImagesDiv = document.querySelector('#pokemon-images'); // grabs element by query selector I.E. '#' for id, '.' for classes

const getPokemonTheme = () => {
  pokemonImagesDiv.innerHTML = '';
  const randNum = Math.floor(Math.random() * 300);
  const api = `https://pokeapi.co/api/v2/pokemon/${randNum}`;
  axios.get(api).then((response) => {
    console.log(response.data.types[0].type.name);
    const type = response.data.types[0].type.name;
    pokemonTypeDiv.innerHTML = `<h1>${type}</h1>`;
    //create elements: div, img, and label
    // const img = document.createElement('img');
    // const div = document.createElement('div');
    // const label = document.createElement('label');
    // img['src'] = response.data['sprites']['front_default'];
    // label.innerHTML = response.data['name'];
    // div.appendChild(img);
    // div.appendChild(label);
    // pokemonImagesDiv.appendChild(div);
    createImg(response.data['sprites']['front_default'], response.data['name']);
    for (let i = 0; i < 5; i++) {
      getPokemonByType(type);
    }
  });
};

const getPokemonByType = (type) => {
  const api = `https://pokeapi.co/api/v2/type/${type}`;
  axios.get(api).then((response) => {
    const randNum = Math.floor(Math.random() * response.data.pokemon.length);
    console.log(response.data.pokemon[randNum]);
    const name = response.data.pokemon[randNum].pokemon.name;
    const url = response.data.pokemon[randNum].pokemon.url;
    // console.log(name, url);
    axios.get(url).then((response) => {
      if (response.data['sprites']['front_default'] == null) {
        getPokemonByType(type);
      } else {
        createImg(
          response.data['sprites']['front_default'],
          response.data['name']
        );
      }
    });
  });
};

const createImg = (url, name) => {
  const img = document.createElement('img');
  const div = document.createElement('div');
  const label = document.createElement('label');
  // img['src'] = response.data['sprites']['front_default'];
  img['src'] = `${url}`;
  // label.innerHTML = response.data['name'];
  label.innerHTML = `${name}`;
  div.appendChild(img);
  div.appendChild(label);
  div.style.display = 'flex';
  div.style.flexDirection = 'column';
  div.style.alignItems = 'center';
  pokemonImagesDiv.appendChild(div);
};
