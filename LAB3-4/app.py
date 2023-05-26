from flask import Flask, render_template, request

app = Flask(__name__)

# Предопределенные курсы валют
exchange_rates = {
    'USD': 1.0,
    'EUR': 0.9,
    'GBP': 0.8,
    'JPY': 110.0,
    'RUB': 75.0,
    'KZT': 420.0,
    'AUD': 1.3,
    'NOK': 8.5,
}


@app.route('/', methods=['GET', 'POST'])
def converter():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        base_currency = request.form['base_currency']
        target_currency = request.form['target_currency']

        if base_currency in exchange_rates and target_currency in exchange_rates:
            base_rate = exchange_rates[base_currency]
            target_rate = exchange_rates[target_currency]
            converted_amount = amount * (target_rate / base_rate)
        else:
            converted_amount = "Invalid currency"

        return render_template('result.html', amount=amount, base_currency=base_currency,
                               target_currency=target_currency, converted_amount=converted_amount)

    return render_template('converter.html')


if __name__ == '__main__':
    app.run()
