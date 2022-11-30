import ArticleTeaser from "./ArticleTeaser";

function ArticleList({ articles }) {
  const HandleTitleClick = (article_id) => {
    console.log(article_id);
  };

  return (
    <div>
      {articles.map((article, index) => (
        <ArticleTeaser key={article.id} {...article} index={index} />
      ))}
    </div>
  );
}

export default ArticleList;
