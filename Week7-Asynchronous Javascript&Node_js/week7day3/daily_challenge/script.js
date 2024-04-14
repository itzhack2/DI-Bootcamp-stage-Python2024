
fetchCurrencies( );
function fetchCurrencies( ) {
    const url = "https://v6.exchangerate-api.com/v6/2e8500aa3e1463725c092741/latest/ILS";
    fetch(url)
        .then((res) => res.json())
        .then((res) => console.log(res.conversion_rates));
        .catch((error) => console.log(error));
}