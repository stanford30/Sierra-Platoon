import { Link } from 'react-router-dom';

function ArticleList(props) {
  console.log(props);

  return (
    <div>
      {props.articles.map((article, index) => {
        return (
          <>
            <p {...article} onClick={() => props.handleTitleClick(index)}>
              {article.title}
            </p>
            {/* <Link to={`/articles/${article.id}`}>{article.title}</Link> */}
          </>
        );
      })}
    </div>
  );
}

export default ArticleList;
