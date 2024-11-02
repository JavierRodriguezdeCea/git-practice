import requests
from bs4 import BeautifulSoup
import pandas as pd

def alcampo(search_term: str) -> pd.DataFrame:
    url = "https://www.compraonline.alcampo.es/search?q=" + search_term
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    product_names = []
    product_prices = []
    product_quantity = []
    product_uniform_prices = []
    components = soup.find_all('div', class_="product-card-container")

    for component in components:
        name = component.find('h3', attrs={"data-test": "fop-title"}).text.strip() 
        product_names.append(name)
        price = float(component.find('span', attrs={"data-test": "fop-price"}).text.strip().replace("€", "").replace("\xa0", "").replace(",", "."))
        product_prices.append(price)
        cantidad = component.find('div', attrs={"data-test": "fop-size"}).contents[0].text.strip()
        if cantidad.startswith("("):
            cantidad = 1
        product_quantity.append(cantidad)
        uniform_price = float(component.find('div', attrs={"data-test": "fop-size"}).contents[-1].text.strip().replace("(", "").split()[0].replace(",", "."))
        product_uniform_prices.append(uniform_price)

    # Create DataFrame
    df = pd.DataFrame({
        'Name': product_names,
        'Price (€)': product_prices,
        'Cantidad': product_quantity,
        'Uniform Price (€)': product_uniform_prices,
    })

    df['Super'] = 'Alcampo'

    df = df.sort_values("Uniform Price (€)")

    df = df.reset_index(drop=True)
    return df

def eroski(search_term:str)-> pd.DataFrame:
    url = "https://supermercado.eroski.es/es/search/results/?q=" + search_term
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    product_names = []
    product_prices = []
    product_quantity = []
    product_uniform_prices = []
    components = soup.find_all('div', class_="product-item")

    for component in components:
        if len(component.contents) == 0:
            continue
        name = component.find('h2', class_="product-title").text.strip()
        product_names.append(name)
        price = float(component.find('span', class_="price-now").text.strip().replace("€", "").replace("Ahora", "").replace(",", "."))
        product_prices.append(price)
        cantidad = " ".join(name.split()[-2:])
        product_quantity.append(cantidad)
        uniform_price = component.find('span', class_="price-product")
        if uniform_price is not None:
            uniform_price = float(uniform_price.text.strip().replace("€", "").replace("[", "").replace(",", ".").replace("]", ""))
        else:
            uniform_price = price
        product_uniform_prices.append(uniform_price)

    # Create DataFrame
    df2 = pd.DataFrame({
        'Name': product_names,
        'Price (€)': product_prices,
        'Cantidad': product_quantity,
        'Uniform Price (€)': product_uniform_prices,
    })
    df2['Super'] = 'Eroski'

    df2 = df2.sort_values("Uniform Price (€)")

    df2 = df2.reset_index(drop=True)
    return df2


def dia(search_term:str)-> pd.DataFrame:
    url = "https://www.dia.es/api/v1/search-back/search/reduced?q="+ search_term
    headers = {
    'accept': 'application/json',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36',
    'Cookie': 'MUID=0668C04EBE70620B23B6D212BFD86339'
    }
    product_names = []
    product_prices = []
    product_quantity = []
    product_uniform_prices = []
    response = requests.request("GET", url, headers=headers)
    products = response.json()['search_items']
    for product in products:
        name = product['display_name']
        product_names.append(name)
        price = product['prices']['price']
        product_prices.append(price)
        uniform_price = product['prices']['price_per_unit']
        product_uniform_prices.append(uniform_price)
        unidad = product['prices']["measure_unit"]
        cantidad = price/uniform_price
        if unidad == "DOCENA":
            cantidad *=12
            cantidad = str(round(cantidad)) + " uds"
        if unidad == "KILO":
            cantidad *=1000
            cantidad = str(round(cantidad)) + " g"
        if unidad == "LITRO":
            cantidad *=1000
            cantidad = str(round(cantidad)) + " ml"
        if unidad == "UNIDAD":
            cantidad = str(round(cantidad)) + " uds"

        product_quantity.append(cantidad)
    
    # Create DataFrame
    df3 = pd.DataFrame({
        'Name': product_names,
        'Price (€)': product_prices,
        'Cantidad': product_quantity,
        'Uniform Price (€)': product_uniform_prices,
    })
    df3['Super'] = 'Dia'

    df3 = df3.sort_values("Uniform Price (€)")

    df3 = df3.reset_index(drop=True)
    return df3