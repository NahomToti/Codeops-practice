import "./Menu.css";
import Dish from "../../Dish/Dish";
import Payment from "../../Payment/Payment";
import dishes from "./Dishes.json";

const Menu = ({ category, cart, setCart }) => {
    const addDish = (id) => {
        setCart((prevCart) => ({
            ...prevCart,
            [id]: (prevCart[id] || 0) + 1
        }));
    };

    const filteredDishes = dishes.filter((dish) => {
        if (category === "all") {
            return true;
        }

        return dish.category === category;
    });

    const total = dishes.reduce((sum, dish) => {
        const quantity = cart[dish.id] || 0;
        return sum + dish.price * quantity;
    }, 0);

    return (
        <main className="menu">

            <div className="menu-header">
                <p className="menu-label">
                    HABESHA DELIGHTS
                </p>

                <h1>Our Menu</h1>

                <p className="menu-subtitle">
                    Traditional flavors, fresh ingredients
                </p>
            </div>

            <div className="dish-container">
                {filteredDishes.length > 0 ? (
                    filteredDishes.map((dish) => (
                        <Dish
                            key={dish.id}
                            name={dish.name}
                            description={dish.description}
                            price={dish.price}
                            image={dish.image}
                            spicy={dish.spicy}
                            count={cart[dish.id] || 0}
                            onAdd={() => addDish(dish.id)}
                        />
                    ))
                ) : (
                    <p className="no-dishes">
                        No dishes available in this category.
                    </p>
                )}
            </div>

            <div className="order-total">
                <div>
                    <span>Order Total</span>
                    <h2>{total.toLocaleString()} ETB</h2>
                </div>
            </div>

            <Payment total={total} />

        </main>
    );
};

export default Menu;