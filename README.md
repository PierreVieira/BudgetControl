# BudgetControl

A Python application for tracking and analyzing personal financial transactions, providing detailed breakdowns of expenses and gains with percentage calculations.

## Features

- Parse financial transactions from JSON data
- Categorize transactions by type (expenses and gains)
- Calculate totals and percentages for each transaction
- Split analysis by date ranges (days 1-15 and 15-30)
- Display profit calculations for different periods
- Sort transactions by value

## Project Structure

```
BudgetControl/
├── controller/
│   ├── json_parser.py        # Parses JSON transaction data
│   └── output_generator.py   # Generates formatted output
├── model/
│   ├── transaction.py        # Transaction model
│   ├── transaction_type.py   # Transaction type enum
│   └── transactions.py       # Collection of transactions
├── data.json                 # Transaction data file
└── main.py                   # Entry point
```

## Data Format

The application expects a JSON file (`data.json`) with the following structure:

```json
{
  "15": {
    "expenses": [
      {
        "description": "light bill",
        "value": 147.29
      }
    ],
    "gains": [
      {
        "description": "salary",
        "value": 8000.94
      }
    ]
  },
  "30": {
    "expenses": [...],
    "gains": [...]
  }
}
```

Days represent transaction periods (e.g., day 15 for transactions in the first half, day 30 for second half).

## Usage

Run the application:

```bash
python main.py
```

### Output Example

```
===== GAINS =====
salário (97.49 %): R$ 36622.94
Reembolso do meli (2.51 %): R$ 944.10

Total: R$ 37567.04
===== Expenses =====
nubank (76.44 %): R$ 11000.00
picpay (21.87 %): R$ 3146.15
mercado pago (7.03 %): R$ 1010.65
Faxina (1.56 %): R$ 224.00
luz (1.02 %): R$ 147.29
internet (0.56 %): R$ 79.90
-------------------
Expenses 01-15: R$ 14373.34
Expenses 15-30: R$ 1234.65
Total expenses: R$ 15607.99
===============

Profit 01-15: R$ 23193.70
Profit 15-30: R$ -1234.65
Total profit: R$ 21959.05
```

## Requirements

- Python 3.x
- No external dependencies (uses standard library only)

## License

This project is for personal use.
