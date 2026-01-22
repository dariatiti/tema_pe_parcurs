import pandas as pd
import matplotlib.pyplot as plt
import sys

FILE_PATH = 'data.csv'
X = 14
Y = 8

try:
    df = pd.read_csv(FILE_PATH)
except FileNotFoundError:
    print(f"Eroare: Fișierul '{FILE_PATH}' nu a fost găsit.")
    sys.exit()

plt.figure(figsize=(15, 12))

plt.subplot(3, 1, 1)
for col in df.columns:
    plt.plot(df[col], label=col)
plt.title("Toate valorile din fișier", fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(3, 1, 2)
df_head = df.head(X)
for col in df_head.columns:
    plt.plot(df_head[col], marker='o', label=col)
plt.title(f"Primele {X} valori", fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.subplot(3, 1, 3)
df_tail = df.tail(Y)

if 'Durata' in df.columns and 'Puls' in df.columns:
    plt.plot(df_tail.index, df_tail['Durata'], label='Durata', color='blue', marker='^')
    plt.plot(df_tail.index, df_tail['Puls'], label='Puls', color='red', marker='v')

plt.title(f"Ultimele {Y} valori (Durata și Puls)", fontsize=14)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

print(f"--- Primele {X} înregistrări ---")
print(df_head)

print(f"\n--- Ultimele {Y} înregistrări (Durata și Puls) ---")
if 'Durata' in df.columns and 'Puls' in df.columns:
    print(df_tail[['Durata', 'Puls']])
else:
    print(df_tail)