import "./Dish.css";

const Dish = ({ name, description, price, image, spicy, count, onAdd }) => {
    return (
        <div className="dish">

            <img src={image} alt={name} />

            <div className="dish-info">

                <div className="dish-title">
                    <h2>{name}</h2>

                    {spicy && (
                        <span className="spicy">
                            🌶️ Spicy
                        </span>
                    )}
                </div>

                <p>{description}</p>

                <div className="dish-bottom">

                    <h3>{price} ETB</h3>

                    <button onClick={onAdd}>
                        Add
                    </button>

                </div>

                {count > 0 && (
                    <p className="count">
                        Added: {count}
                    </p>
                )}

            </div>

        </div>
    );
};

export default Dish;