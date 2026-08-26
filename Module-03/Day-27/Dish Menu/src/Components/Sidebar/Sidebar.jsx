import "./Sidebar.css";

function Sidebar() {
  return (
    <aside className="sidebar">
      <h2>Categories</h2>

      <ul>
        <li>All Dishes</li>
        <li>Traditional</li>
        <li>Meat Dishes</li>
        <li>Vegetarian</li>
        <li>Breakfast</li>
        <li>Drinks</li>
      </ul>
    </aside>
  );
}

export default Sidebar;