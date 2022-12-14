import { useState, useEffect } from "react";
import axios from "axios";

import "./App.css";

import AppNav from "./components/AppNav";
import HomePage from "./pages/HomePage";
import ArticlePage from "./pages/ArticlePage";
import SectionPage from "./pages/SectionPage";

import NewsData from "./data/news.json";

import { HashRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  // const [articles, setArticles] = useState(
  //   NewsData.map((article, index) => {
  //     return {
  //       id: index,
  //       title: article.title,
  //       abstract: article.abstract,
  //       byline: article.byline,
  //       // image: article.multimedia.length ? article.multimedia[0] : null,
  //       created_date: article.created_date,
  //       section: article.section,
  //     };
  //   })
  // );
  const [articles, setArticles] = useState([]);
  const fetchArticleByID = async (id) => {
    const url = `http://hn.algolia.com/api/v1/items/${id}`;
    const res = await axios.get(url).then((response) => {
      console.log(response);
    });
  };
  // fetchArticleByID(1);

  const getFrontPage = async () => {
    const response = await axios
      .get("http://hn.algolia.com/api/v1/search?tags=front_page", {
        params: {
          hitsPerPage: 30,
        },
      })
      .then((res) => {
        // console.log(res.data.hits);
        setArticles([...res.data.hits]);
      });
    // console.log(response);
  };
  useEffect(() => {
    getFrontPage();
  }, []);
  // console.log(articles);

  return (
    <div className="App">
      <AppNav />
      {/* <HomePage articles={articles} /> */}
      <Router>
        <Routes>
          <Route path="/" element={<HomePage articles={articles} />} />
          <Route
            path="/articles/:articleID"
            element={<ArticlePage articles={articles} />}
          />
          <Route
            path="/sections/:sectionName"
            element={<SectionPage articles={articles} />}
          />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
