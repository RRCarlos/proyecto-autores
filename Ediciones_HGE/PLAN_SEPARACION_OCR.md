# Plan: Separación del OCR en Libros I–IV

## Objetivo

Obtener los textos individualizados de los Libros I, II, III y IV de la edición de 1617 de la *Historia General de España* de Juan de Mariana, partiendo directamente del PDF digitalizado, y verificarlos contra el OCR existente (`mariana_1617_tomo_primero_ocr.txt`).

---

## Fase 1: Localizar la edición de 1617

| Tarea | Descripción |
|-------|-------------|
| 1.1 | Buscar la edición de 1617 en Internet Archive |
| 1.2 | Confirmar que es el tomo primero (que contiene los Libros I–IV) |
| 1.3 | Verificar la estructura del PDF (número de páginas, rango de Libros I–IV) |
| 1.4 | **Proporcionar el link de descarga** para verificación manual paralela por el investigador |

**Criterio de aceptación:** PDF localizado, confirmado como tomo primero, link de descarga entregado.

---

## Fase 2: Extraer el OCR de los Libros I–IV

> **Nota:** Se trabaja directamente con el PDF. El archivo `mariana_1617_tomo_primero_ocr.txt` se trata como si no existiera en esta fase.

| Tarea | Descripción |
|-------|-------------|
| 2.1 | Identificar en el PDF dónde empieza y termina el bloque de Libros I–IV (excluyendo prólogo, tabla de contenidos y otros libros) |
| 2.2 | Extraer solo el texto correspondiente a Libros I–IV directamente del PDF |
| 2.3 | Guardar como `mariana_1617_libros_i_iv_ocr.txt` en `Ediciones_HGE/` |

**Criterio de aceptación:** Archivo generado que contiene exclusivamente el texto de Libros I–IV.

---

## Fase 3: Separar en 4 documentos

| Tarea | Descripción |
|-------|-------------|
| 3.1 | Localizar los límites exactos entre Libro I / II / III / IV |
| 3.2 | Generar `libro_i.txt`, `libro_ii.txt`, `libro_iii.txt`, `libro_iv.txt` |
| 3.3 | Almacenar en `Ediciones_HGE/` |

**Criterio de aceptación:** 4 archivos generados, uno por libro, con contenido completo y sin solapamientos.

---

## Fase 4: Verificación

> **Referencia:** `mariana_1617_tomo_primero_ocr.txt` (el OCR existente del tomo completo).

| Tarea | Descripción |
|-------|-------------|
| 4.1 | Verificar Libro I: contenido extraído vs. OCR de referencia |
| 4.2 | Verificar Libro II |
| 4.3 | Verificar Libro III |
| 4.4 | Verificar Libro IV |
| 4.5 | Reportar discrepancias (si las hay) |

**Criterio de aceptación:** Los 4 archivos coinciden con el OCR de referencia o las diferencias están justificadas y documentadas.

---

## Fase 5: Limpieza y commit

| Tarea | Descripción |
|-------|-------------|
| 5.1 | Identificar qué archivos de `Ediciones_HGE/` van a eliminarse |
| 5.2 | **El investigador valida** la lista de borrado |
| 5.3 | Borrar lo aprobado |
| 5.4 | Actualizar README.md (árbol de repositorio y descripciones) |
| 5.5 | Commit y push a GitHub |

**Criterio de aceptación:** Repositorio limpio con solo los 4 libros individualizados + `mariana_1617_tomo_primero_page_numbers.json`. README actualizado.

---

## Archivos resultantes esperados en `Ediciones_HGE/`

```
Ediciones_HGE/
├── libro_i.txt
├── libro_ii.txt
├── libro_iii.txt
├── libro_iv.txt
└── mariana_1617_tomo_primero_page_numbers.json
```

---

## Notas

- `mariana_1617_tomo_primero_page_numbers.json` se conserva (puede ser útil).
- El investigador realizará una verificación manual paralela usando el PDF descargado en la Fase 1.
- Si se detectan discrepancias significativas en la Fase 4, se detiene el proceso y se analizan antes de continuar.
