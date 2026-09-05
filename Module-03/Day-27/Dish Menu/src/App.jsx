import { useState } from "react";

import Header from "./Components/Header/Header";
import Footer from "./Components/Footer/Footer";
import Sidebar from "./Components/Sidebar/Sidebar";
import Menu from "./Components/Main/Menu/Menu";
import Checkout from "./Components/Checkout/Checkout";

import "./App.css";

const App = () => {
  const [category, setCategory] = useState("all");

  return (
    <div className="app">
      <Header />

      <div className="main">
        <Sidebar
          category={category}
          setCategory={setCategory}
        />

        <main>
          <Menu category={category} />
        </main>

        <Checkout />
      </div>

      <Footer />
    </div>
  );
};

export default App;