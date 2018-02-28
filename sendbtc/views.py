# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from models import Broadcast
from TransactionUtils import *

def home(request):
	return render(request, "send.html")

def test_env(request):
	return render(request, "testing.html")

def ajax_tx(request):
	try:
		s_address = str(request.GET.get("sender", None))
		receivers = request.GET.getlist("receivers[]", None)
		amounts = request.GET.getlist("amounts[]", None)
		fee = int(request.GET.get("fee", None))
	except:
		bytes_ = "Transaction Generation Failed:\nVerify all input fields.\nLeave no fields blank!"

	try:
		outs = [{'address':receivers[i], 'value':int(amounts[i])} for i in range(len(receivers))]
		bytes_ = unsigned_tx(s_address, outs, fee)
	except:
		bytes_ = "Transaction Generation Failed:\nVerify all input fields.\nMake sure sender has enough funds for transaction and fee."
	data = {'bytes_':bytes_}
	return JsonResponse(data)

def ajax_broadcast(request):

	bytes_ = str(request.GET.get("signed", None))
	
	try:
		broadcast_tx(bytes_)
		output = "Transaction Submitted."
		receipt = Broadcast()
		receipt.time = timezone.now()
		receipt.tx = bytes_
		receipt.save()
		txid = get_txid(bytes_)
	except Exception as x:
		output = str(repr(x))
		txid = '-'
	data = {'output':output, 'txid':txid}
	return JsonResponse(data)

def ajax_verify(request):

	bytes_ = str(request.GET.get('bytes_', None))

	try:
		data = decode_tx(bytes_)
	except:
		data = {'error': 'Cannot decode transaction!'}
	return JsonResponse(data)

def ajax_suggest(request):
	try:
		addr = str(request.GET.get('addr', None))
		nums = request.GET.getlist('amounts[]', None)
		o = [{'address': "none", 'value':int(num)} for num in nums]
		data = {"msg":txsize_est(addr, o)}
	except:
		data = {"msg": 0}
	return JsonResponse(data)

def ajax_unlock(request):
	addr = str(request.GET.get('address', None))
	utxos = get_utxos(addr)
	data = {'utxos':utxos}
	return JsonResponse(data)


def tutorial_1(request):
	return render(request, "tutorial1.html")


