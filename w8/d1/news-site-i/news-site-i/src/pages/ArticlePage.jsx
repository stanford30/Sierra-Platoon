import Article from '../components/Article/Article.jsx';
import News from '../data/news.json';
import { useParams } from 'react-router-dom';

function ArticlePage(props) {
  let { articleID } = useParams();
  console.log(props);

  return (
    <div>
      <div>article page</div>
      <div>Article ID: {articleID}</div>
      <div></div>
    </div>
  );
}

export default ArticlePage;
