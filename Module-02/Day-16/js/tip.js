let bill = Number(500);
let partysize = 5;
let paymentmethod = "Telebirr";

let tip;
if(bill>300){
    tip= bill *0.1;

}
else{
    tip = bill *0.5;
}

let total = bill + tip;

let servicefee = 0;

switch(paymentmethod){
    case "Telebirr":
        servicefee = 5;
        break;

        case "CBE":
            servicefee = 3;
            break;
            default:
                servicefee = 0;
} total += servicefee;

let perperson = total / partysize;

console.log(`Bill: ${bill.toFixed (2)}ETB`);
console.log(`ServiceFee: ${servicefee.toFixed(2)} ETB`);
console.log(`Total: ${total.toFixed(2)} ETB`);
console.log(`Amount per Person: ${perperson.toFixed(2)} ETB`);