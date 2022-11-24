import ArticleList from '../components/ArticleList/ArticleList.jsx';
import News from '../data/news.json';
import { useNavigate } from 'react-router-dom';
import { Link } from 'react-router-dom';

function HomePage() {
  let navigateTo = useNavigate();
  const handleTitleClick = (articleID) => {
    navigateTo(`/articles/${articleID}`);
    console.log(articleID);

    // <Link to="/#/articles/1"> title </Link>;
  };
  // console.log(
  //   "TODO - use React Router's history.push() method to change the page to /article/${articleID}"
  // );
  // <Link to=`/articles/${articleID}`>title</Link>

  return (
    <div>
      <ArticleList articles={News} handleTitleClick={handleTitleClick} />
    </div>
  );
}

export default HomePage;
