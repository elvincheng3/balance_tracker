import re
from flask import Flask
from flask import request
import requests
from db_gen import BalanceDB, MerchandiseStatus, ExpenseType

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# get requests

@app.route("/data/skulist/", methods=['GET'])
def get_skulist():
    if request.method == 'GET':
        db = BalanceDB()
        skulist = db.get_skulist()
        db.close()

        skulist_json = {
            "skulist": []
        }
        for sku in skulist:
            skulist_json["skulist"].append({
                "sku": sku[0],
                "model": sku[1]
            })

        print(skulist_json)
        return skulist_json

@app.route("/data/purchases/", methods=['GET'])
def get_purchases():
    if request.method == 'GET':
        db = BalanceDB()
        purchases = db.get_purchases()
        db.close()

        purchases_json = {
            "purchases": []
        }
        for purchase in purchases:
            purchases_json["purchases"].append({
                "purchase_id": purchase[0],
                "date": purchase[1],
                "name": purchase[2],
                "sku": purchase[3],
                "size": purchase[4],
                "site": purchase[5],
                "price": purchase[6],
                "status": purchase[7]
            })

        print(purchases_json)
        return purchases_json

@app.route("/data/sales/", methods=['GET'])
def get_sales():
    if request.method == 'GET':
        db = BalanceDB()
        sales = db.get_sales()
        db.close()

        sales_json = {
            "sales": []
        }
        for sale in sales:
            sales_json["sales"].append({
                "sale_id": sale[0],
                "date": sale[1],
                "name": sale[2],
                "sku": sale[3],
                "location": sale[4],
                "gross_price": sale[5],
                "taxes": sale[6],
                "shipping_expenses": sale[7],
                "fees": sale[8],
                "net_price": sale[9]
            })

        print(sales_json)
        return sales_json

@app.route("/data/expenses/", methods=['GET'])
def get_expenses():
    if request.method == 'GET':
        db = BalanceDB()
        expenses = db.get_expenses()
        db.close()

        expenses_json = {
            "expenses": []
        }
        for expense in expenses:
            expenses_json["expenses"].append({
                "expense_id": expense[0],
                "date": expense[1],
                "name": expense[2],
                "type": expense[3],
                "cost": expense[4],
            })

        print(expenses_json)
        return expenses_json

@app.route("/data/services/", methods=['GET'])
def get_services():
    if request.method == 'GET':
        db = BalanceDB()
        services = db.get_services()
        db.close()

        services_json = {
            "services": []
        }
        for service in services:
            services_json["services"].append({
                "service_id": service[0],
                "date": service[1],
                "name": service[2],
                "sku": service[3],
                "client": service[4],
                "unit_cost": service[5],
                "quantity": service[6],
                "total": service[7],
            })

        print(services_json)
        return services_json

# post new entries

@app.route("/new/skulist/", methods=['POST'])
def add_skulist():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.add_skulist(data["sku"], data["model"])
        db.close()

@app.route("/new/purchase/", methods=['POST'])
def add_purchase():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.add_purchase(data["date"], data["sku"], data["size"], data["location"], data["price"])
        db.close()

@app.route("/new/sale/", methods=['POST'])
def add_sale():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.add_sale(data["date"], data["purchase_id"], data["location"], data["gross_price"], data["taxes"], data["shipping_expenses"], data["fees"], data["net_price"])
        db.close()

@app.route("/new/expense/", methods=['POST'])
def add_expense():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.add_expense(data["date"], data["name"], ExpenseType[data["type"]], data["cost"])
        db.close()

@app.route("/new/service/", methods=['POST'])
def add_service():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.add_service(data["date"], data["sku"], data["client"], data["unit_cost"], data["quantity"], data["total"])
        db.close()

# delete entries

@app.route("/delete/skulist/", methods=['POST'])
def delete_skulist():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.delete_skulist(data["sku"])
        db.close()

@app.route("/delete/purchase/", methods=['POST'])
def delete_purchase():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.delete_purchase(data["purchase_id"])
        db.close()

@app.route("/delete/sale/", methods=['POST'])
def delete_sale():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.delete_sale(data["sale_id"])
        db.close()

@app.route("/delete/expense/", methods=['POST'])
def delete_expense():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.delete_expense(data["expense_id"])
        db.close()

@app.route("/delete/service/", methods=['POST'])
def delete_service():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.delete_service(data["service_id"])
        db.close()

# edit entries

@app.route("/edit/skulist/", methods=['POST'])
def edit_skulist():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.edit_skulist(data["sku"], data["newModel"])
        db.close()

@app.route("/edit/purchase/", methods=['POST'])
def edit_purchase():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.edit_purchase(data["purchase_id"], data["date"], data["sku"], data["size"], data["location"], data["price"], MerchandiseStatus[data["status"]])
        db.close()

@app.route("/edit/sale/", methods=['POST'])
def edit_sale():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.edit_sale(data["sale_id"], data["date"], data["location"], data["gross_price"], data["taxes"], data["shipping_expenses"], data["fees"], data["net_price"])
        db.close()

@app.route("/edit/expense/", methods=['POST'])
def edit_expense():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.edit_expense(data["expense_id"], data["date"], data["name"], ExpenseType[data["type"]], data["cost"])
        db.close()

@app.route("/edit/service/", methods=['POST'])
def edit_service():
    if request.method == 'POST':
        data = request.get_json()
        db = BalanceDB()
        db.edit_service(data["service_id"], data["date"], data["sku"], data["client"], data["unit_cost"], data["quantity"], data["total"])
        db.close()



