# Transaction Pattern Analyzer

**Transaction Pattern Analyzer** — утилита для классификации Bitcoin-транзакций по количеству входов и выходов.

## Что делает

- Получает данные о транзакции по TXID
- Анализирует количество входов и выходов
- Делает предположение о типе транзакции:
  - Консолидация
  - Fan-out
  - Обычный перевод
  - Крупная транзакция

## Использование

```bash
python transaction_pattern_analyzer.py <txid>
```

## Пример

```
python transaction_pattern_analyzer.py b6f6991d02f73e...
```

## Вывод

```
🔍 Анализ транзакции: ...
🔢 Входов: 6
🔢 Выходов: 1
🔄 Консолидация входов
```

## Зависимости

- requests

## Лицензия

MIT
