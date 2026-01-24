from datetime import datetime, timedelta

# Разница в 5 дней
delta = timedelta(days=5)
print(delta)

today = datetime.today()
print(today)
future_date = today + timedelta(days=10, hours=2)
print(future_date)
