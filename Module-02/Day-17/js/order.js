const subtotal = (...prices) => {
    return prices.reduce((total, price) => total + price, 0);
};

const discountBy = (rate) => {
    return (amount) => amount - amount * rate;
};

const withVat = (amount) => {
    return amount + amount * 0.15;
};

const toETB = (amount) => {
    return `${amount.toFixed(2)} ETB`;
};

const makeReceiptMaker = () => {
    let orderNumber = 0;

    return (amount) => {
        orderNumber++;
        return `#${orderNumber}: ${toETB(amount)}`;
    };
};