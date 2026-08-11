const memberDiscount = discountBy(0.10);
const receiptMaker = makeReceiptMaker();

const order1 = withVat(
    memberDiscount(
        subtotal(120, 80, 150)
    )
);

const order2 = withVat(
    subtotal(200, 175)
);

const order3 = withVat(
    memberDiscount(
        subtotal(90, 60, 140)
    )
);

console.log(receiptMaker(order1));
console.log(receiptMaker(order2));
console.log(receiptMaker(order3));