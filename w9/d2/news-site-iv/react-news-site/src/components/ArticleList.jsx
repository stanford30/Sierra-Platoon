import ArticleTeaser from "./ArticleTeaser";

function ArticleList({ articles }) {
  const HandleTitleClick = (article_id) => {
    console.log(article_id);
  };

  return (
    <div>
      {articles.map((article, index) => {
        // console.log(article.title);

        return (
          <>
            {/* <h3>{index}</h3> */}
            <ArticleTeaser key={article.title} {...article} index={index} />
          </>
        );
      })}
    </div>
  );
}

export default ArticleList;
