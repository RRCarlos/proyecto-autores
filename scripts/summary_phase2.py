import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
csv_path = ROOT / "docs" / "TABLA_USOS_AUTORES_LIBROS_I_IV_OBRAS_EXPLICITAS_COMPLETO.csv"

with csv_path.open("r", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

assigned = [r for r in rows if r["Obra asociada"]]
print(f"Total filas con obra explícita: {len(assigned)}")
by_book = {}
for r in assigned:
    by_book[r["Libro"]] = by_book.get(r["Libro"], 0) + 1

for bk, cnt in sorted(by_book.items()):
    print(f"  {bk}: {cnt} filas")
print()

for r in assigned:
    print(f"  Orden {r['Orden']:>3s} | {r['Libro']} | {r['Autor citado']:<30s} -> {r['Obra asociada']}")
