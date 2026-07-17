# Proyecto Autores — Registro del Proyecto

> Análisis historiográfico de las fuentes de la *Historia General de España* de Juan de Mariana (1536–1624).  
> Trabajo de Fin de Grado · Mayo 2026

---

## 1. Qué investigamos

Juan de Mariana (1536–1624), jesuita e historiador, publicó en 1592 la versión latina de su *Historia General de España* (*Historiae de rebus Hispaniae libri XX*, Toledo) y en 1601 la primera traducción al castellano. En 1605 publicó la edición latina completa (*Libri XXX*, Maguncia) y en 1617 la edición castellana corregida y aumentada (Madrid). Una de las obras de referencia de la historiografía europea hasta mediados del siglo XIX. En los cuatro primeros libros de esa obra —que abarcan desde los orígenes míticos de Hispania hasta la caída del Imperio romano de Occidente—, Mariana recurre a **68 autores distintos** para fundamentar su relato.

La pregunta que guía este proyecto es:

> **¿Para qué cita Mariana a cada autor?**

No se trata ya de determinar si Mariana tuvo acceso físico a las obras que menciona —pregunta que, aunque legítima, resulta difícil de resolver sin evidencia material directa—, sino de entender la **función historiográfica** de cada cita dentro de la construcción del relato. Plinio aparece casi siempre para describir la geografía de Hispania. Tito Livio sustenta el relato de guerras y conquistas. San Isidoro actúa como puente entre el mundo clásico y el altomedieval. Los autores tardorromanos y medievales (Orosio, Casiodoro, Beda, Sigiberto) anclan cronologías y tradiciones eclesiásticas. Y cuando Mariana entra en terreno dudoso —reyes fabulosos, genealogías fantásticas, falsificaciones—, despliega varios autores en contraste, desplegando su escepticismo humanista.

El objeto de estudio son, por tanto, **180 citas distribuidas en los Libros I–IV** de la *Historia General de España*, referenciadas contra la edición de 1617 y clasificadas según su función en el argumento de Mariana.

---

## 2. Por qué lo investigamos

### Contexto académico

Este proyecto se enmarca en un **Trabajo de Fin de Grado** cuyo objetivo inicial era responder una pregunta binaria: ¿tuvo Mariana acceso real a los autores que cita? La verificación sistemática de 68 autores en seis catálogos internacionales y la validación contra el OCR de la edición de 1617 aportaron datos valiosos, pero también pusieron de manifiesto los límites de esa pregunta. Demostrar que una edición existía antes de 1592 no prueba que Mariana la leyera.

### El giro metodológico

En un momento dado, el investigador reorientó el eje del trabajo. La pregunta original —*¿tuvo acceso?*— se transformó en una más fértil:

> **¿Para qué usa Mariana a cada autor?**

Este cambio no abandona los resultados previos, sino que los recontextualiza. La verificación de existencias bibliográficas pasa a ser un dato de contexto, no el objetivo central. El objetivo nuevo es analizar la **tipología funcional de las citas**: qué categoría de autoridad representa cada autor (geográfica, narrativa, cronológica, bíblica, etimológica, crítica), y cómo se articulan esas autoridades dentro del sistema historiográfico de Mariana.

### Valor del estudio

Comprender el sistema de citas de Mariana permite, entre otras cosas:

- Reconstituir las **estrategias argumentativas** de un historiador del siglo XVI.
- Identificar las **tradiciones textuales** que nutrieron la historiografía española moderna.
- Detectar los casos en que Mariana opera con **escepticismo** (cita para desacreditar) frente a los que opera con **adhesión** (cita para fundamentar).
- Distinguir entre el uso de **fuentes directas** (ediciones impresas), **transmisión indirecta** (compilaciones medievales, florilegios) y **fuentes problemáticas** (obras perdidas, falsificaciones).

---

## 3. Fuentes

### 3.1 Edición de 1601 — Texto base

La edición de referencia para este trabajo es la **primera traducción al castellano**, publicada en Toledo en 1601: *Historia General de España*. El investigador leyó íntegramente los Libros I–IV de esta edición, tomando notas capítulo por capítulo en un documento Word. Toda la extracción de citas y la clasificación funcional de los autores parte de esa lectura directa.

La elección de la edición de 1601 como base metodológica responde a que es la primera versión completa en lengua vernácula y, por tanto, la que Mariana ofreció al público hispanohablante.

### 3.2 Notas del investigador

El punto de partida empírico del proyecto es un **documento Word** (*Historia general de España.docx*) donde el investigador recogió, durante la lectura de la edición de 1601, las menciones a autores en los Libros I–IV. Cada entrada incluye:

- Libro y capítulo donde aparece la mención.
- Nombre del autor citado (tal como aparece en Mariana).
- Contexto de la cita.
- Función que cumple esa cita dentro del argumento.
- Tipo de fuente (realizado a partir de una búsqueda rápida de cada autor).

**Nota:** Durante el procesamiento automatizado, la IA detectó que podían faltar autores en las notas originales. Este aspecto está pendiente de re-verificación.

Esas notas constituyen la **fuente primaria** del proyecto: todo lo que sigue —tablas, validaciones, clasificaciones— se construyó a partir de ellas. El documento Word original no se incluye en el repositorio por derechos de autor, pero su contenido está completamente volcado en `data/tabla_base.csv`.

### 3.3 Edición de 1617 — Testigo auxiliar para OCR

La edición latina ampliada de 1617 (*Historiae de rebus Hispaniae libri XXX*, Maguncia) se incorporó al proyecto como **herramienta de validación**, no como sustituta de la de 1601. Su función es auxiliar: facilitar la localización de pasajes mediante búsqueda de texto.

La razón es práctica: de la edición de 1617 se descargó el tomo primero de Internet Archive y se ejecutó un OCR completo, generando un archivo de texto de **aproximadamente 96.000 líneas** (~3.8 MB). Ese texto permite a los agentes de IA procesar la obra y localizar menciones de autores de forma automatizada. La edición de 1601, en cambio, no está disponible en formato digital procesable.

**Limitaciones importantes:**

- Solo se dispone del **tomo primero** (Libros I–IV). Los tomos II, III y IV de la edición completa no han sido incorporados.
- El OCR de una obra del siglo XVII con tipografía de la época genera **errores significativos**: variantes ortográficas, letras confundidas (larga s → f, v → u), nombres propios distorsionados.
- Todos los resultados de la validación automática están marcados como **"Pendiente de verificación visual"**: el OCR ayuda a localizar pasajes, pero no reemplaza al facsímil.

El corpus se limita a los **Libros I–IV** dentro del tomo primero. No se procesarán libros posteriores salvo necesidad puntual de contraste bibliográfico.

### 3.4 Catálogos de verificación

Para verificar la existencia de cada uno de los 68 autores y la disponibilidad de ediciones anteriores a 1592, se consultaron los siguientes catálogos:

**Catálogo principal:**

| Catálogo | Función |
|----------|---------|
| [Library of Congress (LOC)](https://www.loc.gov) | Autoridades y registros bibliográficos internacionales. Referencia principal para identificación de autores y localización de ediciones. |

**Catálogos secundarios:**

| Catálogo | Función |
|----------|---------|
| [Biblioteca Nacional de España (BNE)](https://www.bne.es) | Catálogo nacional español. Verificación de ediciones hispánicas. |
| [Biblioteca de Castilla-La Mancha (CLM)](https://patrimoniodigital.castillalamancha.es) | Fondo del antiguo Colegio de Jesuitas de Toledo. Localización de exemplares conservados con posible procedencia jesuita. |

**Catálogos complementarios:**

| Catálogo | Función |
|----------|---------|
| [VIAF](https://viaf.org) | Archivos de autoridad internacionales. Cruzamiento de identificadores. |
| [USTC](https://ustc.ac.uk) | Universal Short Title Catalogue. Ediciones europeas impresas antes de 1600. |
| [GW](https://gesamtkatalogderwiegendrucke.de) | Gesamtkatalog der Wiegendrucke. Incunables (1450–1500). |
| [CCPB](https://bvpb.mcu.es) | Catálogo Colectivo del Patrimonio Bibliográfico Español. |

---

## 4. Resultados

### 4.1 Autores verificados

De los **68 autores** identificados en los Libros I–IV, se verificó su existencia y la disponibilidad de ediciones impresas anteriores a 1592 (año de la primera edición de la *Historia General de España*):

| Categoría | Cantidad | Porcentaje |
|-----------|----------|------------|
| Edición pre-1592 verificada | 58 | 85.3% |
| Status especial (ver abajo) | 10 | 14.7% |
| **Total** | **68** | **100%** |

El hecho de que el 85.3% de los autores tuvieran ediciones impresas accesibles antes de 1592 confirma que Mariana **podía** haber tenido acceso a la mayoría de las obras que cita. Sin embargo, como se explicó en la sección 2, la existencia de una edición no prueba el acceso directo.

### 4.2 Autores con status especial

Dentro del grupo de autores cuya situación bibliográfica presenta complejidad, se distinguen cuatro categorías:

**Falsificación:**

| Autor | Problema |
|-------|----------|
| Falso Berroso (Annio de Viterbo) | Giovanni Nanni (1437–1502) publicó en 1498 textos que atribuyó falsamente al historiador babilónico Berroso. La falsificación fue denunciada ya en el siglo XVI por Scaliger. Paradójicamente, Mariana cita a Berroso precisamente para desacreditar las leyendas sobre los primeros reyes de España: usa una falsificación como herramienta de crítica de fuentes. |

**Obras perdidas:**

| Autor | Problema |
|-------|----------|
| Filisto de Siracusa | Obra completamente perdida (11 libros). Solo se conservan fragmentos a través de citas en otros autores. |
| Quinto Fabio Píctor | Obra completamente perdida. Solo se conservan fragmentos citados por Polibio, Dionisio de Halicarnaso, Tito Livio y Plutarco. |

**Principalmente manuscritos:**

| Autor | Problema |
|-------|----------|
| El moro Rasis (al-Razi) | Identidad bibliográfica requiere confirmación adicional. |
| Miguel Sincelo | Principalmente manuscritos. |
| Braulio de Zaragoza | Sin edición incunable verificada. |
| San Ildefonso de Toledo | Sin edición incunable verificada. |

**Autoría dudosa:**

| Autor | Problema |
|-------|----------|
| Julio Capitolino | Compilador de la *Historia Augusta*, atribución cuestionada. |
| Trebellio Polión | Compilador de la *Historia Augusta*, atribución cuestionada. |
| Andrea de' Bardi | No encontrado en catálogos estándar. |

### 4.3 Obras explícitas

Se identificaron **18 casos** en los que Mariana nombra al autor **y** la obra en el mismo pasaje del texto. Este es el estándar más alto de identificación: no solo aparece el nombre del autor, sino que se indica explícitamente qué obra se está consultando. Algunos ejemplos:

| Autor | Obra | Libro | Capítulo |
|-------|------|-------|----------|
| Plinio el Viejo | *Naturalis Historia* | I | I |
| Falso Berroso | *Tablas de Berroso* | I | VII |
| San Isidoro | *Etimologías* | I | VII |
| Platón | *Timeo* | I | XV |
| Antonino | *Itinerario* | I | XVI |
| Filón de Biblos | *Historia de los de Fenicia* | I | XVI |
| Virgilio | *Égloga* | III | XXII |
| Quintiliano | *Instituciones oratorias* | IV | II |
| Braulio | *Vida de Santa Leocadia* | IV | XIII |

La lista completa está en `data/obras_explicitas.md`.

### 4.4 Validación contra la edición de 1617

Se ejecutó una validación automatizada de las 180 citas contra el OCR de la edición de 1617:

| Resultado | Cantidad | Porcentaje |
|-----------|----------|------------|
| Localizado en el OCR | 113 | 62.8% |
| No localizado | 67 | 37.2% |
| **Total** | **180** | **100%** |

Las razones de las no localizaciones son diversas: variantes ortográficas propias de la tipografía del siglo XVII, errores de reconocimiento óptico en nombres propios, menciones que dependen de un contexto más amplio del pasaje, y posibles imprecisiones en las notas originales del investigador.

Todas las validaciones están marcadas como **"Pendiente de verificación visual"** contra el facsímil. La validación automática ayuda a localizar pasajes, pero no sustituye la confrontación directa con la edición impresa.

### 4.5 Ejemplares localizados en CLM

Se consultó la Biblioteca de Castilla-La Mancha (CLM), que conserva los fondos del antiguo Colegio de Jesuitas de Toledo. Se localizaron 11 exemplares con edición anterior a 1592:

| Autor | Obra | Año | Signatura |
|-------|------|-----|-----------|
| Tito Livio | Las Décadas | 1505 | Res.38 |
| Tito Livio | Las quatorze decadas | 1520 | Res.372 |
| Claudio Ptolomeo | Cosmographia | 1486 | Inc.318 |
| Aristóteles | In octo Politicorum | 1500 | Inc.373(I) |
| Platón | Opera omnia | 1548 | FA |
| Marco Tulio Cicerón | Rhetorica ad Herennium | 1496 | FA |
| Séneca el Viejo | Opera | 1529 | FA |
| Antonio de Nebrija | Introductiones | 1540 | FA |
| Ambrosio de Morales | Antigüedades de España | 1574–1575 | FA |
| Lucio Flavio Arriano | Periplus | 1577 | FA |
| Festo Pompeyo | Verrii Flacci quae extant | 1584 | FA |

### 4.6 Incunables más antiguos en CLM

Los incunables más antiguos localizados en la CLM:

| Autor | Año | Signatura GW |
|-------|-----|--------------|
| San Jerónimo (Vulgata) | 1456 | — |
| Cicerón | 1465 | Augusta Vincentiae |
| Virgilio | 1469 | GW M47276 |
| Tito Livio | 1470 | GW M18494 |
| Plutarco | 1470 | GW M34477 |
| Valerio Máximo | 1470 | GW M49160 |
| Pomponio Mela | 1471 | GW M34861 |

### 4.7 Tres vías de transmisión

Las obras llegaron a Mariana principalmente por tres vías:

1. **Ediciones impresas (~70%)** — Desde 1450, los impresores produjeron masivamente ediciones de autores clásicos.
2. **Compilaciones medievales (~20%)** — Autores como San Isidoro o Beda preservaron fragmentos de obras antiguas.
3. **Manuscritos (~10%)** — Para obras menores o fragmentos específicos.

---

## 5. Estado del proyecto

| Área | Estado |
|------|--------|
| Extracción y verificación de autores | ✅ Completo — 68 autores verificados |
| Validación contra OCR 1617 | ✅ Completo — 113/180 localizados |
| Identificación de obras explícitas | ✅ Completo — 18 casos |
| Reorientación metodológica | ✅ Documentada |
| Fase 1 separación OCR (localización edición) | ✅ Completo — edición 1617 verificada, PDF descargado |
| Fase 2 separación OCR (extracción Libros I–IV) | 🔲 Pendiente |
| Transcripción verificada de fragmentos | 🔲 Pendiente — verificación visual contra facsímil |
| Análisis historiográfico | 🔲 Pendiente |
| Redacción de conclusiones | 🔲 Pendiente |

---

## 6. Estructura del repositorio

```
Proyecto_Autores/
│
├── README.md                          — Este archivo: registro del proyecto
│
├── data/
│   ├── tabla_base.csv                 — Tabla principal: 180 citas extraídas del Word
│   ├── validacion_1617.csv            — Resultado de validación contra OCR 1617
│   ├── validacion_por_lotes.md        — Validación detallada por lotes de capítulos
│   └── obras_explicitas.md            — 18 casos con autor + obra nombrados juntos
│
├── scripts/
│   ├── build_citation_use_table.py    — Extrae citas del Word y genera tabla_base
│   ├── validate_table_against_1617.py — Valida cada cita contra el OCR, segmentado por libro/capítulo
│   ├── apply_explicit_works_phase1.py — Identifica obras explícitas en Libro I
│   ├── apply_explicit_works_phase2_complete.py — Identifica obras explícitas en Libros I–IV
│   ├── export_validation_table_md.py  — Exporta validación a Markdown
│   └── summary_phase2.py             — Resumen de obras explícitas por libro
│
└── Ediciones_HGE/
    ├── EDICION_1617_USO.md                       — Ficha completa de la edición 1617 (fuente, OCR, ediciones descartadas)
    ├── mariana_1617_tomo_primero_ocr.txt          — OCR completo del tomo primero (96K líneas, ~3.8 MB)
    ├── mariana_1617_tomo_primero_page_numbers.json — Mapeo de páginas del OCR
    └── PLAN_SEPARACION_OCR.md                     — Plan de separación en Libros I–IV (fase 1 completada)
```

### Descripción de archivos principales

**`data/tabla_base.csv`** — Es el núcleo del proyecto. Contiene las 180 citas extraídas del documento Word original, organizadas con los siguientes campos: orden, libro, capítulo, título del capítulo, autor citado, forma normalizada, obra asociada, pasaje/contexto, función de la cita, tipo de fuente y observaciones.

**`data/validacion_1617.csv`** — Las mismas 180 citas cruzadas con el OCR de la edición de 1617. Indica para cada una si el autor fue localizado o no en el texto impreso.

**`data/validacion_por_lotes.md`** — La validación completa, organizada en 12 lotes por rangos de capítulos. Incluye los fragmentos OCR candidatos y la columna de transcripción verificada manualmente (todavía vacía, pendiente de verificación visual).

**`data/obras_explicitas.md`** — Los 18 casos en los que Mariana nombra al autor y la obra en el mismo pasaje. Incluye la evidencia OCR con las líneas exactas del texto.

**`Ediciones_HGE/mariana_1617_tomo_primero_ocr.txt`** — El archivo de mayor volumen del repositorio. Contiene el texto completo del tomo primero de la edición de 1617, extraído mediante OCR. Es una fuente primaria digitalizada, con todos los errores inherentes al reconocimiento óptico de tipografía del siglo XVII.

---

## 7. Referencias y enlaces

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
| Gallica (BnF) | https://gallica.bnf.fr |
| Biblioteca Virtual Miguel de Cervantes | https://www.cervantesvirtual.com |
| Internet Archive | https://archive.org |

### Obra de referencia

Mariana, J. de. *Historia General de España*. Toledo, 1601. — *Historiae de rebus Hispaniae libri XXX*. Maguncia, 1617.

---

*Registro del proyecto actualizado: Julio 2026*  
[Repositorio en GitHub](https://github.com/RRCarlos/Proyecto_Autores)
