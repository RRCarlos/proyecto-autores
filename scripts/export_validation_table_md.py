from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_IN = ROOT / "docs" / "TABLA_USOS_AUTORES_LIBROS_I_IV_VALIDACION_POR_LOTES.csv"
MD_OUT = ROOT / "docs" / "TABLA_USOS_AUTORES_LIBROS_I_IV_VALIDACION_POR_LOTES.md"


def esc(value: str) -> str:
    return (value or "").replace("|", "\\|").replace("\n", "<br>").strip()


def main() -> None:
    with CSV_IN.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))

    groups: dict[str, list[dict[str, str]]] = {}
    for row in rows:
        groups.setdefault(row["Lote de revisión"], []).append(row)

    lines: list[str] = []
    lines.append("# Tabla de usos de autores — Validación por lotes")
    lines.append("")
    lines.append("Documento de trabajo para validar las menciones de autores en los Libros I-IV de la *Historia General de España* contra la edición de 1617.")
    lines.append("")
    lines.append("> **Criterio importante:** el campo `Fragmento OCR candidato 1617` no es una cita literal fiable. Solo sirve para localizar el pasaje. La cita válida debe escribirse en `Transcripción verificada manualmente` tras comprobar el facsímil.")
    lines.append("")

    cols = [
        "Orden",
        "Libro",
        "Capítulo",
        "Autor citado",
        "Pasaje / contexto",
        "Validación 1617",
        "Fragmento OCR candidato 1617",
        "Transcripción verificada manualmente",
        "Estado transcripción",
    ]

    for lote, lote_rows in groups.items():
        lines.append(f"## {esc(lote)}")
        lines.append("")
        lines.append("| " + " | ".join(cols) + " |")
        lines.append("| " + " | ".join(["---"] * len(cols)) + " |")
        for row in lote_rows:
            lines.append("| " + " | ".join(esc(row.get(col, "")) for col in cols) + " |")
        lines.append("")

    MD_OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"created {MD_OUT}")


if __name__ == "__main__":
    main()
