import matplotlib.pyplot as plt

interval = [
    '0-100.000', 
    '100.001-200.000', 
    '200.001-300.000',
    '300.001-400.000', 
    '400.001-500.000', 
    '500.001-600.000',
    '600.001-700.000', 
    '700.001-800.000',
    '800.001-900.000',
    '900.001-1.000.000'
]
frekuensi = [17, 10, 9, 4, 4, 3, 0, 1, 0, 2]

plt.figure(figsize=(12, 6))
plt.bar(interval, frekuensi, color='skyblue', edgecolor='black', width=0.8)

plt.title('Histogram Pengeluaran untuk Fashion')
plt.xlabel('Interval Pengeluaran')
plt.ylabel('Frekuensi')

for i in range(len(frekuensi)):
    plt.text(i, frekuensi[i] + 0.1, str(frekuensi[i]), ha='center')

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
