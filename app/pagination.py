import requests

def page(limit=10, page_no=1):
    url ={"dummy" : "https://dummyjson.com/products"}
    
    # page_data = requests.get(url["dummy"]).json()
    # print(page_data)
    skip = (page_no - 1) * limit
    params = {
        "limit" : limit,
        "skip" : skip
    }
    response = requests.get(url=url['dummy'], params=params)
    if response.status_code == 200:
        data = response.json()
        products = data.get("products", [])
        return products
    else:
        return ({"Failed to fetch data", response.status_code})