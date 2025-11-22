import React, { useEffect, useState } from "react";
import axios from "axios";

function TestAPI() {
  const [data, setData] = useState(null);

  useEffect(() => {
    const apiUrl = process.env.REACT_APP_API_URL;

    console.log("Loaded API URL:", apiUrl);  // Debug

    if (!apiUrl) {
      console.error("ERROR: REACT_APP_API_URL is NULL");
      return;
    }

    axios
      .get(`${apiUrl}products/`)
      .then((res) => {
        console.log("API Response:", res.data);
        setData(res.data);
      })
      .catch((err) => {
        console.error("API Error:", err);
      });
  }, []);

  return (
    <div>
      <h1>API Test</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}

export default TestAPI;
