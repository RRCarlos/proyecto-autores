# TFG Juan de Mariana — Análisis Historiográfico de las Fuentes de la *Historia General de España* (Libros I–IV, 1601)

> **Trabajo de Fin de Grado** | Curso de Inteligencia Artificial  
> Análisis de las fuentes historiográficas utilizadas por Juan de Mariana (1536–1624) en los cuatro primeros libros de su *Historia General de España*.

---

## Resumen

Este repositorio contiene el proceso completo de investigación del TFG, que responde a la pregunta:

> **¿Para qué usa Juan de Mariana a cada autor que cita en su *Historia General de España*?**

El estudio va más allá de un mero recuento de fuentes: analiza la **función historiográfica** de cada autor dentro del discurso histórico de Mariana. No se trata solo de saber *si* existían las obras, sino de entender *cómo* y *para qué* las utiliza.

### Resultados principales

| Indicador | Dato |
|-----------|------|
| **Autores únicos** identificados en L. I–IV | 68 |
| **Citas** extraídas y clasificadas | **180** |
| **Localizadas** en la edición de 1617 mediante OCR automatizado | **113 (62.8%)** |
| **Obras explícitas** (autor + obra nombrados en el mismo pasaje) | **18** |
| **Autores con edición pre-1592 verificada** | **58 (85.3%)** |
| **Falsificaciones detectadas** | 1 (Falso Beroso / Annio de Viterbo) |
| **Obras perdidas** | 2 (Filisto, Quinto Fabio Píctor) |

---

## Pregunta de investigación

La investigación parte de una pregunta inicial:

> *¿Realmente tuvo Juan de Mariana acceso a las obras que cita?*

Esta pregunta se descompone en cuatro niveles de evidencia:

1. **¿Existieron** los autores que cita?
2. **¿Tenían ediciones impresas** antes de 1592?
3. **¿Se conservan ejemplares** en las bibliotecas jesuitas de Toledo?
4. **¿Tienen esos ejemplares marcas de propiedad jesuita?**

Tras la reorientación metodológica, el eje central pasó a ser:

> **¿Qué función cumple cada autor citado dentro del relato histórico de Mariana?**

Esto permite analizar las citas como parte de la **construcción historiográfica**: autoridad clásica, apoyo cronológico, tradición bíblica, legitimación de episodios, etc.

---

## ¿Por qué es importante este estudio?

La *Historia General de España* de Juan de Mariana fue la obra de referencia sobre la historia de España durante más de dos siglos (1592–1850). Entender de dónde sacaba Mariana su información —y **para qué** usaba cada fuente— es clave para:

- Evaluar la **fiabilidad historiográfica** de la obra
- Distinguir entre fuentes clásicas que leyó directamente, tradiciones medievales que heredó, y falsificaciones que incorporó sin saberlo
- Comprender cómo funcionaba la **erudición humanista** del Siglo de Oro español
- Trazar la **transmisión del conocimiento** desde la Antigüedad hasta el siglo XVII

La pregunta "¿tuvo acceso?" puede parecer sencilla, pero implica desenredar la maraña de ediciones, manuscritos, compilaciones, fragmentos, falsificaciones y tradiciones orales que mediaban entre un autor clásico del siglo I a.C. y un jesuita del XVI leyendo en Toledo.

---

## El enfoque: función historiográfica

Este TFG no se limita a un recuento de autores. Propone una **tipología funcional de las citas**:

| Función | ¿Para qué usa Mariana al autor? | Ejemplo |
|---------|--------------------------------|---------|
| **Autoridad geográfica** | Describir territorios, límites, ciudades, ríos | Plinio, Ptolomeo, Estrabón |
| **Autoridad narrativa** | Apoyar el relato de guerras y conquistas | Tito Livio, Polibio, Apiano |
| **Cronología** | Fijar fechas y ordenar acontecimientos | Eusebio de Cesarea, Justino |
| **Orígenes y genealogía** | Explicar linajes, fundadores, mitos de origen | Diodoro Sículo, San Isidoro |
| **Tradición bíblica** | Conectar la historia de España con el marco bíblico | Flavio Josefo |
| **Crítica o contraste** | Señalar discrepancias entre fuentes | Cicerón, Nebrija |
| **Fuente problemática** | Citar con reservas o desacreditar | Falso Beroso, Andrea de' Bardi |

Esta clasificación permite ver **patrones**: Mariana usa sistemáticamente a Plinio para geografía, a Tito Livio para narración bélica, a Justino como epitomista de confianza. Cuando entra en materia mítica o dudosa, despliega múltiples autores en contraste, mostrando su escepticismo humanista.

---

## Estructura del repositorio

```
TFG_JUAN_DE_MARIANA/
├── README.md                    ← Este documento
├── .gitignore
├── requirements.txt             ← Dependencias Python (openpyxl)
│
├── docs/                        ← Documentación académica
│   ├── MEMORIA.md               ← Memoria completa del proyecto
│   └── PLAN_REORIENTACION_METODOLOGICA.md  ← Nueva metodología (2026-05-18)
│
├── data/                        ← Tablas de investigación (CSV + XLSX + MD)
│   ├── tabla_base.*             ← 180 citas extraídas de notas Word
│   ├── validacion_1617.*        ← Localización automatizada contra OCR
│   ├── validacion_por_lotes.*   ← Validación completa con fragmentos OCR
│   └── obras_explicitas.*       ← 18 obras donde Mariana nombra autor + obra
│
├── scripts/                     ← Procesamiento y validación
│   ├── build_citation_use_table.py      ← Extrae citas del docx Word
│   ├── validate_table_against_1617.py   ← Valida contra OCR 1617
│   ├── apply_explicit_works_phase1.py   ← Fase 1: obras explícitas Libro I
│   ├── apply_explicit_works_phase2_complete.py ← Fase 2: obras explícitas I–IV
│   ├── export_validation_table_md.py    ← Exporta validación a Markdown
│   └── summary_phase2.py               ← Resumen de obras explícitas
│
└── sources/                     ← Fuentes digitalizadas
    ├── mariana_1617_tomo_primero_ocr.txt         ← OCR completo (96K líneas)
    └── mariana_1617_tomo_primero_page_numbers.json
```

---

## Metodología

### Fases de la investigación

| Fase | Descripción | Estado |
|------|-------------|--------|
| **1–2** | Extracción de autores desde notas Word de la edición 1601 | ✅ |
| **3–4** | Verificación en 6 catálogos internacionales | ✅ |
| **5** | Verificación de ediciones pre-1592 (85.3% verificadas) | ✅ |
| **6** | Localización en Biblioteca de Castilla-La Mancha (fondos jesuitas) | ✅ |
| **7** | OCR de la edición 1617 + validación automatizada | ✅ |
| **8** | Identificación de obras explícitas (autor + obra en mismo pasaje) | ✅ |
| **9** | Reorientación metodológica (nuevo eje: función historiográfica) | ✅ |
| **10** | Transcripción verificada de fragmentos | 🔲 |
| **11** | Análisis historiográfico por función de cita | 🔲 |

### Ediciones de referencia

| Edición | Año | Uso |
|---------|-----|-----|
| *Historia General de España* (castellano) | **1601** | Texto base de referencia. BNE, tomo primero |
| *Historia General de España* (latín, ampliada) | **1617** | Testigo auxiliar para búsqueda OCR |

---

## El papel de la inteligencia artificial en la investigación

Este TFG se ha desarrollado íntegramente con la asistencia de **agentes de inteligencia artificial**, integrados en el flujo de trabajo a través de **OpenCode** (entorno de desarrollo asistido por IA). Aquí se explica cómo se ha utilizado la IA y por qué es relevante para un trabajo de historiografía.

### ¿Qué se usó?

| Herramienta / Agente | Función en el proyecto |
|----------------------|------------------------|
| **Claude (Anthropic)** como agente de IA | Orquestación de toda la investigación: leer, buscar, analizar, escribir scripts, generar tablas, redactar documentos |
| **OpenCode** | Entorno de trabajo que permite al agente IA ejecutar código, acceder al sistema de archivos, navegar por la web y usar GitHub |
| **Python 3.10+** | Scripts de procesamiento: extracción de citas (openpyxl), validación contra OCR, exportación a Markdown |
| **OCR de Internet Archive** | Digitalización de la edición 1617 (~3.8 MB de texto OCR, 96.000 líneas) |
| **Catálogos web** | VIAF, USTC, GW, BNE, CCPB, Biblioteca CLM (consultados directamente por el agente IA vía web) |

### ¿Cómo funcionó el proceso con IA?

#### 1. Extracción de autores y citas (fases 1–2)

El investigador (Carlos) leyó los Libros I–IV de la edición de 1601 y tomó notas en un documento Word. Ese documento contenía 180 referencias a autores con contexto, capítulo, y observaciones preliminares.

**Intervención de la IA**: Un script Python (`build_citation_use_table.py`) procesó el documento Word extrayendo cada mención y estructurándola en una tabla con campos: libro, capítulo, autor citado, pasaje, función de la cita, tipo de fuente y observaciones. El agente de IA escribió este script, lo ejecutó, y generó la tabla base en formato `.xlsx` y `.csv`.

#### 2. Verificación en catálogos internacionales (fases 3–5)

Cada uno de los **68 autores** identificados fue verificado contra seis bases de datos para confirmar:

- **VIAF** (Virtual International Authority File): existencia y forma normalizada del nombre
- **USTC** (Universal Short Title Catalogue): ediciones europeas anteriores a 1600
- **GW** (Gesamtkatalog der Wiegendrucke): incunables (1450–1500)
- **BNE** (Biblioteca Nacional de España): ejemplares en bibliotecas españolas
- **CCPB** (Catálogo Colectivo del Patrimonio Bibliográfico): fondo patrimonial español
- **Biblioteca de Castilla-La Mancha**: fondos del Colegio de Jesuitas de Toledo

**Intervención de la IA**: El agente realizó **búsquedas web automatizadas** contra cada catálogo, consultando uno por uno los 68 autores. Para cada autor, el agente:
1. Buscaba su ID VIAF y ficha de autoridad
2. Consultaba el USTC para verificar ediciones pre-1592
3. Buscaba en los catálogos españoles ejemplares conservados
4. Documentaba cada hallazgo en la tabla con su fuente y enlace

Este proceso, que manualmente habría llevado semanas, se completó en horas gracias a la capacidad del agente de realizar **búsquedas paralelas y sistemáticas**.

#### 3. OCR y validación automatizada (fases 7–8)

Se descargó de Internet Archive la edición de 1617 (tomo primero) y se ejecutó un OCR completo, generando un archivo de texto de **3.8 MB** con aproximadamente **96.000 líneas**.

**Intervención de la IA**: El agente escribió y ejecutó el script `validate_table_against_1617.py`, que:

1. Segmenta el OCR por libros usando los títulos de capítulo como marcadores
2. Para cada una de las 180 citas, busca el nombre del autor en la zona del libro correspondiente
3. Extrae el **fragmento candidato** (contexto OCR) donde aparece el nombre
4. Marca cada cita como "Confirmado en 1617", "No localizado" o "Localizado en el libro"
5. Genera automáticamente los archivos de validación en `data/validacion_por_lotes.*`

**Resultado**: 113 de 180 citas (62.8%) fueron localizadas automáticamente en la edición de 1617.

#### 4. Identificación de obras explícitas (fase 9)

El agente aplicó un segundo script (`apply_explicit_works_phase2_complete.py`) que examinaba cada fragmento OCR validado para determinar si Mariana **nombraba la obra** además del autor en el mismo pasaje. Esto requiere un análisis semántico: no basta con que aparezca "Plinio", tiene que aparecer "Plinio, al fin de su historia natural".

**Intervención de la IA**: El agente analizó cada fragmento candidato y aplicó criterios conservadores:
- Solo se marca como "obra explícita" si autor + obra aparecen en el mismo pasaje del OCR
- Las identificaciones dudosas se dejan sin asignar
- Cada entrada incluye la evidencia textual (líneas del OCR donde aparece)

**Resultado**: 18 obras explícitas identificadas en los Libros I–IV.

#### 5. Reorientación metodológica y análisis

A mitad del proceso, el equipo (Carlos + agente IA) se reunió con un experto en historiografía que recomendó cambiar el enfoque: pasar de "¿tuvo acceso?" (difícil de probar sin evidencia material directa) a "¿para qué usa cada autor?" (analizable desde el texto mismo).

**Intervención de la IA**: El agente documentó esta decisión en `PLAN_REORIENTACION_METODOLOGICA.md` y reclasificó las 180 citas por **función historiográfica**, no solo por existencia.

### ¿Qué NO hizo la IA?

Es importante dejar claro los límites:

1. **La lectura de la obra original** la hizo Carlos, no la IA. El agente trabajó sobre las notas que él tomó.
2. **La verificación en Biblioteca de Castilla-La Mancha** requiere visita presencial para comprobar exlibris jesuitas. La IA solo pudo consultar los catálogos digitales.
3. **El criterio historiográfico** (clasificar por función de cita) lo define Carlos con ayuda del experto. La IA ejecuta la clasificación, pero no sustituye el juicio académico.
4. **La transcripción verificada de fragmentos** (fase 10) requiere cotejar el OCR contra el facsímil real, algo que debe hacer el investigador.

La IA actuó como **asistente de investigación**: ejecutó búsquedas sistemáticas, procesó grandes volúmenes de texto, generó tablas estructuradas, y liberó al investigador para centrarse en el análisis crítico y la interpretación.

---

## Sobre la verificación con fuentes académicas

Uno de los temores habituales con la IA es que "invente" referencias o datos (las conocidas alucinaciones). Para mitigarlo, se siguieron estos principios:

1. **Trazabilidad**: cada autor verificado tiene su ID VIAF documentado. Cualquier lector puede comprobar que el autor existe y que las ediciones citadas son reales.
2. **Fuentes primarias**: el OCR de la edición 1617 es una fuente digitalizada real, descargada de Internet Archive. Los fragmentos citados en las tablas de validación son literales del OCR (aunque el OCR del siglo XVII tiene errores de reconocimiento).
3. **Criterio conservador**: en la identificación de obras explícitas, solo se asignó "obra asociada" cuando el OCR mostraba claramente autor + obra en el mismo pasaje. Las dudas se dejaron sin asignar.
4. **Contraste manual pendiente**: toda la validación automatizada está marcada como "Pendiente de verificación visual" hasta que se coteje con el facsímil real.
5. **El investigador decide**: la IA propone clasificaciones y detecta patrones, pero la interpretación historiográfica final es de Carlos.

Este enfoque —IA como **herramienta de procesamiento y búsqueda** combinada con **juicio humano** en cada paso— es la clave metodológica del proyecto.

---

## Hallazgos clave

### Autores con status especial

| Categoría | Autores | Implicación |
|-----------|---------|-------------|
| **Falsificación** | Falso Beroso (Annio de Viterbo) | Mariana utiliza una obra forjada en 1498, no fuentes antiguas genuinas |
| **Obra perdida** | Filisto, Quinto Fabio Píctor | Solo fragmentos conservados; Mariana cita a través de tradición indirecta |
| **Principalmente manuscritos** | Moro Rasis, Miguel Sincelo, Braulio, San Ildefonso | Sin edición impresa verificada antes de 1592 |
| **Autoría dudosa** | Julio Capitolino, Trebellio Polión (Historia Augusta), Andrea de' Bardi | Atribuciones cuestionadas por la crítica textual |

### Vías de transmisión

1. **Ediciones impresas** (~70%): Desde 1450, producción masiva de clásicos
2. **Compilaciones medievales** (~20%): Isidoro, Beda preservan fragmentos
3. **Manuscritos** (~10%): Obras menores o fragmentos específicos

### Incunables más antiguos localizados

| Autor | Obra | Año |
|-------|------|-----|
| San Jerónimo | Vulgata | 1456 |
| Cicerón | Opera | 1465 |
| Virgilio | Opera | 1469 |
| Tito Livio | Ab Urbe Condita | 1470 |
| Plutarco | Vidas Paralelas | 1470 |

---

## Cómo usar este repositorio

```bash
# Clonar
git clone https://github.com/RRCarlos/TFG_JUAN_DE_MARIANA.git
cd TFG_JUAN_DE_MARIANA

# Instalar dependencias
pip install -r requirements.txt

# Regenerar tabla base desde el Word original
python scripts/build_citation_use_table.py

# Validar contra OCR 1617
python scripts/validate_table_against_1617.py

# Identificar obras explícitas
python scripts/apply_explicit_works_phase2_complete.py
```

> **Nota**: El script `build_citation_use_table.py` requiere el archivo Word original (`Historia general de España.docx`) que no está incluido en el repositorio por derechos de autor. Las tablas pregeneradas en `data/` contienen el resultado completo del análisis.

---

## Estado del proyecto

| Fase | Estado |
|------|--------|
| Extracción y verificación de fuentes | ✅ Completo |
| OCR y validación automatizada | ✅ Completo |
| Identificación de obras explícitas | ✅ Completo |
| Reorientación metodológica | ✅ Completo |
| Transcripción verificada de fragmentos | 🔲 Pendiente |
| Análisis historiográfico completo | 🔲 Pendiente |
| Redacción de conclusiones | 🔲 Pendiente |

---

## Referencias

### Catálogos internacionales
- [VIAF](https://viaf.org) — Authority files internacionales
- [USTC](https://ustc.ac.uk) — Ediciones europeas pre-1600
- [GW](https://gesamtkatalogderwiegendrucke.de) — Incunables (1450–1500)

### Bibliotecas españolas
- [BNE](https://www.bne.es) — Biblioteca Nacional de España
- [CCPB](https://bvpb.mcu.es) — Catálogo Colectivo del Patrimonio Bibliográfico Español
- [Biblioteca CLM](https://patrimoniodigital.castillalamancha.es) — Fondo del Colegio de Jesuitas de Toledo

### Bibliotecas digitales
- [Gallica](https://gallica.bnf.fr) — Bibliothèque nationale de France
- [Biblioteca Virtual Miguel de Cervantes](https://www.cervantesvirtual.com)

### Referencias académicas
- Cirot, G. *Mariana historien: études sur l'historiographie espagnole*. Burdeos: Feret & Fils, 1905.

---

## Licencia

El contenido académico y los datos de investigación son de acceso abierto.  
Los scripts están disponibles bajo licencia MIT.

---

**TFG Juan de Mariana** — Mayo 2026  
[Repositorio](https://github.com/RRCarlos/TFG_JUAN_DE_MARIANA)
