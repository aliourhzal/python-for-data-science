from datetime import datetime

now = datetime.now();
formated = f"Seconds since January 1, 1970: {now.timestamp():,} or {now.timestamp():.2e} in scientific notation"
print(formated)
formated = f"{now.strftime('%b')} {now.strftime('%d')} {now.strftime('%Y')}"
print(formated)


