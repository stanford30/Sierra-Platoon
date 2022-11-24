// import './App.css';
import { useState } from 'react';
// data
import News from './data/news.json';
import navItemsData from './data/navItems.json';
// components
import AppNav from './components/AppNav/AppNav.jsx';

import { HashRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ArticlePage from './pages/ArticlePage';
// seed values
// const randomArticleIndex = Math.floor(Math.random() * News.length);
// const randomArticle = News[randomArticleIndex];

function App() {
  // states
  const [navItems, setNavItems] = useState(navItemsData);

  // console.log(article);

  const handleNavClick = (clickedItem) => {
    console.log(clickedItem);
  };

  const handleTitleClick = (articleID) => {
    console.log(articleID);
  };

  // renders
  return (
    <div>
      <h1>AppNav Component</h1>
      <hr />
      <AppNav
        navItems={navItems}
        handleNavClick={(clickedItem) => console.log(clickedItem)}
      />
      <Router>
        <div>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/articles/:articleID" element={<ArticlePage />} />
          </Routes>
        </div>
      </Router>
    </div>
  );
  // return (
  //   <div>
  //     <h1>AppNav Component</h1>
  //     <hr />
  //     <AppNav navItems={navItems} handleNavClick={handleNavClick} />
  //     <h1>ArticleTeaser Component</h1>
  //     <hr />
  //     <ArticleTeaser
  //       id={article.id}
  //       title={article.title}
  //       created_date={article.created_date}
  //       handleTitleClick={handleTitleClick}
  //     />
  //     <h1>Article Component</h1>
  //     <hr />
  //     <Article {...article} />
  //   </div>
  // );
}

export default App;
