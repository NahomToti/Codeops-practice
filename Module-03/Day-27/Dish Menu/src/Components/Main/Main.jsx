import "./Main.css";
import Menu from "./Menu/Menu";

function Main() {
  return (
    <main className="main">
      <section className="content">
        <div className="content-header">
          <h2>Our Ethiopian Menu</h2>
          <p>Enjoy delicious traditional Ethiopian dishes</p>
        </div>

        <Menu />
      </section>
    </main>
  );
}

export default Main;