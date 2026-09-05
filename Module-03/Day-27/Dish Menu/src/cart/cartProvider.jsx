import {
  createContext,
  useMemo,
  useReducer,
} from "react";

import {
  cartReducer,
  initialCartState,
} from "./cartReducer";

export const CartContext = createContext(null);

export default function CartProvider({ children }) {
  const [state, dispatch] = useReducer(
    cartReducer,
    initialCartState
  );

  const total = state.items.reduce(
    (sum, item) =>
      sum + item.price * item.quantity,
    0
  );

  const itemCount = state.items.reduce(
    (sum, item) =>
      sum + item.quantity,
    0
  );

  const value = useMemo(
    () => ({
      items: state.items,
      dispatch,
      total,
      itemCount,
    }),
    [state.items, total, itemCount]
  );

  return (
    <CartContext.Provider value={value}>
      {children}
    </CartContext.Provider>
  );
}