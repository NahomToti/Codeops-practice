import { useContext } from "react";
import { CartContext } from "../../cart/CartProvider";

export default function Header() {
  const { itemCount } = useContext(CartContext);

  return (
    <header className="header">
      <h1>🍴 Addis Eats</h1>

      <div className="cart-badge">
        🛒 Cart: {itemCount}
      </div>
    </header>
  );
}