import "./Dish.css";

function Dish({ name, description, price, image }) {
  return (
    <div className="dish-card">

      <div className="dish-image">
        <img src={image} alt={name} />
      </div>

      <div className="dish-info">

        <h3>{name}</h3>

        <p className="dish-description">
          {description}
        </p>

        <div className="dish-bottom">

          <span className="dish-price">
            {price} ETB
          </span>

          <button>
            Add
          </button>

        </div>

      </div>

    </div>
  );
}

export default Dish;