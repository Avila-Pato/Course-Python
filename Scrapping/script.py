import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import re
from datetime import datetime

def setup_driver():
    """Configura el navegador Chrome para scraping"""
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-notifications")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    
    # Descomenta para modo headless
    # options.add_argument("--headless")
    return webdriver.Chrome(options=options)

def extract_hotel_data(card):
    """Extrae datos detallados de cada hotel con selectores actualizados"""
    try:
        # 1. Nombre del hotel
        hotel_name = card.find_element(By.CSS_SELECTOR, "h2.hotel-title").text.strip()
        
        # 2. Dirección (selector actualizado)
        address = extract_with_fallback(
            card, 
            "div.hotel__address", 
            "div.hotel-address", 
            "div.address",
            default="N/A"
        )
        
        # 3. Puntuación (selector actualizado)
        rating = extract_with_fallback(
            card, 
            "span.green.points", 
            "span.hotel-rating", 
            "div.rating-value",
            default="N/A"
        )
        
        # 4. Número de reseñas (selector actualizado)
        reviews_text = extract_with_fallback(
            card, 
            "span.reviews-count", 
            "span.review-count", 
            default="0"
        )
        reviews = int(re.search(r'\d+', reviews_text).group()) if reviews_text != "0" else 0
        
        # 5. Precios por proveedor
        providers = extract_provider_prices(card)
        
        return {
            "Hotel": hotel_name,
            "Dirección": address,
            "Puntuación": rating,
            "Reseñas": reviews,
            **providers
        }
    except Exception as e:
        print(f"Error procesando hotel: {str(e)}")
        return None

def extract_provider_prices(card):
    """Extrae precios exactos por proveedor con selectores específicos"""
    providers = {
        "Booking.com": None,
        "Expedia": None,
        "Agoda": None,
        "Atrapalo": None,
        "Cocha": None
    }
    
    try:
        # Buscar todos los bloques de proveedores
        provider_blocks = card.find_elements(By.CSS_SELECTOR, "div.hotel__provider-list__item")
        
        for block in provider_blocks:
            try:
                # Extraer nombre del proveedor (de la imagen o texto)
                name = extract_provider_name(block)
                if not name:
                    continue
                    
                # Extraer precio (selector específico)
                price_text = extract_with_fallback(
                    block, 
                    "span.hotel__provider-list__item__price", 
                    "div.price-value", 
                    "span.price-main",
                    default=""
                )
                
                if not price_text:
                    continue
                    
                # Limpiar y convertir el precio
                price = clean_price(price_text)
                
                # Asignar al proveedor correspondiente
                if "booking" in name.lower():
                    providers["Booking.com"] = price
                elif "expedia" in name.lower():
                    providers["Expedia"] = price
                elif "agoda" in name.lower():
                    providers["Agoda"] = price
                elif "atrapalo" in name.lower():
                    providers["Atrapalo"] = price
                elif "cocha" in name.lower():
                    providers["Cocha"] = price
                    
            except Exception:
                continue
                
    except NoSuchElementException:
        pass
    
    return providers

def extract_provider_name(block):
    """Extrae el nombre del proveedor de diferentes formas"""
    try:
        # Primero intentar con la imagen (alt text)
        return block.find_element(By.CSS_SELECTOR, "img").get_attribute("alt").strip()
    except:
        try:
            # Luego intentar con el texto visible
            return block.find_element(By.CSS_SELECTOR, "div.provider-name").text.strip()
        except:
            return ""

def clean_price(price_text):
    """Limpia y convierte el texto del precio a número"""
    try:
        # Eliminar símbolos no numéricos
        clean_text = re.sub(r'[^\d.]', '', price_text.replace('.', ''))
        return float(clean_text) if clean_text else None
    except:
        return None

def extract_with_fallback(element, *selectors, default="N/A"):
    """Intenta múltiples selectores hasta encontrar el elemento"""
    for selector in selectors:
        try:
            return element.find_element(By.CSS_SELECTOR, selector).text.strip()
        except NoSuchElementException:
            continue
    return default

def save_to_csv(data, filename):
    """Guarda los datos en CSV con formato adecuado"""
    if not data:
        return pd.DataFrame()
    
    df = pd.DataFrame(data)
    
    # Formatear precios para visualización
    for provider in ["Booking.com", "Expedia", "Agoda", "Atrapalo", "Cocha"]:
        if provider in df.columns:
            df[provider] = df[provider].apply(
                lambda x: f"${x:,.0f}".replace(",", ".") if pd.notnull(x) and x != "" else "N/A"
            )
    
    # Ordenar columnas
    columns_order = ["Hotel", "Dirección", "Puntuación", "Reseñas", 
                    "Booking.com", "Expedia", "Agoda", "Atrapalo", "Cocha"]
    df = df[[col for col in columns_order if col in df.columns]]
    
    # Guardar archivo
    df.to_csv(filename, index=False, sep=";", encoding="utf-8-sig")
    return df

def main():
    print("🚀 Iniciando scraping de turismocity.cl...")
    driver = setup_driver()
    hotel_data = []
    
    try:
        # Acceder a la página
        print("🌐 Cargando página...")
        driver.get("https://www.turismocity.cl/hoteles-en-Santiago_Chile")
        
        # Esperar a que cargue el contenido
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.card-info-container"))
        )
        print("✅ Página cargada correctamente")
        
        # Desplazarse para cargar más hoteles
        print("🔄 Desplazando para cargar más hoteles...")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(2)
        driver.execute_script("window.scrollTo(0, 0)")
        time.sleep(1)
        
        # Obtener todas las tarjetas de hoteles
        cards = driver.find_elements(By.CSS_SELECTOR, "div.card-info-container")
        print(f"🔍 Encontradas {len(cards)} tarjetas de hoteles")
        
        # Procesar cada hotel
        for i, card in enumerate(cards, 1):
            print(f"🏨 Procesando hotel {i}/{len(cards)}...")
            hotel = extract_hotel_data(card)
            if hotel:
                hotel_data.append(hotel)
        print(f"✅ Datos de {len(hotel_data)} hoteles extraídos correctamente")
                
    except TimeoutException:
        print("⏱️ Error: Tiempo de espera agotado al cargar la página")
    except Exception as e:
        print(f"❌ Error crítico: {str(e)}")
    finally:
        driver.quit()
    
    # Guardar resultados
    if hotel_data:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"hoteles_santiago_{timestamp}.csv"
        df = save_to_csv(hotel_data, filename)
        
        print(f"\n✅ Datos guardados en '{filename}'")
        print("📊 Resumen estadístico:")
        print(f"- Total hoteles: {len(df)}")
        print(f"- Hoteles con puntuación: {len(df[df['Puntuación'] != 'N/A'])}")
        
        # Calcular promedios
        for provider in ["Booking.com", "Expedia", "Agoda", "Atrapalo", "Cocha"]:
            if provider in df.columns:
                # Convertir a numérico para cálculo
                prices = df[provider].replace("N/A", None).replace(r'[^\d.]', '', regex=True)
                prices = pd.to_numeric(prices, errors="coerce")
                avg_price = prices.mean()
                
                if pd.notna(avg_price):
                    print(f"- Precio promedio ({provider}): ${avg_price:,.0f}".replace(",", "."))
                else:
                    print(f"- Sin precios disponibles para {provider}")
        
        # Mostrar muestra de datos
        print("\n🔍 Muestra de datos:")
        print(df.head().to_string(index=False))
    else:
        print("❌ No se extrajeron datos válidos")

if __name__ == "__main__":
    main()