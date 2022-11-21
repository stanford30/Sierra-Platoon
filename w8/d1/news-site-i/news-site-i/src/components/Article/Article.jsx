function Article(props) {
  return (
    <div>
      <h1>{props.title}</h1>
      <p>{props.created_date}</p>
      {props.byline && <h2>{props.byline}</h2>}
      {props.image && <img src={props.image}></img>}
      <p>{props.abstract}</p>
    </div>
  );
}

export default Article;
