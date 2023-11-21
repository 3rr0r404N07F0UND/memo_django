from django.shortcuts import render, HttpResponse, redirect
from django.views.decorators.csrf import csrf_exempt
from api_app.models import User, Memo
from django.core import serializers
import json

# Create your views here.

ip = "rabbiyfy.koreacentral.cloudapp.azure.com"

def user_id_api(request):
  check_id = None
  if User.objects.filter(user_id = request.GET.get("id")):
    check_id = True
  else:
    # User.objects.create(user_id = request.GET.get("id"), user_pw = "admin1234")
    check_id = False
  return HttpResponse(json.dumps({"result": check_id}))

def user_pw_api(request):
  if User.objects.filter(user_id = request.GET.get("id"), user_pw = request.GET.get("pw")):
    resp = HttpResponse(json.dumps({"result": True}))
    resp.set_cookie(key = "id", value = request.GET.get("id"), samesite = "Lax")
    resp.set_cookie(key = "pw", value = request.GET.get("pw"), samesite = "Lax")
    return resp
  else:
    return HttpResponse(json.dumps({"result": False}))

def delete_memo(request):
  Memo.objects.filter(pk = request.GET.get("no")).delete()
  return HttpResponse("delete")

@csrf_exempt
def create_memo(request):
  data = json.loads(request.body)
  if (Memo.objects.filter(memo_title = data.get("title"))):
    return HttpResponse("you can't make!")
  else:
    print(request.COOKIES.get("id"))
    Memo.objects.create(memo_title = data.get("title"),
                        memo_text = data.get("text"),
                        memo_id = request.COOKIES.get("id"))
    return HttpResponse("create")

def show_list(request):
  print(request.COOKIES.get("id"))
  print(request.GET.get("search"))
  temp_result = serializers.serialize(
      "json",
      Memo.objects.filter(memo_id = request.COOKIES.get("id"),
                          memo_title__icontains = request.GET.get("search")).order_by("memo_time").order_by("memo_time").all())
  print(temp_result)
  return HttpResponse(json.dumps(temp_result))

def get_memo(request):
  data = request.GET.get("title")
  print(data)
  result = serializers.serialize("json", Memo.objects.filter(memo_title = data).all())
  return HttpResponse(json.dumps(result))

def get_pk(request):
  result = Memo.objects.filter(pk = request.GET.get("pk"))
  result_json = json.loads(serializers.serialize("json", result))
  result_last = result_json[0].get("fields")
  print(result_last)
  return HttpResponse(json.dumps(result_last))

@csrf_exempt
def mode_pk(request):
  req = json.loads(request.body)
  Memo.objects.filter(pk = req.get("pk")).update(memo_title = req.get("title"), memo_text = req.get("text"))
  return HttpResponse("")

def create_account(request):
  return render(request, "create_account.djt")

def create_account_post(request):
  User.objects.create(user_id = request.POST.get("id"), user_pw = request.POST.get("pw"))
  return redirect(f"http://{ip}/memo")

def ping():
  return HttpResponse("pong")
