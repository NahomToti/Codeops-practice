import Header from "./Components/Header/Header";
import Footer from "./Components/Footer/Footer";
import Sidebar from "./Components/Sidebar/Sidebar";
import Menu from "./Components/Main/Menu/Menu";

const App = () => {
  return (
    <div>
      <Header />

      <div className="main">
        <Sidebar />
        <Menu />
      </div>

      <Footer />
    </div>
  );
};

export default App;