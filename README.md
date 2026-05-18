# TFG Juan de Mariana

## Análisis Historiográfico de las Fuentes de la *Historia General de España* (Libros I-IV, 1601)

---

## Descripción

Este repositorio contiene la documentación del Trabajo de Fin de Grado sobre la historiografía de Juan de Mariana. La investigación responde a la pregunta: **¿Para qué usa Juan de Mariana a cada autor que cita en su *Historia General de España*?** — un análisis de la función historiográfica de las fuentes, no solo de su existencia.

---

## Estructura del proyecto

```
TFG_JUAN_DE_MARIANA/
├── README.md
├── .gitignore
├── docs/                          ← Documentación académica
│   ├── MEMORIA.md
│   ├── PLAN_REORIENTACION_METODOLOGICA.md
│   ├── TABLA_USOS_AUTORES_LIBROS_I_IV.xlsx/.csv         ← Tabla base (180 filas)
│   ├── TABLA_USOS_AUTORES_LIBROS_I_IV_VALIDACION_POR_LOTES.xlsx/.csv/.md  ← Validada
│   ├── TABLA_USOS_AUTORES_LIBROS_I_IV_VALIDADA_1617.xlsx/.csv             ← OCR 1617
│   └── TABLA_USOS_AUTORES_LIBROS_I_IV_OBRAS_EXPLICITAS_COMPLETO.xlsx/.csv/.md
│
├── scripts/                       ← Scripts de generación y validación
│   ├── build_citation_use_table.py
│   ├── validate_table_against_1617.py
│   ├── apply_explicit_works_phase1.py
│   ├── apply_explicit_works_phase2_complete.py
│   ├── export_validation_table_md.py
│   └── summary_phase2.py
│
└── sources/                       ← Fuentes digitalizadas
    ├── mariana_1617_tomo_primero_ocr.txt         ← OCR completo (96k líneas)
    └── mariana_1617_tomo_primero_page_numbers.json
```

### Documentación (`docs/`)

| Documento | Descripción |
|-----------|-------------|
| `MEMORIA.md` | Documento principal con metodología, resultados y análisis |
| `PLAN_REORIENTACION_METODOLOGICA.md` | Plan actualizado tras reunión con experto (2026-05-18) |
| `TABLA_USOS_AUTORES_LIBROS_I_IV.xlsx/.csv` | Tabla base: 180 citas extraídas de notas Word |
| `TABLA_USOS_AUTORES_LIBROS_I_IV_VALIDADA_1617.xlsx/.csv` | Resultados de localización automatizada contra OCR |
| `TABLA_USOS_AUTORES_LIBROS_I_IV_VALIDACION_POR_LOTES.xlsx/.csv/.md` | Validación completa con fragmentos OCR candidatos |
| `TABLA_USOS_AUTORES_LIBROS_I_IV_OBRAS_EXPLICITAS_COMPLETO.xlsx/.csv/.md` | 18 obras explícitas identificadas |

---

## Resultados principales

- **180 citas** de autores en los Libros I-IV de la *Historia General de España* (1601)
- **113 localizadas** en la edición de 1617 mediante OCR automatizado (62.8%)
- **18 obras explícitas** identificadas donde Mariana nombra la obra en el mismo pasaje
- **Eje de investigación**: no determinar "si tuvo acceso", sino **analizar la función** de cada autor en el discurso histórico de Mariana
- **Ediciones de referencia**: 1601 (castellano, texto base) + 1617 (latín ampliado, testigo auxiliar)

---

## Metodología

1. **Extracción**: 180 citas de autores desde notas del Word *Historia general de España*
2. **Validación**: OCR de la edición 1617 (Internet Archive) con localización automatizada
3. **Obras explícitas**: identificación conservadora — solo cuando autor + obra aparecen en el mismo pasaje del OCR
4. **Análisis**: cada cita clasificada por función (autoridad, exemplum, fuente historiográfica, etc.)

**Fuente OCR**: `bub_gb_qpHbv84HpA0C` — Juan de Mariana, *Historia general de España*, tomo I, ed. 1617, Google Books / Internet Archive.

---

## Fases completadas

| Fase | Descripción | Estado |
|------|-------------|--------|
| 1 | Extracción de citas desde notas Word | ✅ |
| 2 | Generación de tabla base (180 filas) | ✅ |
| 3 | Descarga y segmentación OCR 1617 | ✅ |
| 4 | Validación automatizada contra OCR | ✅ |
| 5 | Identificación de obras explícitas (Fase 1+2) | ✅ |
| 6 | Plan metodológico y reorientación | ✅ |
| 7 | Transcripción verificada de fragmentos | 🔲 Pendiente |
| 8 | Análisis historiográfico por función de cita | 🔲 Pendiente |

---

*Última actualización: Mayo 2026*
