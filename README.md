# Proyecto Autores — Historia General de España

> Análisis historiográfico de las fuentes de la *Historia General de España* de Juan de Mariana (1536–1624).
> Trabajo de Fin de Grado · Mayo 2026

---

## 1. Qué investigamos

Juan de Mariana (1536–1624), jesuita e historiador, publicó en 1601 la primera traducción al castellano de su *Historia General de España* (*Historia General de España, compuesta primero en latín, después vuelta en castellano por Juan de Mariana*). En los cuatro primeros libros —que abarcan desde los orígenes míticos de Hispania hasta la caída del Imperio romano de Occidente—, Mariana recurre a **77 autores distintos (76 fuentes externas + 1 autoreferencia)** para fundamentar su relato.

La pregunta que guía este proyecto es:

> **¿Para qué cita Mariana a cada autor?**

No se trata de determinar si Mariana tuvo acceso físico a las obras que menciona, sino de entender la **función historiográfica** de cada cita dentro de la construcción del relato. Plinio aparece casi siempre para describir la geografía de Hispania. Tito Livio sustenta el relato de guerras y conquistas. San Isidoro actúa como puente entre el mundo clásico y el altomedieval. Y cuando Mariana entra en terreno dudoso —reyes fabulosos, genealogías fantásticas, falsificaciones—, despliega varios autores en contraste, desplegando su escepticismo humanista.

El objeto de estudio son **209 citas a fuentes externas y 2 autoreferencias distribuidas en los Libros I–IV**, referenciadas contra la edición de 1601 y clasificadas según su función en el argumento de Mariana.

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

Se realizó una verificación exhaustiva de las **209 citas** contra los archivos OCR de la edición de 1601. Además, se hizo un barrido sistemático de **25 capítulos sin citas** en busca de nuevas referencias. Resultados:

- **Autores verificados como fuentes citadas**: 76 autores externos resultaron ser citaciones genuinas (incluidos San Agustín y Juan Margarite, localizados e indexados en julio de 2026)
- **Autores no encontrados en el OCR**: 6 autores no aparecen como fuentes citadas en los Libros I–IV (Casiodoro, Filisto, Hilderico, Miguel Sincelo, Hernando del Pulgar, Arriano en LIV)
- **Barrido de capítulos**: de 25 capítulos vacíos, se hallaron **6 citas nuevas** (Rufo Festo y Tito Livio en L.I CAP XXI; Trebellio Polión y San Jerónimo en L.IV; San Agustín ×2 en L.IV; Juan Margarite en L.III)

#### Tabla de autores

La tabla principal (`Tabla de autores 1.md`) contiene:

| Columna | Contenido |
|---------|-----------|
| # | Número de entrada (1–209) |
| Autor | Nombre del autor tal como aparece en Mariana |
| Capítulo | Libro y capítulo de la cita |
| Línea | Línea exacta en el archivo OCR |
| Cita | Extracto textual original del OCR (sin normalizar) |
| Contexto | Descripción del contexto historiográfico de la cita |

Se incluyen además:
- **Resumen por autor** (77 autores con temática y frecuencia de aparición)
- **Autoreferencias de Juan de Mariana** (2 remisiones a su *Historiae de Rebus Hispaniae* de 1592)
- **Autores no encontrados** (6 autores sin citas genuinas en el OCR)
- **Notas sobre la revisión** (6 hallazgos verificados: duplicaciones OCR, atribuciones erróneas, variantes ortográficas, barrido de capítulos, recuperación de autores perdidos, indexación de San Agustín y Juan Margarite)

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

El punto de partida empírico del proyecto es un **documento Word** (*Historia general de España.docx*) donde el investigador recogió, durante la lectura de la edición de 1601, las menciones a autores en los Libros I–IV. Una versión en texto plano de esas notas se incluye en el repositorio (`Notas/Apuntes sobre HGE Cap I-IV.txt`, 795 líneas). Cada entrada incluye:

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
proyecto-autores/
│
├── README.md                          — Bitácora del proyecto
│
├── Tablas/
│   ├── Tabla de autores 1.md          — Tabla principal: 209 citas con Cita y Contexto
│   └── Tabla de capítulos.md          — Estructura de capítulos de los Libros I–IV
│
├── Datos/
│   └── Relación_de_datos.md           — Análisis cuantitativo y cualitativo de las citas
│
├── Notas/
│   └── Apuntes sobre HGE Cap I-IV.txt — Notas del investigador: menciones a autores en Libros I–IV
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

## 5. Análisis cuantitativo de las citas

El análisis completo se encuentra en [`Datos/Relación_de_datos.md`](Datos/Relación_de_datos.md). A continuación se presentan los resultados principales.

### 5.1 Panorama general

| Métrica | Valor |
|---------|-------|
| Total de citas (apariciones) | 209 |
| Autores únicos | 77 (76 externos + 1 autoref) |
| Libros cubiertos | 4 (I–IV) |
| Capítulos con al menos 1 cita | 82 de 92 |
| Autores que acaparan el 50 % de las citas | 13 de 77 (16,9 %) |
| Autor más citado | Plinio (20 citas, 9,6 %) |
| Libro con más citas | Libro Cuarto (75 citas, 35,9 %) |
| Libro con más autores únicos | Libro Cuarto (41 autores) |
| Autores citados en 3+ libros | 12 de 77 (15,6 %) |
| Autores de una sola aparición | 41 de 77 (53,2 %) |

### 5.2 Ranking de frecuencia — Top 15

| Pos. | Autor | Apariciones | % | Libros | Categoría |
|------|-------|-------------|---|--------|-----------|
| 1 | Plinio | 20 | 9,6 % | I–IV | Geógrafo/enciclopedista |
| 2 | Claudio Ptolomeo | 14 | 6,7 % | I–IV | Geógrafo |
| 3 | Marco Varrón | 11 | 5,3 % | I–IV | Erudito/gramático |
| 4 | Dion Casio | 8 | 3,8 % | III, IV | Historiador |
| 5 | Plutarco | 8 | 3,8 % | I–IV | Biógrafo/moralista |
| 6 | Cicerón | 7 | 3,3 % | III, IV | Filósofo/orador |
| 7 | San Isidoro de Sevilla | 7 | 3,3 % | I, III, IV | Polígrafo eclesiástico |
| 8 | Séneca | 7 | 3,3 % | III, IV | Filósofo/orador |
| 9 | Prudencio | 6 | 2,9 % | IV | Poeta cristiano |
| 10 | Tito Livio | 6 | 2,9 % | I, II, IV | Historiador |
| 11 | Apiano | 5 | 2,4 % | I, III | Historiador |
| 12 | Cayo Silio Italico | 5 | 2,4 % | II, IV | Poeta épico |
| 13 | Estrabón | 5 | 2,4 % | I, III | Geógrafo |
| 14 | Quintiliano | 5 | 2,4 % | IV | Retórico |
| 15 | Polibio | 4 | 1,9 % | I, II | Historiador |

### 5.3 Curva de Pareto

| Grupo | Autores | % autores | Citas | % citas |
|-------|---------|-----------|-------|---------|
| Top 5 | Plinio, Ptolomeo, Varrón, Dion, Plutarco | 6,5 % | 61 | 29,2 % |
| Top 10 | + Cicerón, Isidoro, Séneca, Prudencio, T. Livio | 13,0 % | 94 | 45,0 % |
| Top 15 | + Apiano, Silio, Estrabón, Quintiliano, Polibio | 19,5 % | 118 | 56,5 % |
| Top 20 | + Amiano, Aristóteles, Solino, Suetonio, Diodoro | 26,0 % | 133 | 63,6 % |
| Todos (77) | — | 100 % | 209 | 100 % |

**Interpretación:** Un tercio de los autores concentra dos tercios de las citas. El patrón es típico de una obra historiográfica humanista: unas pocas autoridades fundacionales (Plinio, Ptolomeo, Varrón) sostienen la mayor parte del aparato erudito, mientras que la «cola larga» de 41 autores de una sola aparición refleja menciones puntuales, curiosidades eruditas o referencias de apoyo circunstancial.

### 5.4 Distribución por libro

| Libro | Entradas | % | Autores únicos | Densidad (citas/cap.) |
|-------|----------|---|----------------|-----------------------|
| Libro Primero | 49 | 23,4 % | 27 | 2,2 |
| Libro Segundo | 30 | 14,4 % | 17 | 1,8 |
| Libro Tercero | 55 | 26,3 % | 22 | 2,2 |
| Libro Cuarto | 75 | 35,9 % | 41 | 3,0 |
| **Total** | **209** | **100 %** | **77** | **2,3** |

**Interpretación:** El Libro Cuarto concentra la mayor densidad de citas (3,0 por capítulo) y el mayor número de autores únicos (41). Esto se explica porque abarca el Imperio romano tardío —una etapa con más fuentes disponibles, más tradiciones historiográficas y más polemica interpretativa—. El Libro Segundo, por el contrario, es el más parco (30 citas, 17 autores): corresponde a un período más oscuro (período prefilial), con menos fuentes clásicas accesibles.

### 5.5 Autores transculturales (presentes en varios libros)

| Libros | N.º autores | Ejemplos |
|--------|-------------|----------|
| 4 libros (I–IV) | 4 | Plinio, Ptolomeo, Varrón, Plutarco |
| 3 libros | 5 | San Isidoro, Tito Livio, Estrabón, Apiano, Orosio |
| 2 libros | 21 | Dion Casio, Cicerón, Séneca, Silio Italico, etc. |
| 1 libro | 47 | El resto |

**Interpretación:** Solo 4 autores aparecen en los cuatro libros: Plinio, Ptolomeo, Varrón y Plutarco. Son las «columnas vertebrales» de la erudición de Mariana —fuentes que consulta a lo largo de toda la obra—. Los 47 autores de un solo libro representan referencias localizadas: un geógrafo para una descripción concreta, un poeta épico para un episodio particular, un eclesiástico para un punto de teología.

### 5.6 Categorías de autores

| Categoría | Autores | Citas | % citas |
|-----------|---------|-------|---------|
| Historiadores | 18 | 55 | 26,3 % |
| Geógrafos | 5 | 44 | 21,1 % |
| Eclesiásticos | 17 | 31 | 14,8 % |
| Filósofos/oradores | 7 | 28 | 13,4 % |
| Poetas | 6 | 17 | 8,1 % |
| Eruditos/polígrafos | 6 | 14 | 6,7 % |
| Otros (biógrafos, compiladores, etc.) | 18 | 20 | 9,6 % |

**Interpretación:** Los historiadores son la categoría más numerosa (18 autores), pero los geógrafos —pocos en número (5)— acaparan la mayor cuota de citas (21,1 %) gracias a la preponderancia de Plinio y Ptolomeo. Esto refleja una de las características distintivas de la HGE: la obsesión por situar geográficamente cada evento en el territorio hispano. Los eclesiásticos (17 autores, 14,8 %) aparecen sobre todo en el Libro Cuarto, cuando el relato entra en contacto con el mundo cristiano.

### 5.7 Paganos versus cristianos

| Tipo | Autores | Citas | % |
|------|---------|-------|---|
| Paganos | 59 | 155 | 74,2 % |
| Cristianos | 18 | 38 | 18,2 % |
| Indeterminados | — | 16 | 7,7 % |

**Interpretación:** Mariana se apoya predominantemente en fuentes paganas (74,2 %), coherente con su proyecto de escribir una historia de España desde los orígenes hasta su época, empezando por los autores clásicos grecolatinos. La proporción de autores cristianos (18,2 %) crece significativamente en el Libro Cuarto, cuando el relato llega al Bajo Imperio y la romanización cristiana.

### 5.8 Distribución cronológica de las fuentes

| Período | Autores | Citas | % citas |
|---------|---------|-------|---------|
| Antigüedad clásica (s. V a.C.–II d.C.) | 30 | 110 | 52,6 % |
| Imperio romano tardío (s. III–V) | 12 | 34 | 16,3 % |
| Alta Edad Media (s. VI–X) | 10 | 22 | 10,5 % |
| Plena Edad Media (s. XI–XV) | 14 | 18 | 8,6 % |
| Renacimiento (s. XVI) | 9 | 15 | 7,2 % |
| Indeterminados | 2 | 10 | 4,8 % |

**Interpretación:** Más de la mitad de las citas se remontan a la antigüedad clásica (52,6 %), lo que confirma la orientación humanista de Mariana: su modelo historiográfico se ancla en los autores grecolatinos. Las fuentes altomedievales (10,5 %) incluyen autores como San Isidoro y Alcuino, que Mariana utiliza como puente entre el mundo clásico y la España visigoda. Las fuentes renacentistas (7,2 %) incluyen a Juan Margarite y otros autores contemporáneos con los que Mariana dialoga o polemiza.

### 5.9 Autores más densos por capítulo

| Capítulo | Libro | Citas | Autores principales |
|----------|-------|-------|---------------------|
| Cap. XII | IV | 14 | Prudencio (6), Quintiliano (5), Amiano (3) |
| Cap. XXIIII | III | 7 | Cicerón (1), Dion (×2), Isidoro (×3), Juan Margarite (1) |
| Cap. I | IV | 5 | San Agustín (1), Dion, Plinio, otros |
| Cap. XVII | III | 5 | Séneca (3), Dion Casio (2) |

**Interpretación:** El capítulo XII del Libro Cuarto es el más denso (14 citas), dedicado a la persecución de Diocleciano y la resistencia cristiana. Mariana despliega aquí un aparato erudito excepcional para dar credibilidad a un relato cargado de implicaciones teológicas.

### 5.10 Mariana como crítico (14 citas)

En 14 de las 209 citas, Mariana no cita para fundamentar, sino para **desacreditar o corregir** a un autor:

- **Juan Margarite** (III, XXIIII): Mariana corrige su cálculo sobre la Era del César.
- **San Agustín** (IV, I): Mariana señala la discrepancia en los nombres de los cónsules del año de fundación de Roma.
- **San Agustín** (IV, XII): Referencia a edictos contra los cristianos; Mariana usa su autoridad para situar la cronología.
- **Nepote, Floro, Orosio, M. Varrón, Eusebio**: Correcciones o matices en cálculos cronológicos.
- **Dion, Justino, Plutarco, Tito Livio**: Variantes narrativas o desacuerdos sobre hechos concretos.

**Interpretación:** Estas 14 citas de tipo crítico (6,7 % del total) revelan el escepticismo humanista de Mariana. No se limita a compilar autoridades: las contrasta, las cuestiona y, cuando discrepa, lo dice explícitamente. Este patrón es coherente con la tradición historiográfica jesuita del siglo XVI, que privilegiaba la verificación crítica frente a la erudición acrítica.

---

## 6. Referencias

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

*Última actualización: 21 de julio de 2026*
[Repositorio en GitHub](https://github.com/RRCarlos/proyecto-autores)
