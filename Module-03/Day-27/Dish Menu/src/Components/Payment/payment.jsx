import { useState } from "react";
import "./Payment.css";

const Payment = ({ total }) => {
    const [telebirrNumber, setTelebirrNumber] = useState("");

    const isValidTelebirr = /^(09|07)\d{8}$/.test(telebirrNumber);

    const handleNumberChange = (event) => {
        const value = event.target.value.replace(/\D/g, "");

        if (value.length <= 10) {
            setTelebirrNumber(value);
        }
    };

    const handlePayment = () => {
        if (!isValidTelebirr) {
            return;
        }

        alert("Payment request sent successfully!");
    };

    return (
        <div className="payment">

            <div className="payment-header">
                <h2>Telebirr Payment</h2>
                <p>Enter your Telebirr number to complete your order.</p>
            </div>

            <label htmlFor="telebirr">
                Telebirr Number
            </label>

            <input
                id="telebirr"
                type="text"
                value={telebirrNumber}
                onChange={handleNumberChange}
                placeholder="09XXXXXXXX"
                maxLength="10"
            />

            {telebirrNumber.length > 0 && !isValidTelebirr && (
                <p className="payment-error">
                    Enter a valid Telebirr number.
                </p>
            )}

            {isValidTelebirr && (
                <p className="payment-success">
                    ✓ Telebirr number is valid
                </p>
            )}

            <div className="payment-total">
                <span>Total</span>
                <strong>{total.toLocaleString()} ETB</strong>
            </div>

            <button
                className="payment-button"
                disabled={!isValidTelebirr || total === 0}
                onClick={handlePayment}
            >
                Pay with Telebirr
            </button>

        </div>
    );
};

export default Payment;