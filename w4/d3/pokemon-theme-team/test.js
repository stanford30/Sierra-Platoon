// const axios = require('axios');
const searchBtn = document.querySelector('.search-button');
const imagesDiv = document.querySelector('.images');

const search = async () => {
  try {
    imagesDiv.innerHTML = '';
    const num = Math.floor(Math.random() * 1000);
    const apiUrl = `https://pokeapi.co/api/v2/`;
    let type;
    await axios.get(apiUrl + `pokemon/${num}`).then((response) => {
      type = response.data.types[0].type.name;
    });
    console.log(type);
  } catch (e) {
    console.log(e);
    await search();
  }
  // console.log('hello world');
};

const getRandomPokemon = async (type) => {
  try {
    const apiUrl = `https://pokeapi.co/api/v2/type/${type}`;
    const pokemonImgUrl = await axios.get(apiUrl).then((response) => {
      return response;
    });
  } catch (e) {
    console.log(e);
    await getRandomPokemon();
  }
};
// searchBtn.addEventListener('mousedown', search);
