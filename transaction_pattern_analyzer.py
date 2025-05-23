"""
Transaction Pattern Analyzer — анализатор паттернов входов и выходов Bitcoin-транзакции.
"""

import requests
import sys

def fetch_transaction(txid):
    url = f"https://blockstream.info/api/tx/{txid}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

def classify_transaction(tx):
    vin = tx['vin']
    vout = tx['vout']
    in_count = len(vin)
    out_count = len(vout)

    print(f"
🔍 Анализ транзакции: {tx['txid']}")
    print(f"🔢 Входов: {in_count}")
    print(f"🔢 Выходов: {out_count}")

    if in_count == 1 and out_count == 2:
        print("🧠 Вероятный обычный перевод с 'change output'")
    elif in_count > 5 and out_count == 1:
        print("🐳 Возможен слив средств с биржи или кошелька")
    elif in_count >= out_count and out_count > 10:
        print("📦 Вероятный 'fan-out' — распределение на множество адресов")
    elif in_count > 1 and out_count == 1:
        print("🔄 Консолидация входов")
    elif out_count == 0:
        print("⚠️ Выходов нет — возможно, это ошибка или особый тип транзакции")
    else:
        print("ℹ️ Стандартная или нестандартная транзакция")

def main():
    if len(sys.argv) != 2:
        print("Использование: python transaction_pattern_analyzer.py <txid>")
        return
    txid = sys.argv[1]
    try:
        tx = fetch_transaction(txid)
        classify_transaction(tx)
    except Exception as e:
        print("Ошибка при анализе:", e)

if __name__ == "__main__":
    main()
