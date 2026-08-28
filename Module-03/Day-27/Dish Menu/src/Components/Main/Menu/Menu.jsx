import { useState } from "react";
import "./Menu.css";
import Dish from "../../Dish/Dish";
import dishes from "./Dishes.json";

const Menu = () => {
    const [category, setCategory] = useState("all");

    const filteredDishes = dishes.filter((dish) => {
        if (category === "all") {
            return true;
        }

        return dish.category === category;
    });

    return (
        <div className="menu">

            <h1>Menu</h1>

            <div className="categories">

                <button
                    className={category === "all" ? "active" : ""}
                    onClick={() => setCategory("all")}
                >
                    All Dishes
                </button>

                <button
                    className={category === "drinks" ? "active" : ""}
                    onClick={() => setCategory("drinks")}
                >
                    Drinks
                </button>

                <button
                    className={category === "vegetarian" ? "active" : ""}
                    onClick={() => setCategory("vegetarian")}
                >
                    Vegetarian
                </button>

                <button
                    className={category === "meat" ? "active" : ""}
                    onClick={() => setCategory("meat")}
                >
                    Meats
                </button>

            </div>

            <div className="dish-container">

                {filteredDishes.map((dish) => (
                    <Dish
                        key={dish.id}
                        name={dish.name}
                        description={dish.description}
                        price={dish.price}
                        image={dish.image}
                        spicy={dish.spicy}
                    />
                ))}

            </div>

        </div>
    );
};

export default Menu;