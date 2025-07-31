import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time, re
from datetime import datetime

def setup_driver(headless=False):
    opts = Options()
    opts.add_argument("--disable-blink-features=AutomationControlled")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--disable-notifications")
    opts.add_experimental_option("excludeSwitches", ["enable-automation"])
    opts.add_experimental_option("useAutomationExtension", False)
    if headless:
        opts.add_argument("--headless")
    return webdriver.Chrome(options=opts)

def extract_with_fallback(element, selectors, default="N/A"):
    for sel in selectors:
        try:
            txt = element.find_element(By.CSS_SELECTOR, sel).text.strip()
            if txt:
                return txt
        except:
            continue
    return default

def clean_price(price_text):
    try:
        _ = re.sub(r'[^\d]', '', price_text)
        return float(_) if _ else None
    except:
        return None

def extract_provider_prices(card):
    """Extrae los precios por proveedor de la tabla dentro de cada tarjeta de hotel"""
    providers = {
        "Booking.com": None,
        "Expedia": None,
        "Agoda": None,
        "Atrapalo": None,
        "Cocha": None
    }

    try:
        # Scroll hasta el final del card para asegurar que carguen todos los proveedores
        card.location_once_scrolled_into_view
        time.sleep(0.5)

        # Esperar hasta que aparezcan los items de proveedores dentro del card
        blocks = card.find_elements(By.CSS_SELECTOR, ".hotel__provider-list__item")
        for block in blocks:
            try:
                # Nombre del proveedor
                name = ""
                try:
                    name = block.find_element(By.CSS_SELECTOR, "img").get_attribute("alt").strip()
                except:
                    try:
                        name = block.find_element(By.CSS_SELECTOR, "span").text.strip()
                    except:
                        continue

                # Precio del proveedor
                try:
                    price_txt = block.find_element(By.CSS_SELECTOR, ".hotel__provider-list__item__price").text.strip()
                    price = clean_price(price_txt)
                except:
                    price = None

                # Normalizar y asignar
                n = name.lower()
                if "booking" in n:
                    providers["Booking.com"] = price
                elif "expedia" in n:
                    providers["Expedia"] = price
                elif "agoda" in n:
                    providers["Agoda"] = price
                elif "atrapalo" in n:
                    providers["Atrapalo"] = price
                elif "cocha" in n:
                    providers["Cocha"] = price

            except:
                continue

    except Exception as e:
        print("⚠️ Error en proveedores:", e)

    return providers



def extract_hotel_data(card):
    try:
        name = extract_with_fallback(card, ["h2", ".hotel-card-name", ".hotel-name"], default="N/A")
        # address = extract_with_fallback(card, [".address", "span[class*='address']", ".hotel__address"], default="N/A")
        rating = extract_with_fallback(card, ["span[class*='rating']", ".points", ".hotel-rating"], default="N/A")
        reviews_txt = extract_with_fallback(card, ["span[class*='review']", ".reviews-count"], default="0")
        reviews = int(re.search(r'\d+', reviews_txt).group()) if re.search(r'\d+', reviews_txt) else 0

        providers = extract_provider_prices(card)

        return {
            "Hotel": name,
            # "Dirección": address,
            "Puntuación": rating,
            "Reseñas": reviews,
            **providers
        }

    except Exception as e:
        print("Error:", e)
        return None


def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8-sig", sep=";")
    return df

def main():
    driver = setup_driver(headless=False)
    driver.get("https://www.turismocity.cl/hoteles-en-Santiago_Chile")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card-info-container")))
    time.sleep(5)

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(4)
    cards = driver.find_elements(By.CSS_SELECTOR, ".card-info-container")
    print(f"Encontradas {len(cards)} tarjetas")

    hotel_data = []
    for card in cards:
        d = extract_hotel_data(card)
        if d: hotel_data.append(d)

    driver.quit()
    if hotel_data:
        fn = f"hoteles_santiago_{datetime.now().strftime('%Y%m%d_%H%M')}.csv"
        df = save_to_csv(hotel_data, fn)
        print("✓ Guardado en", fn)
        print(df.head().to_string(index=False))
    else:
        print("⚠️ No se extrajeron datos útiles.")

if __name__ == "__main__":
    main()
