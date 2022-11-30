import Form from "react-bootstrap/Form";
import { useState, useEffect } from "react";
import ArticleTeaser from "../components/ArticleTeaser";
import axios from "axios";

function Search({ articles }) {
  const [searchTitle, setSearchTitle] = useState("");
  const [results, setResults] = useState([]);

  const handleChange = (event) => {
    const value = event.target.value;
    console.log(`${value} val changed`);

    setSearchTitle(value);
  };

  useEffect(() => {
    if (searchTitle != "") {
      //   const filteredArticles = articles.filter((article) =>
      //     article.title.includes(searchTitle)
      //   );
      const filteredArticles = axios
        .get(
          `http://hn.algolia.com/api/v1/search?query=${searchTitle}&tags=story`,
          { params: { hitsPerPage: 30 } }
        )
        .then((res) => {
          //   return res.data.hits;
          setResults([...res.data.hits]);
          //   console.log(res);
        });
      //   setResults(filteredArticles);
    } else {
      setResults([]);
    }
  }, [searchTitle]);
  console.log(results);

  return (
    <div>
      <Form>
        <Form.Control
          type="search"
          placeholder="Search"
          aria-label="Search"
          onChange={(event) => {
            handleChange(event);
          }}
        />
      </Form>
      <div>
        {results.length > 0 ? (
          <div>
            <h2>search results</h2>
            {results.map((article) => (
              <ArticleTeaser key={article.id} {...article} />
            ))}
          </div>
        ) : (
          ""
        )}
      </div>
    </div>
  );
}

export default Search;
