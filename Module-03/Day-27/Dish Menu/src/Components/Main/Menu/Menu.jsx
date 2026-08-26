import "./Menu.css";
import Dish from "../../Dish/Dish";
import dishes from "./Dishes.json";

function Menu() {
  return (
    <div className="menu-container">

      {dishes.map((dish) => (
        <Dish
          key={dish.id}
          name={dish.name}
          description={dish.description}
          price={dish.price}
          image={dish.image}
        />
      ))}

    </div>
  );
}

export default Menu;