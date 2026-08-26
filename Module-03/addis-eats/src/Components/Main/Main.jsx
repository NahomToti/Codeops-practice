import "./Main.css";
import Sidebar from "../Sidebar/Sidebar";
import Product from "../Product/Product";

function Main() {
  return (
    <main className="main">
      <Sidebar />

      <section className="products">
        <h2>Our Menu</h2>

        <div className="product-grid">
          <Product
            name="Doro Wot"
            price="350"
            description="Traditional Ethiopian spicy chicken stew."
          />

          <Product
            name="Tibs"
            price="400"
            description="Tender beef cooked with vegetables and spices."
          />

          <Product
            name="Kitfo"
            price="450"
            description="Traditional Ethiopian minced beef dish."
          />

          <Product
            name="Shiro"
            price="200"
            description="Delicious Ethiopian chickpea stew."
          />
        </div>
      </section>
    </main>
  );
}

export default Main;