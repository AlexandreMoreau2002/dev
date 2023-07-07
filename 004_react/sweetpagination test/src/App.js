import React, { useState } from "react";
import SweetPagination from "sweetpagination";
import './App.css';

function boucle() {
  const array = [];

  for (let i = 1; i <= 200; i++) {
    array.push(i);
  }

  return array;
}

export default function App() {

  const [currentPageData, setCurrentPageData] = useState(new Array(2).fill());
  // Example items, to simulate fetching from another resources.
  // const items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14];
  const array = boucle()

  return (
    <div className="App">
      {currentPageData.map((item) => (
        <div>
          <h3>Item #{item}</h3>
        </div>
      ))}

      <SweetPagination
        currentPageData={setCurrentPageData}
        getData={array}
      />
    </div>
  );
}