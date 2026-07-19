# Proyecto Autores — Historia General de España

> Análisis historiográfico de las fuentes de la *Historia General de España* de Juan de Mariana (1536–1624).
> Trabajo de Fin de Grado · Mayo 2026

---

## 1. Qué investigamos

Juan de Mariana (1536–1624), jesuita e historiador, publicó en 1601 la primera traducción al castellano de su *Historia General de España* (*Historia General de España, compuesta primero en latín, después vuelta en castellano por Juan de Mariana*). En los cuatro primeros libros —que abarcan desde los orígenes míticos de Hispania hasta la caída del Imperio romano de Occidente—, Mariana recurre a **59 autores distintos** para fundamentar su relato.

La pregunta que guía este proyecto es:

> **¿Para qué cita Mariana a cada autor?**

No se trata de determinar si Mariana tuvo acceso físico a las obras que menciona, sino de entender la **función historiográfica** de cada cita dentro de la construcción del relato. Plinio aparece casi siempre para describir la geografía de Hispania. Tito Livio sustenta el relato de guerras y conquistas. San Isidoro actúa como puente entre el mundo clásico y el altomedieval. Y cuando Mariana entra en terreno dudoso —reyes fabulosos, genealogías fantásticas, falsificaciones—, despliega varios autores en contraste, desplegando su escepticismo humanista.

El objeto de estudio son **186 citas distribuidas en los Libros I–IV**, referenciadas contra la edición de 1601 y clasificadas según su función en el argumento de Mariana.

---

## 2. Por qué lo investigamos

### Contexto académico

Este proyecto se enmarca en un **Trabajo de Fin de Grado** cuyo objetivo inicial era responder una pregunta binaria: ¿tuvo Mariana acceso real a los autores que cita? La verificación sistemática de 68 autores en seis catálogos internacionales aportó datos valiosos, pero también puso de manifiesto los límites de esa pregunta. Demostrar que una edición existía antes de 1592 no prueba que Mariana la leyera.

### El giro metodológico

La pregunta original —*¿tuvo acceso?*— se transformó en una más fértil:

> **¿Para qué usa Mariana a cada autor?**

Este cambio no abandona los resultados previos, sino que los recontextualiza. La verificación de existencias bibliográficas pasa a ser un dato de contexto, no el objetivo central. El objetivo nuevo es analizar la **tipología funcional de las citas**: qué categoría de autoridad representa cada autor (geográfica, narrativa, cronológica, bíblica, etimológica, crítica), y cómo se articulan esas autoridades dentro del sistema historiográfico de Mariana.

### Valor del estudio

Comprender el sistema de citas de Mariana permite:

- Reconstituir las **estrategias argumentativas** de un historiador del siglo XVI.
- Identificar las **tradiciones textuales** que nutrieron la historiografía española moderna.
- Detectar los casos en que Mariana opera con **escepticismo** (cita para desacreditar) frente a los que opera con **adhesión** (cita para fundamentar).
- Distinguir entre el uso de **fuentes directas** (ediciones impresas), **transmisión indirecta** (compilaciones medievales) y **fuentes problemáticas** (obras perdidas, falsificaciones).

### Estado actual del proyecto (Julio 2026)

#### Verificación de autores

Se realizó una verificación exhaustiva de las **186 citas** contra los archivos OCR de la edición de 1601. Resultados:

- **Autores verificados como fuentes citadas**: 59 de los 68 autores iniciales resultaron ser citaciones genuinas
- **Autores no encontrados en el OCR**: 9 autores no aparecen como fuentes citadas en los Libros I–IV (algunos aparecen solo como figuras históricas pasajeras o marcas de imprenta)
- **Autores hallados en búsqueda profunda**: 4 autores no incluidos originalmente en la tabla fueron encontrados como fuentes citadas (Filón de Biblos, Nicéforo, Poggio Florentín, Dion Casio)

#### Tabla de autores

La tabla principal (`Tabla de autores 1.md`) contiene:

| Columna | Contenido |
|---------|-----------|
| # | Número de entrada (1–186) |
| Autor | Nombre del autor tal como aparece en Mariana |
| Capítulo | Libro y capítulo de la cita |
| Línea | Línea exacta en el archivo OCR |
| Cita | Extracto textual original del OCR (sin normalizar) |
| Contexto | Descripción del contexto historiográfico de la cita |

Se incluyen además:
- **Resumen por autor** (59 autores con temática y frecuencia de aparición)
- **Autores no encontrados** (9 autores sin citas genuinas en el OCR)
- **Notas sobre la revisión** (12 hallazgos técnicos: duplicaciones OCR, atribuciones erróneas, variantes ortográficas)

---

## 3. Fuentes

### Edición de 1601 — Texto base

La edición de referencia es la **primera traducción al castellano**, publicada en Toledo en 1601 por Pedro Rodríguez.

| Campo | Valor |
|-------|-------|
| Título completo | *Historia General de España, compuesta primero en latín, después vuelta en castellano por Juan de Mariana* |
| Lugar | Toledo |
| Imprenta | Pedro Rodríguez |
| Fecha | 5 de octubre de 1601 |
| Formato | 2 tomos en folio: Tomo I (4h + 1015 pág.), Tomo II (2h + 962 pág. + 13h) |
| OCLC | 36264560 |
| USTC | 5006449 |

El archivo de texto completo (`HGE_TomosI-II.txt`, ~6 MB, 98.805 líneas) fue obtenido del OCR de la digitalización BNE Digital. Para trabajar de forma más cómoda, se dividió en 5 archivos:

| Archivo | Contenido | Líneas |
|---------|-----------|--------|
| `00_portada_indice.txt` | Portada, privilegio, dedicatoria, índice | 254 |
| `01_libro_primero.txt` | Libro I completo | 2.863 |
| `02_libro_segundo.txt` | Libro II completo | 3.109 |
| `03_libro_tercero.txt` | Libro III completo | 2.902 |
| `04_libro_cuarto.txt` | Libro IV completo | 3.165 |

**Notas sobre el TXT**: El archivo proviene de un OCR de una digitalización del siglo XVI. Contiene artefactos de reconocimiento óptico propios de la tipografía de la época (ſ→f, v/u intercambiables, ligaduras rotas, abreviaturas de imprenta). Estos artefactos son predecibles y se mitigan con normalización ortográfica antes de la comparación textual.

### Notas del investigador

El punto de partida empírico del proyecto es un **documento Word** (*Historia general de España.docx*) donde el investigador recogió, durante la lectura de la edición de 1601, las menciones a autores en los Libros I–IV. Cada entrada incluye:

- Libro y capítulo donde aparece la mención.
- Nombre del autor citado (tal como aparece en Mariana).
- Contexto de la cita.
- Función que cumple esa cita dentro del argumento.
- Tipo de fuente.

Esas notas constituyen la **fuente primaria** del proyecto: todo lo que sigue —tablas, validaciones, clasificaciones— se construirá a partir de ellas. El documento Word original no se incluye en el repositorio por derechos de autor.

La tabla resultante (`Tabla de autores 1.md`) fue verificada contra los archivos OCR y completada con las columnas **Cita** (extracto textual original sin normalizar) y **Contexto** (descripción del contexto historiográfico).

### Catálogos de verificación

Para verificar la existencia de cada uno de los 68 autores y la disponibilidad de ediciones anteriores a 1592, se consultaron:

| Catálogo | Función |
|----------|---------|
| [Library of Congress (LOC)](https://www.loc.gov) | Autoridades y registros bibliográficos internacionales |
| [Biblioteca Nacional de España (BNE)](https://www.bne.es) | Catálogo nacional español |
| [Biblioteca de Castilla-La Mancha (CLM)](https://patrimoniodigital.castillalamancha.es) | Fondo del antiguo Colegio de Jesuitas de Toledo |
| [VIAF](https://viaf.org) | Archivos de autoridad internacionales |
| [USTC](https://ustc.ac.uk) | Ediciones europeas impresas antes de 1600 |
| [GW](https://gesamtkatalogderwiegendrucke.de) | Incunables (1450–1500) |
| [CCPB](https://bvpb.mcu.es) | Catálogo Colectivo del Patrimonio Bibliográfico Español |

---

## 4. Estructura del repositorio

```
Proyecto_Autores/
│
├── README.md                          — Bitácora del proyecto
│
├── Tablas/
│   ├── Tabla de autores 1.md          — Tabla principal: 186 citas con Cita y Contexto
│   └── Tabla de capítulos.md          — Estructura de capítulos de los Libros I–IV
│
└── Ediciones_HGE/
    ├── HGE_TomosI-II.txt              — Texto completo de la edición de 1601 (backup, ~6 MB)
    ├── 00_portada_indice.txt          — Portada, privilegio, dedicatoria, índice
    ├── 01_libro_primero.txt           — Libro I (2.863 líneas)
    ├── 02_libro_segundo.txt           — Libro II (3.109 líneas)
    ├── 03_libro_tercero.txt           — Libro III (2.902 líneas)
    └── 04_libro_cuarto.txt            — Libro IV (3.165 líneas)
```

---

## 5. Referencias

### Catálogos

| Catálogo | URL |
|----------|-----|
| Library of Congress (LOC) | https://www.loc.gov |
| Biblioteca Nacional de España (BNE) | https://www.bne.es |
| Biblioteca de Castilla-La Mancha | https://patrimoniodigital.castillalamancha.es |
| VIAF | https://viaf.org |
| USTC | https://ustc.ac.uk |
| GW (Wiegendrucke) | https://gesamtkatalogderwiegendrucke.de |
| CCPB | https://bvpb.mcu.es |

### Bibliotecas digitales

| Biblioteca | URL |
|------------|-----|
| BNE Digital | https://bnedigital.bne.es |
| Gallica (BnF) | https://gallica.bnf.fr |
| Biblioteca Virtual Miguel de Cervantes | https://www.cervantesvirtual.com |
| Internet Archive | https://archive.org |

### Obra de referencia

Mariana, J. de. *Historia General de España*. Toledo, 1601.

---

*Última actualización: Julio 2026*
[Repositorio en GitHub](https://github.com/RRCarlos/Proyecto_Autores)
