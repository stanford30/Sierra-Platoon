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

fetchArticleByID(1);
