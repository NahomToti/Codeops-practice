import { useState } from "react";
import Header from "./Components/Header/Header";
import Footer from "./Components/Footer/Footer";
import Sidebar from "./Components/Sidebar/Sidebar";
import Menu from "./Components/Main/Menu/Menu";
import "./App.css";

const App = () => {
    const [category, setCategory] = useState("all");
    const [cart, setCart] = useState({});

    return (
        <div className="app">
            <Header />

            <div className="main">
                <Sidebar
                    category={category}
                    setCategory={setCategory}
                />

                <Menu
                    category={category}
                    cart={cart}
                    setCart={setCart}
                />
            </div>

            <Footer />
        </div>
    );
};

export default App;