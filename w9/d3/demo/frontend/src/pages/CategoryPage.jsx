import React from "react";
import axios from "axios";
// import { useEffect } from "react";
import { useEffect, useState } from "react";

// import getCookie from "../js/utils";

function CategoryPage() {
  const [categories, setCategories] = useState([]);

  const mapItems = (c) => {
    return c.items.map((title) => {
      // console.log(title);

      return <li className="category-item">{title}</li>;
    });
  };

  const mapCategory = (c) => {
    return c.map((category) => {
      return (
        <>
          <h1>{category.title}</h1>
          <ul>{mapItems(category)}</ul>
        </>
      );
    });
  };

  const getCategories = async () => {
    try {
      // const csrftoken = getCookie("csrftoken");
      // axios.defaults.headers.common["X-CSRFToken"] = csrftoken;
      const response = await axios.get("api/categories");
      // console.log(response.data);

      setCategories(response.data);
    } catch (e) {
      console.log(e);
    }
  };

  useEffect(() => {
    getCategories();
  }, []);

  return (
    <>
      <div>CategoryPage</div>
      <div>{mapCategory(categories)}</div>
    </>
  );
}

export default CategoryPage;
