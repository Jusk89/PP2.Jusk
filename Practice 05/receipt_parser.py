import re
import json

def extract_prices(receipt_text):
    price_pattern = r'(\d{1,3}(?:\s?\d{3})*(?:,\d{2})?)'
    prices = re.findall(price_pattern, receipt_text)
    
    clean_prices = [price.replace(' ', '').replace(',', '.') for price in prices]
    return clean_prices

def find_product_names(receipt_text):
    # Регулярное выражение для поиска названий товаров
    product_pattern = r'(\d+\.\s.*?)(\d{1,3}(?:\s?\d{3})*(?:,\d{2})?)'
    products = re.findall(product_pattern, receipt_text)
    product_names = [product[0].strip() for product in products]
    return product_names

def calculate_total(receipt_text):
    # Регулярное выражение для поиска общей суммы
    total_pattern = r'ИТОГО:\s*(\d{1,3}(?:\s?\d{3})*(?:,\d{2})?)'
    total = re.search(total_pattern, receipt_text)
    return total.group(1) if total else None

def extract_date_time(receipt_text):
    # Регулярное выражение для поиска даты и времени
    date_time_pattern = r'Время:\s*(\d{2}\.\d{2}\.\d{4} \d{2}:\d{2}:\d{2})'
    date_time = re.search(date_time_pattern, receipt_text)
    return date_time.group(1) if date_time else None

def find_payment_method(receipt_text):
    # Обновляем регулярное выражение для извлечения БИН с "Банковская карта:"
    payment_pattern = r'БИН\s*(\d{12})'  # Ищем первые 6 цифр после фразы "Банковская карта:"
    payment = re.search(payment_pattern, receipt_text)
    
    if payment:
        return payment.group(1)  # Возвращаем первые 6 цифр (БИН)
    else:
        return "БИН не найден"

def parse_receipt(receipt_text):
    receipt_data = {}
    
    # Извлечение нужных данных
    receipt_data["prices"] = extract_prices(receipt_text)
    receipt_data["products"] = find_product_names(receipt_text)
    receipt_data["total"] = calculate_total(receipt_text)
    receipt_data["date_time"] = extract_date_time(receipt_text)
    receipt_data["payment_method"] = find_payment_method(receipt_text)
    
    return receipt_data

def create_structured_output(parsed_data):
    # Форматируем вывод в виде текста с отступами и разделением
    structured_output = ""
    structured_output += f"Дата и время: {parsed_data['date_time']}\n\n"
    structured_output += f"Метод оплаты (БИН): {parsed_data['payment_method']}\n\n"
    structured_output += "Товары:\n"
    
    for idx, product in enumerate(parsed_data['products']):
        structured_output += f"{idx+1}. {product}\n"
        structured_output += f"Цена: {parsed_data['prices'][idx]}\n\n"
    
    structured_output += f"Итого: {parsed_data['total']}\n"
    return structured_output

def main():
    # Загрузить данные из файла
    with open('raw.txt', 'r', encoding='utf-8') as file:
        receipt_text = file.read()
    
    # Парсим данные из чека
    parsed_data = parse_receipt(receipt_text)
    
    # Форматируем и выводим структурированный текст
    structured_output = create_structured_output(parsed_data)
    print(structured_output)

if __name__ == "__main__":
    main()