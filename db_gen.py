import sqlite3
from sqlite3 import Error
from sqlite3 import IntegrityError
from sqlite3.dbapi2 import Connection
from enum import Enum
import logging

logging_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=logging_format, level=logging.INFO, handlers=[
    logging.FileHandler("task.log"),
    logging.StreamHandler()
])

class MerchandiseStatus(Enum):
    IN_TRANSIT = "IN TRANSIT"
    WAITING_TO_SHIP = "WAITING TO SHIP"
    HOLD = "HOLD"
    SOLD = "SOLD"
    LISTED = "LISTED"
    CANCELLED = "CANCELLED"

class ExpenseType(Enum):
    CAPTCHA = "CAPTCHA"
    RESI_PROXY = "RESI"
    DC_PROXY = "DC"
    RENTAL = "RENTAL"
    SERVER = "SERVER"
    RENEWAL = "RENEWAL"
    BOT = "BOT"

class BalanceDB:
    def __init__(self) -> None:
        try:
            self.con = sqlite3.connect("balance.db")
            self.cursorObj = self.con.cursor()
            # logging.info("Connected to database")
        except Error:
            logging.info("Error connecting to database")

    def create_purchases(self):
        self.cursorObj.execute("CREATE TABLE purchases(purchase_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT NOT NULL, name TEXT NOT NULL, sku TEXT NOT NULL, size TEXT NOT NULL, location TEXT NOT NULL, price REAL NOT NULL, status TEXT NOT NULL)")
        self.con.commit()
        logging.info("Created purchases table")

    def create_sales(self):
        self.cursorObj.execute("CREATE TABLE sales(sale_id INTEGER REFERENCES purchases(purchase_id), date TEXT NOT NULL, name TEXT NOT NULL, sku TEXT NOT NULL, location TEXT NOT NULL, gross_price REAL NOT NULL, taxes REAL, shipping_expenses REAL, fees REAL, net_price REAL NOT NULL)")
        self.con.commit()
        logging.info("Created sales table")

    def create_expenses(self):
        self.cursorObj.execute("CREATE TABLE expenses(expense_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT NOT NULL, name TEXT NOT NULL, type TEXT NOT NULL, cost REAL NOT NULL)")
        self.con.commit()
        logging.info("Created expenses table")

    def create_services(self):
        self.cursorObj.execute("CREATE TABLE services(service_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, date TEXT NOT NULL, name TEXT NOT NULL, sku TEXT NOT NULL, client TEXT NOT NULL, unit_cost REAL NOT NULL, quantity INTEGER NOT NULL, total REAL NOT NULL)")
        self.con.commit()
        logging.info("Created services table")

    def create_skulist(self):
        self.cursorObj.execute("CREATE TABLE skulist(sku TEXT NOT NULL UNIQUE, model TEXT NOT NULL)")
        self.con.commit()
        logging.info("Created skulist table")

    def init_tables(self):
        self.create_purchases()
        self.create_sales()
        self.create_expenses()
        self.create_services()
        self.create_skulist()

    # return sku name

    def getSkuName(self, sku):
        try:
            return self.cursorObj.execute("SELECT model FROM skulist WHERE sku = '{}'".format(sku)).fetchone()[0]
        except IndexError:
            return "N/A"

    # get/set skulist

    def get_skulist(self):
        return self.cursorObj.execute("SELECT * FROM skulist").fetchall()

    def add_skulist(self, sku, model):
        try:
            self.cursorObj.execute("INSERT INTO skulist (sku, model) VALUES ('{}', '{}')".format(sku, model))
            self.con.commit()
            logging.info("Added SKU {} into skulist table".format(sku))
        except sqlite3.IntegrityError:
            logging.info("SKU Already Exists in Database")

    def delete_skulist(self, sku):
        self.cursorObj.execute("DELETE FROM skulist WHERE sku = '{}'".format(sku))
        self.con.commit()
        logging.info("Removed {} from skulist table".format(sku))

    def edit_skulist(self, sku, newModel):
        self.cursorObj.execute("UPDATE skulist SET model = '{}' WHERE sku = '{}'".format(newModel, sku))
        self.con.commit()
        logging.info("Edited {} in skulist table".format(sku))

    # get/set purchases

    def get_purchases(self):
        return self.cursorObj.execute("SELECT * FROM purchases").fetchall()

    def add_purchase(self, date, sku, size, location, price):
        self.cursorObj.execute("INSERT INTO purchases (date, name, sku, size, location, price, status) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(date, self.getSkuName(sku), sku, size, location, price, MerchandiseStatus.IN_TRANSIT.name))
        self.con.commit()
        logging.info("Added Purchase of {} into purchases table".format(sku))

    def delete_purchase(self, purchase_id):
        self.cursorObj.execute("DELETE FROM purchases WHERE purchase_id = '{}'".format(purchase_id))
        self.con.commit()
        # consider also checking to remove sales with associated purchase_id
        logging.info("Deleted Purchase with id {} from purchases table".format(purchase_id))

    def edit_purchase(self, purchase_id, date, sku, size, location, price, status: MerchandiseStatus):
        self.cursorObj.execute("UPDATE purchases SET date = '{}', name = '{}', sku = '{}', size = '{}', location = '{}', price = '{}', status = '{}'".format(date, self.getSkuName(sku), sku, size, location, price, status.name))
        self.con.commit()
        logging.info("Edited purchase with id {} from purchases table".format(purchase_id))

    # get/set sales

    def get_sales(self):
        return self.cursorObj.execute("SELECT * FROM sales").fetchall()

    def add_sale(self, date, purchase_id, location, gross_price, taxes, shipping_expenses, fees, net_price):
        self.cursorObj.execute("INSERT INTO sales (sale_id, date, name, sku, location, gross_price, taxes, shipping_expenses, fees, net_price) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(purchase_id, date, self.cursorObj.execute("SELECT name FROM purchases WHERE purchase_id = '{}'".format(purchase_id)).fetchone()[0], self.cursorObj.execute("SELECT sku FROM purchases WHERE purchase_id = '{}'".format(purchase_id)).fetchone()[0], location, gross_price, taxes, shipping_expenses, fees, net_price))
        self.con.commit()
        logging.info("Added Sale of {} into sales table".format(purchase_id))

    def delete_sale(self, sale_id):
        self.cursorObj.execute("DELETE FROM sales WHERE sale_id = {}".format(sale_id))
        self.con.commit()
        logging.info("Deleted sale with id {} from sales table".format(sale_id))

    def edit_sale(self, sale_id, date, location, gross_price, taxes, shipping_expenses, fees, net_price):
        self.cursorObj.execute("UPDATE sales SET date = '{}', location = '{}', gross_price = '{}', taxes = '{}', shipping_expenses = '{}', fees = '{}', net_price = '{}' WHERE sale_id = '{}'".format(date, location, gross_price, taxes, shipping_expenses, fees, net_price, sale_id))
        self.con.commit()
        logging.info("Updated sale with id {} in sales table".format(sale_id))

    # get/set expenses

    def get_expenses(self):
        return self.cursorObj.execute("SELECT * FROM expenses").fetchall()

    def add_expense(self, date, name, type: ExpenseType, cost):
        self.cursorObj.execute("INSERT INTO expenses (date, name, type, cost) VALUES ('{}', '{}', '{}', '{}')".format(date, name, type.name, cost))
        self.con.commit()
        logging.info("Added Expense of {} into expenses table".format(name))

    def delete_expense(self, expense_id):
        self.cursorObj.execute("DELETE FROM expenses WHERE expense_id = {}".format(expense_id))
        self.con.commit()
        logging.info("Deleted expense with id {} from expenses table".format(expense_id))

    def edit_expense(self, expense_id, date, name, type, cost):
        self.cursorObj.execute("UPDATE expenses SET date = '{}', name = '{}', type = '{}', cost = '{}' WHERE expense_id = '{}'".format(date, name, type, cost, expense_id))
        self.con.commit()
        logging.info("Edited expense with id {} in expenses table".format(expense_id))

    # get/set services

    def get_services(self):
        return self.cursorObj.execute("SELECT * FROM services").fetchall()

    def add_service(self, date, sku, client, unit_cost, quantity, total):
        self.cursorObj.execute("INSERT INTO services (date, name, sku, client, unit_cost, quantity, total) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(date, self.getSkuName(sku), sku, client, unit_cost, quantity, total))
        self.con.commit()
        logging.info("Added Service of {} for {} into services table".format(sku, client))

    def delete_service(self, service_id):
        self.cursorObj.execute("DELETE FROM services WHERE service_id = {}".format(service_id))
        self.con.commit()
        logging.info("Deleted service with id {} from services table".format(service_id))

    def edit_service(self, service_id, date, sku, client, unit_cost, quantity, total):
        self.cursorObj.execute("UPDATE services SET date = '{}', name = '{}', sku = '{}', client = '{}', unit_cost = '{}', quantity = '{}', total = '{}' WHERE service_id = '{}'".format(date, self.getSkuName(sku), sku, client, unit_cost, quantity, total, service_id))

    def close(self):
        self.con.close()

# db = BalanceDB()
# db.init_tables()
# db.add_skulist("CP9652", "Yeezy Boost 350 v2 - Bred")
# db.add_purchase('2021-06-01', 'CP9652', 'M 9', 'Footlocker', "107.99")
# db.add_sale('2021-06-02', 1, "GOAT", 200.00, 0, 0, 25, 175.00)
# db.add_expense('2021-06-02', "BestProxy 5GB", ExpenseType.RESI_PROXY, 50)
# db.add_service('2021-06-02', "CP9652", "Bob Smith", 10, 2, 20)
# db.close()