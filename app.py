from flask import Flask, render_template, request

app = Flask(__name__)

PRECIO_BOLETO = 12000


@app.route("/", methods=["GET", "POST"])
def cinepolis():
    valor_pagar = ""

    if request.method == "POST":
        nombre = request.form.get("nombre")
        compradores = int(request.form.get("compradores"))
        boletos = int(request.form.get("boletos"))
        cineco = request.form.get("cineco")

        
        max_boletos = compradores * 7
        if boletos > max_boletos:
            valor_pagar = "Error: Máximo 7 boletos por persona"
        else:
            total = boletos * PRECIO_BOLETO
            descuento = 0

            
            if boletos >= 3 and boletos <= 5:
                descuento = 0.10
            elif boletos > 5:
                descuento = 0.15

            total -= total * descuento


            if cineco == "si":
                total -= total * 0.10

            valor_pagar = f"$ {total:,.2f}"

    return render_template("cinepolis.html", valor_pagar=valor_pagar)


if __name__ == "__main__":
    app.run(debug=True)
