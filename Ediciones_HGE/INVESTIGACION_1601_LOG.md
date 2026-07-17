# Bitácora de Investigación: Edición de 1601

## Estado

| Campo | Valor |
|-------|-------|
| **Inicio** | 2026-07-17 |
| **Estado** | ✅ RESUELTA — Fuente 1601 obtenida del investigador |
| **Fase actual** | Completada |

---

## Fase 0 — Inicialización

**Fecha**: 2026-07-17
**Estado**: Completada ✅

- Plan de investigación creado (`PLAN_INVESTIGACION_1601.md`)
- Esta bitácora creada
- Commit `d728edc` push a main

---

## Fase 1 — Oleada 1: Repositorios principales

**Fecha**: 2026-07-17
**Estado**: Completada ✅

### Repositorios consultados

| # | Repositorio | URL | Resultado |
|---|-------------|-----|-----------|
| 1 | BNE (Biblioteca Digital Hispánica) | bdh.bne.es | ❌ NO ENCONTRADA (búsqueda directa falló) |
| 2 | Biblioteca Virtual Miguel de Cervantes | cervantesvirtual.com | ❌ NO ENCONTRADA (ediciones: 1780, 1678, 1794, 1818) |
| 3 | Internet Archive | archive.org | ❌ NO ENCONTRADA (ediciones: 1780, 1794, 1818, 1678) |
| 4 | HathiTrust | hathitrust.org | ❌ NO ENCONTRADA |
| 5 | Gallica (BnF) | gallica.bnf.fr | ❌ NO ENCONTRADA |
| 6 | WorldCat / catálogos | worldcat.org | ❌ NO ENCONTRADA (encontrada 1817-1822, OCLC 8097245) |

**Conclusión**: La edición de 1601 no está en ninguno de los 6 repositorios principales.

---

## Fase 2 — Oleada 2: Búsqueda dirigida + hallazgos críticos

**Fecha**: 2026-07-17
**Estado**: Completada ✅

### CANDIDATOS ENCONTRADOS ⭐

#### Candidato 1: Universidad de Chile (libros.uchile.cl) — ONLINE READING

| Campo | Valor |
|-------|-------|
| **Repositorio** | Universidad de Chile — Libros de Oro |
| **URL Tomo I** | https://libros.uchile.cl/109 |
| **URL Tomo II** | https://libros.uchile.cl/110 |
| **DOI Tomo I** | 10.34720/ng00-yq91 |
| **DOI Tomo II** | 10.34720/8582-y679 |
| **Formato** | FlippingBook (lectura online) |
| **Derechos** | Public Domain |
| **Contenido** | Tomo I: Prólogo + Libros I-XV / Tomo II: Libros XVI-XXX |
| **¿Buen OCR?** | DESCONOCIDO — formato FlippingBook, no se puede descargar PDF directamente |
| **⚠ Verificación de edición** | El TOC incluye "Prólogo de la Real Biblioteca" + "Prólogo del autor". El "Prólogo de la Real Biblioteca" es típico de ediciones 1780+, NO de la primera edición de 1601 (que solo tendría el prólogo propio de Mariana). **Posible que no sea la edición de 1601.** Requiere verificación manual del usuario. |

**Nota**: La Universidad de Chile tiene AMBOS tomos. El formato FlippingBook es lectura online; no se encontró descarga directa de PDF. La edición NO está confirmada como 1601 — la presencia del "Prólogo de la Real Biblioteca" sugiere una edición posterior (1780 o más).

#### Candidato 2: BNE (Biblioteca Nacional de España) — ❌ DESCARTADA (edición 1780, no 1601)

| Campo | Valor |
|-------|-------|
| **Repositorio** | BNE — Biblioteca Digital Hispánica |
| **Catálogo** | datos.bne.es/obra/XX2073435.html |
| **URL proporcionada por usuario** | `http://bnedigital.bne.es/bd/es/card?id=edebc336-e1b8-4628-96d3-fdda261ca9f4` |
| **URL visor (antigua)** | http://bdh-rd.bne.es/viewer.vm?id=0000193802 |
| **Estado visor** | ❌ HTTP 403 — acceso programático bloqueado |
| **Edición real** | **1780** (confirmado por el usuario, que accedió manualmente) |

**Nota (2026-07-17)**: El usuario verificó manualmente y confirmó que la digitalización de BNE Digital corresponde a la edición de 1780 (Ibarra), NO a la de 1601. A pesar de que datos.bne.es enumera una entrada para 1601 (bima0000068832), el contenido digitalizado disponible es la edición posterior. Todos los accesos programáticos devuelven 403.

#### Candidato 3: Biblioteca Cartagena (USal) — TRANSCRIPCIONES + ESCANEADOS

| Campo | Valor |
|-------|-------|
| **Repositorio** | Biblioteca Cartagena — Universidad de Salamanca |
| **URL** | bibliotecacartagena.usal.es |
| **Contenido** | Transcripciones del tomo II + escaneados originales de las páginas |
| **Fuente** | Copia de la BNE (signatura 3/31952) |
| **Páginas disponibles** | Portada, pp. 252-476, colofón (parcial) |

**Nota**: Tiene transcripciones diplomáticas + imágenes facsimilares del tomo II. No es completo (solo pp. 252-476), pero confirma la existencia y legibilidad del original.

### Fuentes académicas consultadas

| Fuente | Referencia clave |
|--------|-----------------|
| Sánchez Torres (2024) | Studia philologica valentina 26, pp. 45-60. DOI: 10.7203/sphv.26.28040 |
| UC3M (s.f.) | Estudio de Libros I-IV. Convención: (I 2) = edición 1601 |
| Brais Ferrás García (2024) | Talia Dixit — confirma diferencias entre ediciones |
| Instituto Juan de Mariana | Resumen histórico de la obra |
| Open Library | Entrada OL43725470M |
| Deutsche Digitale Bibliothek | Ediciones 1592 (latín) y 1605 (Maguncia), NO 1601 |

### Ediciones conocidas de la Historia General (cadena de correcciones)

| # | Año | Lugar | Editor | Notas |
|---|-----|-------|--------|-------|
| 1 | 1601 | Toledo | Pedro Rodríguez | **EDICIÓN OBJETIVO** — Primera edición española |
| 2 | 1605 | Maguncia (Mainz) | Schönwetter | Segunda edición (latín completo, 30 libros) |
| 3 | 1608 | Madrid | Luis Sánchez | Tercera edición — Mariana corregida |
| 4 | 1617 | Madrid | Viuda de Alonso Martín | Cuarta — "corregida y muy aumentada" — +500 correcciones vs 1608 |
| 5 | 1623 | Madrid/Toledo | Luis Sánchez / Diego Rodríguez | Quinta — más completa, incluye falsos cronicones |

**Implicación**: La edición de 1617 NO es sustancialmente igual a la de 1601. El propio Mariana declaró que la de 1617 tenía "exceden de quinientas" correcciones y adiciones respecto a la de 1608 (que a su vez era corregida desde 1601).

---

## Fase 3 — Punto de decisión

**Fecha**: --
**Estado**: PENDIENTE

### Decisión pendiente

¿Qué candidato elegimos para la verificación? Opciones:
1. **U. de Chile** — ambas ediciones disponibles online, formato FlippingBook
2. **BNE** — digitalizada pero visor caído (posible resolver con URL alternativa)
3. **Ambos** — verificar ambos y quedarnos con el mejor

---

## Fase 4A — Verificación de candidato

**Fecha**: --
**Estado**: Pendiente (requiere decisión Fase 3)

---

## Fase 4B — Oleada 2 (extras)

**Fecha**: 2026-07-17
**Estado**: Completada ✅

### Repositorios adicionales consultados

| # | Repositorio | Resultado |
|---|-------------|-----------|
| 1 | Open Library | Entrada encontrada (OL43725470M) — sin descarga directa |
| 2 | Deutsche Digitale Bibliothek | Ediciones 1592 y 1605 — NO 1601 |
| 3 | Instituto Juan de Mariana | Resumen histórico — sin digitalización |
| 4 | UC3M | Estudio académico — referencias a la edición |
| 5 | USal (Biblioteca Cartagena) | ✅ Transcripciones + escaneados parciales |

---

## Fase 5 — Oleada 3: Búsqueda final + descarte

**Fecha**: 2026-07-17
**Estado**: Completada ✅

### Nuevos hallazgos

#### Candidato 4: Biblioteca Foral de Bizkaia (Lau Haizeetara Digital)

| Campo | Valor |
|-------|-------|
| **Repositorio** | Biblioteca Foral de Bizkaia — Lau Haizeetara Digital |
| **Handle** | `liburutegibiltegi.bizkaia.eus/handle/20.500.11938/71883` |
| **Viewer** | `liburutegibiltegi.bizkaia.eus/handle/20.500.11938/71883/viewer/461613` |
| **Contenido** | Solo **Tomo II** — [4]+962+[25] p., Fol. |
| **Imprenta** | Toledo, Pedro Rodríguez, 1601 |
| **Notas físico** | Portada con escudo real; apostillas marginales en la mayoría de las páginas |
| **Derechos** | Public Domain Mark (PDM) |
| **¿Tomo I?** | ❌ NO — el tomo I en Bizkaia es de 1678 (otra edición) |
| **Estado visor** | PDF.js cargado pero documento no se renderizó vía webfetch (puede funcionar en navegador) |

#### Confirmación: Internet Archive NO tiene la edición de 1601

Todas las ediciones de Mariana en Internet Archive son posteriores:

| ID | Año | Editor | Tomo |
|---|---|---|---|
| historiagenerald01mari | 1780 | Ibarra (14ª impresión) | I |
| A212089 | 1678 | García de la Iglesia | I |
| A212090 | 1678 | García de la Iglesia | II |
| A276449 | 1818 | Sabau y Blanco | I |
| historiageneraldes00mari | 1794 | Benito Cano | — |
| historiageneral00migoog | 1839 | F. Oliva (Barcelona) | — |
| ARes71211 | 1592 | Pedro Rodríguez | — (latín original) |

#### Descartes definitivos

| Candidato | Razón de descarte |
|---|---|
| cristoraul.org (7 tomos PDF) | Edición de **1780 Ibarra** ("DECIMACUARTA IMPRESIÓN"), no 1601 |
| clasicoshistoria.blogspot.com | Transcripción basada en 1780 |
| Cervantes Virtual (enlaces múltiples) | Ediciones 1678, 1780, 1794 — ninguna es 1601 |
| Deutsche Digitale Bibliothek | Solo tiene 1592 (latín) y 1605 (Maguncia) |

### Tabla consolidada de candidatos (post-Oleada 3 + correcciones)

| # | Candidato | Edición real | Tomo I | Formato | Acceso programático | Estado |
|---|---|---|---|---|---|---|
| 1 | **U. de Chile** | ⚠ No confirmada (¿1780+?) | Posible | FlippingBook | Lectura online | Requiere verificación manual |
| 2 | **BNE Digital** | ❌ **1780** | — | PDF imagen | 403 | **DESCARTADA** |
| 3 | **Bizkaia** | ✅ 1601 | ❌ Solo tomo II | PDF viewer | Public Domain | Irrelevante (sin tomo I) |
| 4 | **Cartagena (USal)** | ✅ 1601 | ❌ Solo tomo II parcial | Transcripción | Online | Irrelevante (sin tomo I) |

---

## Análisis: Dificultad de acceso a la edición de 1601 con OCR fiable

### Resumen del problema

Tras consultar **más de 10 repositorios digitales** (BNE, Internet Archive, Cervantes Virtual, HathiTrust, Gallica, WorldCat, U. de Chile, Bizkaia, Cartagena/USal, Open Library, Deutsche Digitale Bibliothek, cristoraul.org), **ninguno ofrece el tomo I de la edición de 1601 con OCR procesable por IA**. Las razones se detallan a continuación.

### ¿Qué es el OCR?

**OCR** (*Optical Character Recognition* / Reconocimiento Óptico de Caracteres) es la tecnología que convierte imágenes escaneadas de documentos en texto digital searchable. Cuando una biblioteca digitaliza un libro antiguo, obtiene páginas en imagen (JPEG/TIFF). El OCR intenta "leer" esa imagen y producir un archivo de texto (.txt o searchable PDF).

La calidad del OCR depende de:
1. **Calidad del escaneo** (resolución, iluminación, alineación)
2. **Estado físico del original** (tinta desvanecida, manchas, bleed-through, anotaciones manuscritas)
3. **Tipo de letra** (letras góticas/rotondas del siglo XVI son mucho más difíciles que tipografías modernas)
4. **Motor OCR utilizado** (ABBYY FineReader, Tesseract, etc. — varía enormemente en calidad para textos antiguos)
5. **Post-procesamiento** (corrección humana o automática del texto resultante)

### ¿Por qué las digitalizaciones de la edición de 1601 son tan malas para IA?

El problema es triple:

#### 1. Escaneados como imagen, no como texto
La mayoría de repositorios (especialmente la BNE) digitalizan en **imagen pura** (PDF con páginas escaneadas, sin capa de texto OCR). El resultado es un PDF que un humano puede leer visualmente, pero que una IA (o cualquier software) no puede procesar como texto. El usuario puede leerlo sin problemas en un visor; la IA no puede extraer ni buscar en él.

**Repositorios afectados**: BNE Digital (1780), Bizkaia, Internet Archive (ediciones posteriores).

#### 2. OCR motor genérico sin afinamiento para tipografía del siglo XVI
Cuando sí se aplica OCR (ej. Tesseract en Internet Archive), el motor está configurado para textos modernos. La edición de 1601 usa:
- **Tipografía romanista** (corte de.Types de.Types de.Types — variante del romano renacentista español)
- **Ligaduras** frecuentes (ſt, ct, st, fi, fl)
- **Abreviaturas manuscritas** en márgenes (apostillas)
- **Sangría tipográfica** y formato de dos columnas en algunos pasajes
- **Letra initial** decorativa al inicio de capítulos
- **Erratas** y variantes ortográficas propias de la imprenta del XVI

El OCR produce texto con errores sustanciales: confusión de s/ſ, ligaduras rotas, números incorrectos, palabras inventadas. Un OCR típico para esta época tiene un **error rate del 15-30%** en Tesseract y **5-15%** en ABBYY FineReader, lo que lo hace inutilizable para análisis textual sin corrección manual extensa.

#### 3. La edición de 1601 es escasa y no fue priorizada para digitalización
La edición de 1601 (Toledo, Pedro Rodríguez) es la **primera edición en castellano** pero no fue la más reimpresa. Las ediciones más comunes en bibliotecas son la de 1780 (Ibarra, con 14+ impresiones) y la de 1839. Esto significa:
- **Pocos ejemplares** sobrevivientes → menor prioridad para digitalización
- **Deterioro físico** mayor (425+ años) → peor estado para escaneo
- Las bibliotecas digitalizan primero los ejemplares en mejor estado → ediciones posteriores
- Los catálogos bibliográficos confunden ediciones → una digitalización etiquetada como "1601" puede ser realmente de 1780

### Impacto en este proyecto

El TFG analiza 180 citas del tomo I (Libros I–IV). Para verificarlas contra la edición de 1601 se necesita:
1. **Texto legible** del tomo I de 1601
2. Con capacidad de **búsqueda por palabra/página** (no solo lectura visual)

| Fuente | ¿Texto buscable? | ¿Edición 1601? | ¿Accesible? |
|---|---|---|---|
| U. de Chile | FlippingBook (sin descarga) | No confirmado (¿1780+?) | Lectura online |
| BNE Digital | Imagen (sin OCR procesable) | ❌ Edición 1780 | 403 programático |
| Bizkaia | PDF viewer | ✅ Pero solo tomo II | Viewer (puede funcionar en navegador) |
| Cartagena/USal | Transcripción diplomática | ✅ Pero solo tomo II parcial | Online |
| Copia física del usuario | Sí (lectura directa) | Puede que sí | Presencial |

### Conclusión

La edición de 1601 es un caso donde **la brecha digital afecta directamente la investigación académica**. La rareza bibliográfica, el estado de conservación de los ejemplares, y las limitaciones de los motores OCR para tipografía del XVI conspiran para que, a día de hoy, **no exista una versión digitalizada del tomo I con texto procesable por IA**. Las digitalizaciones existentes son o bien imagen pura (inútil para IA), o bien etiquetadas erróneamente (1780 tomada por 1601).

---

## ⚠ Obstacle: El castellano del siglo XVI como barrera de procesamiento

### El problema

Trabajamos con un texto impreso en **1601**. El castellano de esa época difiere sustancialmente del español moderno. Esto afecta tanto al procesamiento automático (IA) como a la interpretación humana, y debe considerarse un **obstáculo estructural** del proyecto, no un detalle menor.

### Diferencias lingüísticas relevantes

#### 1. Ortografía
| Rasgo | Ejemplo 1601 | Equivalente moderno |
|-------|-------------|-------------------|
| **ſ (s larga)** | *ſer* / *caſa* | *ser* / *casa* — el OCR e IA pueden confundirla con 'f' |
| **u/v intercambiables** | *vn*, *Valor*, *dvn* | *un*, *Valor*, *de uno* — la 'v' y la 'u' eran el mismo carácter |
| **i/j intercambiables** | *Iuan*, *haze* | *Juan*, *hace* |
| **x = j moderno** | *Mexico*, *exprado* | *Méjico*, *esperado* |
| **q con cifra** | `q3` = *que*, `q9` = *quan* | Abreviaturas de imprenta, opacas para IA |
| **Tildes irregulares** | Uso de tilde para abreviar nasal (ã en lugar de an/am) | *ãtro* = *ántro* / *antrO* |

#### 2. Léxico y semántica
- Palabras caídas en desuso: *acaeçer* (suceder), *assí* (así), *fablar* (hablar), *omne* (hombre)
- Sentidos semánticos cambiantes: *tratar* (enfrentar), *efecto* (resultado, no "efecto secundario"), *calidad* (naturaleza, no "cualidad")
- Latinismos y cultismos frecuentes en Mariana: *exordium*, *narratio*, *digressio* — propios del estilo historiográfico jesuítico

#### 3. Sintaxis
- Períodos muy largos con subordinadas encadenadas (estilo historiográfico del XVI)
- Uso del subjuntivo y condicional con valores que hoy suenan arcaicos
- Construcciones con *hazer que + infinitivo* (causativas) en lugar de perifrasis modernas

#### 4. Imprenta del XVI
- **Erratas tipográficas** propias de la composición manual (el propio Mariana las enumera en el colofón de erratas)
- **Ligaduras** impresas: *ſt*, *ct*, *st*, *fi*, *fl* — un solo bloque de plomo
- **Letras capitulares** decorativas que el OCR no reconoce
- **Apostillas manuscritas** en márgenes (correcciones manuales del impresor o del autor)

### Impacto en la verificación de citas del TFG

El TFG contiene 180 citas del tomo I (Libros I–IV). Al verificarlas contra la edición de 1601:

1. **Búsqueda textual**: Una cita modernizada (*"porque los romanos..."*) no coincidirá textualmente con el original (*"porque los Romanos..."* o *"porq̃ los Romanos..."*). Se requiere una estrategia de **normalización ortográfica** antes de la comparación.

2. **Interpretación de la IA**: Las herramientas de IA (como esta) pueden malinterpretar sintaxis arcaica, confundir abreviaturas, o producir traducciones/paráfrasis inexactas. **No se debe confiar ciegamente en la traducción automática del castellano del XVI.**

3. **Fallo de búsqueda por coincidencia exacta**: Cualquier script o herramienta de verificación automática que use búsqueda literal (*string matching*) fallará con el texto de 1601 por las diferencias ortográficas. Se necesita normalización previa o búsqueda difusa.

### Implicación para el trabajo con IA

> **⚠ LIMITACIÓN CONOCIDA**: La capacidad de esta IA para procesar fielmente el castellano del siglo XVI tiene un techo. Los procesos de verificación de citas deben incluir **revisión humana** del usuario en cada paso crítico. La IA puede asistir en la localización y comparación aproximada, pero **la última palabra sobre la correspondencia exacta entre una cita del TFG y el texto de 1601 debe ser del investigador humano**.

### Mitigación propuesta

1. **Normalización ortográfica previa**: Antes de comparar, aplicar reglas de conversión (*ſ→s*, *v→u* donde corresponda, *x→j*, etc.) tanto al texto OCR de 1601 como a las citas del TFG.
2. **Búsqueda difusa**: Usar algoritmos de similitud (Levenshtein, fuzzy matching) en lugar de coincidencia exacta.
3. **Glosario de equivalencias**: Construir un diccionario *ad hoc* de palabras del XVI → su equivalente moderno para acelerar la interpretación.
4. **Revisión humana obligatoria**: Cada cita verificada debe pasar por validación del usuario antes de incluirse en el TFG.

---

## Fase 3 — Punto de decisión

**Fecha**: 2026-07-17
**Estado**: ◀ EN CURSO — Se requiere decisión del usuario

### Decisión pendiente

¿Qué candidato elegimos como referencia textual para verificar 180 citas?

> **Nota**: La BNE Digital ha sido descartada (edición 1780, no 1601). La U. de Chile NO tiene la edición confirmada como 1601 (posible 1780+ por el "Prólogo de la Real Biblioteca"). Las opciones se reducen.

**Opción A** — **Esperar a que el usuario localice la edición de 1601 manualmente**. El usuario ha indicado que buscará la fuente. Si la encuentra, se procede a verificación.

**Opción B** — **Usar la edición de 1617 como base** (ya disponible: `mariana_1617_tomo_primero_ocr.txt`). Limitación conocida: 500+ correcciones respecto a 1601 (Mariana declaró este dato). Aceptable para una primera pasada de verificación, con la salvedad explícita en el TFG.

**Opción C** — **Híbrida**: Verificación inicial con 1617 + anotar las diferencias que se detecten como "requiere consulta de edición 1601 en formato físico". Esta es la opción más pragmática si no se encuentra la 1601 digital.

---

## Fase 6 — Fuente 1601 obtenida ✅

**Fecha**: 2026-07-17
**Estado**: Completada ✅

### Resolución

El investigador descargó manualmente el TXT de la edición de 1601 desde la plataforma BNE Digital (`bnedigital.bne.es`). Aunque el acceso programático devolvía 403, el usuario pudo acceder a través del navegador y descargar el archivo de texto completo.

| Campo | Valor |
|-------|-------|
| **Archivo** | `Ediciones_HGE/HGE_TomosI-II.txt` |
| **Edición** | 1601, Toledo, Pedro Rodríguez — confirmado por portada OCR |
| **Contenido** | Tomo I + Tomo II completos |
| **Tamaño** | ~5.8 MB, 98.805 líneas |
| **Tomo I** | Líneas 1–48.770 (Libros I–XV + prólogo + erratas) |
| **Tomo II** | Líneas 48.774–98.805 (Libros XVI–XXX) |
| **Libros I–IV** | Libro Primero: línea 255 / Libro Segundo: 3.099 / Libro Tercero: 6.227 / Libro Cuarto: 9.105 |
| **Calidad OCR** | Legible con artefactos típicos del XVI (ſ→f, EJpaña, u/v, ligaduras) |

### Verificación realizada

Se inspeccionaron muestras del texto en las líneas clave:
- Portada (líneas 1–30): Confirma "EN TOLEDO, Por Pedro Rodriguez" + "TOMO PRIMERO"
- Libro I, cap. XXX (línea 1.500): Texto legible, narración sobre Siculorey y Tito
- Libro II, cap. I (línea 4.500): Texto legible, guerra contra Aníbal
- Libro III, cap. XXVII (línea 7.500): Texto legible, Cicerón y los Cimbros

**Conclusión**: El archivo es procesable. Los artefactos OCR son consistentes y predecibles (ver sección de análisis OCR y obstáculo lingüístico más arriba). Con normalización ortográfica previa, es apto para verificación automatizada de citas.

### Decisión resuelta

Se adopta la **Opción A** (fuente 1601 como base primaria) con la edición de 1617 como testigo auxiliar de contraste. Las 180 citas se verificarán contra el TXT de 1601 (`HGE_TomosI-II.txt`), no contra el OCR de 1617.

### Pendiente

- Normalización ortográfica del TXT de 1601 para búsqueda automatizada
- Verificación de las 180 citas contra la edición original

---

## Fase 7 — Confirmación definitiva y cambio de plan

**Fecha**: 2026-07-17
**Estado**: Completada ✅

### Confirmación de legibilidad

Se re-verificó el TXT de 1601 (`HGE_TomosI-II.txt`) en los cuatro puntos de Libros I–IV:

| Libro | Línea | Contenido | Legible |
|-------|-------|-----------|---------|
| Libro I | 255 | Inicio: "LIBRO PRIMER O; DE LA HISTORIA de Efpaña" + caps I–III | ✅ |
| Libro II | 3099 | Inicio: "LIBRO SEGVNDO. CAP. I. Que Hannony fus hermanos..." | ✅ |
| Libro III | 6227 | Inicio: "LIBRO TERCERO. CAP. I. elprincipio idaguerra de ISLnmancia" | ✅ |
| Libro IV | 9105 | Inicio: "LIBRO QVARTO. CAP. I. (De U tenida delhjo de (Diosalmundo" | ✅ |

**Conclusión**: El TXT de 1601 es legible y procesable. La edición de 1601 queda confirmada como fuente primaria.

### Decisión: eliminación de la edición de 1617

Con la edición de 1601 confirmada y operativa, la edición de 1617 deja de ser necesaria. Se procederá a eliminar los siguientes archivos en la próxima sesión:

| Archivo | Motivo de eliminación |
|---------|----------------------|
| `mariana_1617_tomo_primero_ocr.txt` | Ya no es fuente primaria; la 1601 la reemplaza |
| `mariana_1617_tomo_primero_page_numbers.json` | Mapeo de páginas del OCR 1617, sin uso con 1601 |
| `EDICION_1617_USO.md` | Ficha técnica de la 1617, ya no relevante |

**Nota**: Los archivos se mantienen temporalmente en el repo hasta que se confirme que no hay referencias cruzadas que dependan de ellos.

### Decisión: revisión del Plan de Separación OCR

El plan de separación OCR (`PLAN_SEPARACION_OCR.md`) fue diseñado para la edición de 1617, donde los Libros I–IV ocupaban las páginas 43–234 del PDF. Con la edición de 1601:

- **Los límites de página NO corresponden**: el TXT de 1601 tiene una estructura diferente (líneas 255–48.770 para el tomo I completo)
- **Los marcadores de libro sí se localizan**: "LIBRO PRIMER O" (línea 255), "LIBRO SEGVNDO" (3099), "LIBRO TERCERO" (6227), "LIBRO QVARTO" (9105)
- **El plan debe rehacerse** para trabajar con el TXT de 1601 en vez del PDF de 1617

Se documenta aquí que el plan de separación queda **PENDIENTE DE REVISIÓN** para la próxima sesión.

### Implicaciones para la Fase 2

La Fase 2 del proyecto (verificación de 180 citas) ahora tiene claridad total:

1. **Fuente**: `HGE_TomosI-II.txt` (edición de 1601,TXT de BNE Digital)
2. **Archivos a eliminar**: Los de la edición de 1617 (próxima sesión)
3. **Plan a revisar**: `PLAN_SEPARACION_OCR.md` (diseñado para 1617, no aplicable a 1601)
4. **Siguiente paso**: Normalización ortográfica del TXT de 1601
- Revisión humana de cada cita verificada
