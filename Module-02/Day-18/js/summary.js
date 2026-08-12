import { withVat, format } from "./pricing.js";
import orders from "./order.js";

const ordersWithTotal = orders.map(order => {
    const total = order.items.reduce((sum, { price, qty }) => {
        return sum + withVat(price * qty);
    }, 0);

    return {
        ...order,
        total
    };
});

const over500 = ordersWithTotal.filter(order => order.total > 500);

const grandTotal = ordersWithTotal.reduce((sum, order) => {
    return sum + order.total;
}, 0);

console.log("ADDIS MARKET ORDER SUMMARY");
console.log("==========================");

ordersWithTotal.forEach(order => {
    console.log(
        `Order #${order.id} - ${order.customer}: ${format(order.total)}`
    );
});

console.log("\nOrders over 500 ETB:");

over500.forEach(order => {
    console.log(
        `Order #${order.id} - ${order.customer}: ${format(order.total)}`
    );
});

console.log(`\nGrand Total: ${format(grandTotal)}`);