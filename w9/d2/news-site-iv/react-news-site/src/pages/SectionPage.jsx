import { useParams } from "react-router-dom";
import { useEffect, useState } from "react";
import ArticleList from "../components/ArticleList";
import { fetchArticleBySection } from "../js/articlesAPI";

function SectionPage({ articles }) {
  const { sectionName } = useParams();
  //   console.log(sectionName);

  const [sectionArticles, setSectionArticles] = useState([]);

  useEffect(() => {
    // const filteredAtricles = articles.filter(
    //   (article) => article.section.toLowerCase() == sectionName.toLowerCase()
    // );

    // setSectionArticles(filteredAtricles);

    // console.log(filteredAtricles);
    fetchArticleBySection(sectionName, setSectionArticles);
  }, [sectionName]);

  return (
    <div>
      {sectionArticles ? (
        <ArticleList articles={sectionArticles} />
      ) : (
        "no articles found"
      )}
    </div>
  );
}

export default SectionPage;
