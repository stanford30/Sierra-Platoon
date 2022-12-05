import axios from "axios";
import React from "react";
import { useEffect, useState } from "react";

function ItemPage() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    axios.get("api/items").then((res) => {
      console.log(res);
    });
  }, []);

  return <div>ItemPage</div>;
}

export default ItemPage;
