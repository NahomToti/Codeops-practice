import { useContext } from "react";
import { CartContext } from "../../cart/CartProvider";

export default function Checkout() {
  const { items, total, dispatch } = useContext(CartContext);

  return (
    <aside className="checkout">
      <h2>Checkout</h2>

      {items.length === 0 ? (
        <p>Your cart is empty.</p>
      ) : (
        <>
          {items.map((item) => (
            <div className="checkout-item" key={item.id}>
              <div>
                <strong>{item.name}</strong>
                <p>
                  {item.price} ETB × {item.quantity}
                </p>
              </div>

              <div>
                <button
                  onClick={() =>
                    dispatch({
                      type: "remove",
                      payload: item.id,
                    })
                  }
                >
                  −
                </button>

                <button
                  onClick={() =>
                    dispatch({
                      type: "add",
                      payload: item,
                    })
                  }
                >
                  +
                </button>
              </div>
            </div>
          ))}

          <h3>Total: {total.toFixed(2)} ETB</h3>

          <button
            onClick={() =>
              dispatch({
                type: "clear",
              })
            }
          >
            Clear Cart
          </button>

          <div className="payment-confirmation">
            <h3>Payment</h3>
            <p>
              Pay <strong>{total.toFixed(2)} ETB</strong> using Telebirr.
            </p>

            <button
              onClick={() =>
                alert(
                  `Telebirr Payment Confirmation\n\nAmount: ${total.toFixed(
                    2
                  )} ETB`
                )
              }
            >
              Confirm Telebirr Payment
            </button>
          </div>
        </>
      )}
    </aside>
  );
}