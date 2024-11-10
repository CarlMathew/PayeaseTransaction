from django.shortcuts import render
import json
from django.http import JsonResponse
from .utils import SQLHandler

# Create your views here.


def registration(request):
    sql_handler = SQLHandler()
    results = sql_handler.read_query("SELECT * FROM Users")
    print(results)
    return render(request, "base/registration.html")

def register(request):
    if request.method == "POST":
        sql_handler = SQLHandler()
        data = json.loads(request.body)
        id = data.get("id", '')
        name = data.get("name", '')
        password = data.get("pass", '')
        amount = data.get("amount", '')
        query = f"INSERT INTO Users (RFID, Name, Balance, Password) Values ('{id}', '{name}', '{amount}', '{password}')"
        sql_handler.update_query(query)
        return JsonResponse({"success": True})

def reload(request):
    return render(request, "base/reload.html")


def reload_card(request):
    if request.method == "POST":
        sql_handler = SQLHandler()
        data = json.loads(request.body)
        id = data.get("id", '')
        date_post = data.get("date_post", '')
        amount = data.get("amount", '')
        query1 = f"UPDATE Users SET Balance = {amount} WHERE RFID = '{id}'"
        query2 = f"INSERT INTO Reload_Transactions(RFID, Amount, Date_Posted) VALUES ('{id}', {amount}, '{date_post}')"
        sql_handler.update_query(query1)
        sql_handler.update_query(query2)
        return JsonResponse({"successs": True})
    else:
        return JsonResponse({"error": True})

    
