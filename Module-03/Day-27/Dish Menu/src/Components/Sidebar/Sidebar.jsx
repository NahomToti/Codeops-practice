import "./Sidebar.css";

const Sidebar = ({ category, setCategory }) => {
    const categories = [
        { id: "all", name: "All Dishes" },
        { id: "traditional", name: "Traditional" },
        { id: "meat", name: "Meat Dishes" },
        { id: "vegetarian", name: "Vegetarian" },
        { id: "breakfast", name: "Breakfast" },
        { id: "drinks", name: "Drinks" }
    ];

    return (
        <aside className="sidebar">
            <h2>Categories</h2>

            <ul>
                {categories.map((item) => (
                    <li
                        key={item.id}
                        className={category === item.id ? "active" : ""}
                        onClick={() => setCategory(item.id)}
                    >
                        {item.name}
                    </li>
                ))}
            </ul>
        </aside>
    );
};

export default Sidebar;