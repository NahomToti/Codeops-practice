const status = document.getElementById("status");
const form = document.getElementById("convert-form");
const amountInput = document.getElementById("amount");
const currencySelect = document.getElementById("currency");
const addWatchlistButton = document.getElementById("add-watchlist");
const result = document.getElementById("result");
const error = document.getElementById("error");
const watchlist = document.getElementById("watchlist");

const state = {
    rates: {},
    watchlist: JSON.parse(localStorage.getItem("birrWatchlist")) || []
};

function saveState() {
    localStorage.setItem("birrWatchlist", JSON.stringify(state.watchlist));
}

function renderCurrencies() {
    currencySelect.innerHTML = '<option value="">Choose currency</option>';

    Object.keys(state.rates)
        .sort()
        .forEach(currency => {
            if (currency !== "ETB") {
                const option = document.createElement("option");
                option.value = currency;
                option.textContent = currency;
                currencySelect.appendChild(option);
            }
        });
}

function renderWatchlist() {
    watchlist.innerHTML = "";

    if (state.watchlist.length === 0) {
        const li = document.createElement("li");
        li.textContent = "Your watchlist is empty.";
        li.className = "empty";
        watchlist.appendChild(li);
        return;
    }

    state.watchlist.forEach(currency => {
        const li = document.createElement("li");

        const span = document.createElement("span");
        span.textContent = currency;

        const button = document.createElement("button");
        button.textContent = "Delete";
        button.dataset.currency = currency;

        li.appendChild(span);
        li.appendChild(button);
        watchlist.appendChild(li);
    });
}

async function loadRates() {
    status.textContent = "Loading...";
    status.className = "loading";
    error.textContent = "";

    try {
        const res = await fetch("https://open.er-api.com/v6/latest/ETB");

        if (!res.ok) {
            throw new Error("Failed to load rates");
        }

        const data = await res.json();

        if (data.result !== "success") {
            throw new Error("Failed to load rates");
        }

        state.rates = data.rates;

        renderCurrencies();
        renderWatchlist();

        status.textContent = "Rates loaded successfully.";
        status.className = "success";
    } catch (err) {
        status.textContent = "Unable to load exchange rates.";
        status.className = "error";
    }
}

function convert(event) {
    event.preventDefault();

    error.textContent = "";
    result.textContent = "";

    const amount = Number(amountInput.value);
    const currency = currencySelect.value;

    if (!amount || amount <= 0) {
        error.textContent = "Please enter a valid amount.";
        return;
    }

    if (!currency) {
        error.textContent = "Please choose a currency.";
        return;
    }

    const rate = state.rates[currency];

    if (!rate) {
        error.textContent = "Exchange rate is not available.";
        return;
    }

    const converted = amount * rate;

    result.textContent = `${amount.toLocaleString()} ETB = ${converted.toFixed(2)} ${currency}`;
}

function addToWatchlist() {
    const currency = currencySelect.value;

    error.textContent = "";

    if (!currency) {
        error.textContent = "Please choose a currency first.";
        return;
    }

    if (state.watchlist.includes(currency)) {
        error.textContent = `${currency} is already in your watchlist.`;
        return;
    }

    state.watchlist.push(currency);

    saveState();
    renderWatchlist();
}

watchlist.addEventListener("click", event => {
    if (event.target.tagName !== "BUTTON") {
        return;
    }

    const currency = event.target.dataset.currency;

    state.watchlist = state.watchlist.filter(item => item !== currency);

    saveState();
    renderWatchlist();
});

form.addEventListener("submit", convert);
addWatchlistButton.addEventListener("click", addToWatchlist);

loadRates();