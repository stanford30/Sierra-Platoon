import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import { Link } from "react-router-dom";

// function ArticleTeaser (props){
function ArticleTeaser({ title, url, index }) {
  return (
    <Container>
      <hr />
      <Row>
        <Col lg="8">
          <h2>
            {/* <Link to={`/articles/${id+1}`} >{title} </Link> */}
            <p>
              {index + 1}. <a href={url}>{title}</a>
            </p>
          </h2>
        </Col>
        <Col lg="4">
          <p></p>
        </Col>
      </Row>
    </Container>
  );
}
export default ArticleTeaser;
