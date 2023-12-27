from fastapi import FastAPI, HTTPException
import requests
import uvicorn

"""采集接口地址 https://www.coinlore.com/zh/cryptocurrency-data-api"""

app = FastAPI()

API_URL = "https://api.coinlore.net/api/"


@app.get("/global/")
async def get_global():
    """Information about the crypto market"""
    try:
        response = requests.get(API_URL + "global/")
        response.raise_for_status()
    except requests.RequestException:
        raise HTTPException(status_code=404)
    results = response.json()
    return results


@app.get("/tickers/")
async def get_tickers(start, limit=100):
    """ Get data for all coins. The maximum result is 100 coins per request. You should use start and limit"""
    params = {"start": start, "limit": limit}
    try:
        response = requests.get(API_URL + "tickers", params=params)
        response.raise_for_status()
    except requests.RequestException:
        raise HTTPException(status_code=404)
    results = response.json()
    return results


@app.get("/ticker/")
async def get_ticker(ids):
    """To get information for a specific coin, you should pass coin id """
    params = {"id": ids}
    try:
        response = requests.get(API_URL + "tickers", params=params)
        response.raise_for_status()
    except requests.RequestException:
        raise HTTPException(status_code=404)
    results = response.json()
    return results


@app.get("/coin/markets")
async def get_coin_markets(ids):
    """Returns first 50 markets for a specific coin"""
    params = {"id": ids}
    try:
        response = requests.get(API_URL + "coin/markets/", params=params)
        response.raise_for_status()
    except requests.RequestException:
        raise HTTPException(status_code=404)
    results = response.json()
    return results


@app.get("/exchanges")
async def get_exchanges():
    """Get all exchanges"""
    try:
        response = requests.get(API_URL + "exchanges/")
        response.raise_for_status()
    except requests.RequestException:
        raise HTTPException(status_code=404)
    results = response.json()
    return results


@app.get("/exchange")
async def get_exchange(ids):
    """Get specific exchange by ID """
    params = {"id": ids}
    try:
        response = requests.get(API_URL + "exchange/", params=params)
        response.raise_for_status()
    except requests.RequestException:
        raise HTTPException(status_code=404)
    results = response.json()
    return results


@app.get("/coin/social_stats")
async def get_coin_social_stats(ids):
    """Get social stats for coin"""
    params = {"id": ids}
    try:
        response = requests.get(API_URL + "coin/social_stats", params=params)
        response.raise_for_status()
    except requests.RequestException:
        raise HTTPException(status_code=404)
    results = response.json()
    return results


if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="127.0.0.1", log_level="info")
