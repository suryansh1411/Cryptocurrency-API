from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from subprocess import call
import json


api=FastAPI(title="Cryptocurrency-API")


@api.get('/')
async def home():
    call(["python3", "scrap.py"])
    with open("data.txt", 'r') as f:
        crypto_dic=json.load(f)
        crypto_list=list(crypto_dic.keys())
    return {"greeting":"Welcome! to Cryptocurrency-API", "cryptocurrencies":crypto_list}


@api.get('/api/crypto/')
async def get_crypto(req: str):
    call(["python3", "scrap.py"])
    with open("data.txt", 'r') as f:
        crypto_dic=json.load(f)
        crypto_list=list(crypto_dic.keys())
    if req in crypto_list:
        return {req:crypto_dic[req]}
    else:
        HTTPException(status_code=404, detail="Item not found")


@api.get('/api/all/')
async def get_all_crypto():
    call(["python3", "scrap.py"])
    with open("data.txt", 'r') as f:
        crypto_dic=json.load(f)
        print("heh")
    return crypto_dic
    

