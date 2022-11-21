function ArticleTeaser({ id, title, created_date, handleTitleClick }) {
  return (
    <div>
      <a onClick={() => handleTitleClick(id)}>{title}</a>
      <p>{created_date}</p>
    </div>
  );
}

export default ArticleTeaser;
