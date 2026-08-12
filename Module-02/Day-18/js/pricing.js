const VAT = 0.15;

function withVat(price) {
    return price + (price * VAT);
}

function format(amount) {
    return `${amount.toFixed(2)} ETB`;
}

export { withVat, format };