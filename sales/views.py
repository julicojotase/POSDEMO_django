from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product
from cash.models import CashRegister
from .models import Sale, SaleItem


@login_required
def pos_view(request):

    products = Product.objects.filter(active=True)

    return render(request, "pos/pos.html", {
        "products": products
    })


@login_required
def create_sale(request):

    if request.method == "POST":

        cart = request.POST.getlist("product_id[]")
        qtys = request.POST.getlist("qty[]")
        prices = request.POST.getlist("price[]")

        paid = float(request.POST.get("paid"))

        cash = CashRegister.objects.filter(
            user=request.user,
            is_open=True
        ).first()

        if not cash:
            return redirect("pos")

        sale = Sale.objects.create(
            user=request.user,
            cash=cash,
            paid=paid,
            change=0
        )

        for i in range(len(cart)):

            product = Product.objects.get(id=cart[i])

            SaleItem.objects.create(
                sale=sale,
                product=product,
                quantity=int(qtys[i]),
                price=float(prices[i]),
                subtotal=0
            )

        sale.calculate_total()

        return redirect("pos")

    return redirect("pos")