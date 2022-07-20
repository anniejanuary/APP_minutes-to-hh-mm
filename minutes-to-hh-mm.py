#liczba minut, przeliczenie tego na godziny

minutes=67
hours=minutes//60
leftover_minutes=minutes-(hours*60)
print(f"Minutes converted to hh:mm format: {hours} h {leftover_minutes} min")
