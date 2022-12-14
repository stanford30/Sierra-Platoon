import axios from "axios";

export const fetchArticleByID = async (id) => {
  const url = `http://hn.algolia.com/api/v1/items/${id}`;
  const res = await axios
    .get(url, {
      headers: {
        "Content-Type": "blob",
        // "Content-Encoding": "gzip",
        // "Accept-Encoding": "gzip,deflate",
      },
    })
    .then((response) => {
      console.log(response);
    });
};

export const fetchArticleBySection = async (sectionName, setArticles) => {
  const url = `https://hacker-news.firebaseio.com/v0/${sectionName}stories.json?print=pretty`;
  const res = await axios.get(url);
  const promises = [];
  for (let i = 0; i < 10; i++) {
    promises.push(
      axios.get(
        `https://hacker-news.firebaseio.com/v0/item/${res.data[i]}.json`
      )
    );
  }
  Promise.all(promises).then((responses) => {
    setArticles(
      responses.map((response) => {
        return response.data;
      })
    );
  });
  // console.log(res.data);
};
