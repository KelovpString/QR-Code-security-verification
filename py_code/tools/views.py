from base64 import b64encode, b64decode

from django.http import HttpResponse
from django.utils.six import BytesIO
import qrcode
# RSA
import rsa
import hashlib
import random

from rest_framework.utils import json

from py_code.settings import PRIVATE_KEY, PUBLIC_KEY
# SQL
#RESTFUL API
from django.contrib.auth.models import User, Group
from rest_framework import generics
from rest_framework import permissions
from rest_framework import viewsets
from tools.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
#import Table
from tools.models import product
from tools.serializers import ProductSerializer
from django.shortcuts import render, render_to_response
from tools.permissions import IsOwnerOrReadOnly

# User In
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserViewSet(viewsets.ModelViewSet):
    """
    Check And Edit User's page
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
class GroupViewSet(viewsets.ModelViewSet):
    """
    Check and Edit Gruop's View page
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# GET the QR_CODE
def generate_qrcode(request, data):
    (out,prikey) = RSA_EncryptStr(data)
    img = qrcode.make(b64encode(out).decode('utf-8'))
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    response = HttpResponse(image_stream, content_type="image/png")
    return response
def RSA_EncryptStr(str):
    # GET public key and prime key
    # Every time to product this key
    content = str.encode('utf-8')
    crypto = rsa.encrypt(content, PUBLIC_KEY)
    return (crypto, PRIVATE_KEY)
# RSA - DEC
def RSA_DeccryptStr(str, pk):
    content = rsa.decrypt(str, pk)
    con = content.decode('utf-8')
    return con
# GET GOOD_NO
def GET_GOOD_NO():
    a = random.randint(65,90) # Get Up letter ASCII
    b = random.randint(65,90)
    c1 = chr(a)
    c2 = chr(b)
    li = [i for i in range(10000,99999)]
    a1 = random.sample(li, 1)
    a2 = random.sample(li, 1)
    a3 = random.sample(li, 1)
    return ""+str(c1)+str(c2)+str(a1[0])+str(a2[0])+str(a3[0])
# GET MD5 CODE
def GET_MD5_CODE(no):
    m = hashlib.md5()
    m.update(bytes(no, encoding='utf8'))
    return m.hexdigest()

# Show The Product
def index(request):
    response_data = {}
    response_data["products"] = product.objects.all()
    return render(request, 'index.html',response_data)
# Fuzzy query
def QueryProductinPc(request):
    request.encoding = 'utf-8'
    response_data = {}
    response_data["products"] = product.objects.filter(name__contains=request.GET['searchInfo'])
    return render(request, 'index.html', response_data)

# RESTFUL API -ALL
# used to Mobile
# And Only in Product
#---------------------------
class ProuctsList(APIView):
    """
        USE Products List Get
    """
    #OUT API
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,)
    def get(self,request):
        products = product.objects.all()
        products.order_by("id")
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def QueryProductinMobile(request ,name):
    if request.method == 'GET':
        products = product.objects.filter(name__contains=name)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
@api_view(['GET'])
def GetproductLimit(request, page):
    if request.method == 'GET':
        products = product.objects.all()[(int(page)-1)*10:int(page)*10]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# This part Must in line to do
@api_view(['GET'])
def CheckTheProductInfo(request, code):
    if request.method == 'GET':
        try:
            md5 = RSA_DeccryptStr(b64decode(code), PRIVATE_KEY)
        except:
            return HttpResponse(json.dumps({"data":"500 --Unlawful verification","status":"500"}),content_type="application/json")
        products = product.objects.filter(code=md5)
        serializer = ProductSerializer(products, many=True)
        if len(serializer.data) == 0 :
            return HttpResponse(json.dumps({"data": "The goods you have scanned are not registered.", "status": "404"}),
                                content_type="application/json")
        return HttpResponse(json.dumps({"data": serializer.data, "status": "200"}),
                                content_type="application/json")

@api_view(['GET'])
def QueryProductinfo(request, id):
    if request.method == 'GET':
        products = product.objects.filter(id=id)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

