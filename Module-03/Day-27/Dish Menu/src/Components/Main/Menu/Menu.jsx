import { useContext, useMemo } from "react";
import { CartContext } from "../../../cart/CartProvider";
import dishesData from "./dishes.json";
import Dish from "../../Dish/Dish";
import "./Menu.css";

export default function Menu({ category }) {
  const { dispatch } = useContext(CartContext);

  const dishes = useMemo(() => {
    if (category === "all") {
      return dishesData;
    }

    return dishesData.filter(
      (dish) =>
        dish.category?.toLowerCase() === category?.toLowerCase()
    );
  }, [category]);

  return (
    <div className="menu">
      <h2>Our Menu</h2>

      <div className="menu-grid">
        {dishes.map((dish) => (
          <Dish
            key={dish.id}
            name={dish.name}
            description={dish.description}
            price={dish.price}
            image={dish.image}
            spicy={dish.spicy}
            count={0}
            onAdd={() =>
              dispatch({
                type: "add",
                payload: {
                  id: dish.id,
                  name: dish.name,
                  price: dish.price,
                  image: dish.image,
                },
              })
            }
          />
        ))}
      </div>
    </div>
  );
}