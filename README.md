# Proyecto Autores — Historia General de España

> Análisis historiográfico de las fuentes de la *Historia General de España* de Juan de Mariana (1536–1624).
> Estado documental de la tabla principal actualizado el 25 de septiembre de 2026.

## 1. Objeto del proyecto

La *Historia General de España*, publicada en Toledo en 1601, es la primera traducción al castellano de la obra de Mariana. Este proyecto identifica y clasifica las autoridades historiográficas que aparecen en sus cinco primeros libros, desde los orígenes míticos de Hispania hasta el reino visigodo.

La pregunta que guía el análisis es:

> **¿Para qué cita Mariana a cada autor?**

El objetivo no es demostrar el acceso directo de Mariana a cada obra, sino describir la función historiográfica de cada mención: fundamentar, contrastar, desacreditar, corregir o remitir a otra tradición documental.

## 2. Estado actual

La tabla principal está completa para los Libros I–V y contiene **324 entradas de autor y capítulo** con numeración global continua.

| Libro | Entradas | Numeración global |
|---|---:|---:|
| Primero | 82 | 1–82 |
| Segundo | 35 | 83–117 |
| Tercero | 53 | 118–170 |
| Cuarto | 81 | 171–251 |
| Quinto | 73 | 252–324 |
| **Total** | **324** | **1–324** |

La columna `Autor` contiene 137 etiquetas textuales distintas. Esta cifra no equivale al número de autores únicos: aún existen variantes como `Plinio` / `Plinio el Viejo`, `Ptolomeo` / `Claudio Ptolomeo` o `Dion` / `Dion Casio`.

Los documentos de apoyo mantienen un alcance menor: los apuntes y `Tablas/Capítulos sin citas.md` corresponden a los Libros I–IV, mientras que `Análisis de datos/Autores y obras.md` es un extracto auxiliar no exhaustivo de 20 entradas de esos mismos libros. Solo la tabla principal debe usarse para recalcular el total vigente I–V.

## 3. Criterio de inclusión

Una entrada se incluye cuando Mariana utiliza a una autoridad como fuente, testimonio o argumento identificable.

- Se incluyen las cartas o epístolas cuyo contenido se cita, resume o utiliza.
- Se excluyen las cartas mencionadas solo como existentes.
- Se excluyen las menciones nominales de personajes sin uso historiográfico.
- Se excluyen las referencias colectivas sin autor identificado, como «nuestros escritores».
- Un mismo pasaje puede generar varias filas cuando Mariana atribuye el mismo testimonio a más de una autoridad.

La columna **Cita normalizada** corrige únicamente la ortografía y la lectura del OCR cuando son evidentes; conserva el contenido y el orden del texto.

## 4. Fuente material

| Campo | Valor |
|---|---|
| Título | *Historia General de España, compuesta primero en latín, después vuelta en castellano por Juan de Mariana* |
| Lugar | Toledo |
| Imprenta | Pedro Rodríguez |
| Fecha | 5 de octubre de 1601 |
| Formato | 2 tomos en folio |
| OCLC | 36264560 |
| USTC | 5006449 |

El texto de trabajo es [Ediciones_HGE/HGE_TomosI-II.txt](Ediciones_HGE/HGE_TomosI-II.txt), obtenido a partir de la digitalización de la edición de 1601. El OCR contiene abreviaturas, ligaduras y confusiones frecuentes de `ſ`, `v/u` e `i/l`; por eso la lectura manual y la normalización siguen siendo necesarias.

## 5. Estructura del repositorio

```text
proyecto-autores/
├── README.md
├── Análisis de datos/
│   └── Autores y obras.md
├── Ediciones_HGE/
│   └── HGE_TomosI-II.txt
├── Notas/
│   └── Apuntes sobre HGE Cap I-IV.txt
├── Tablas/
│   ├── Tabla de autores (Libros I-V).md
│   └── Capítulos sin citas.md
└── .gitignore
```

## 6. Archivos principales

- [Tablas/Tabla de autores (Libros I-V).md](Tablas/Tabla%20de%20autores%20%28Libros%20I-V%29.md): corpus principal, con 324 entradas de los Libros I–V.
- [Ediciones_HGE/HGE_TomosI-II.txt](Ediciones_HGE/HGE_TomosI-II.txt): OCR consolidado de la edición de 1601.
- [Notas/Apuntes sobre HGE Cap I-IV.txt](Notas/Apuntes%20sobre%20HGE%20Cap%20I-IV.txt): apuntes de trabajo del análisis de los Libros I–IV.
- [Análisis de datos/Autores y obras.md](Análisis%20de%20datos/Autores%20y%20obras.md): catálogo auxiliar no exhaustivo de 20 menciones de obra de los Libros I–IV, con referencias a filas actuales.
- [Tablas/Capítulos sin citas.md](Tablas/Capítulos%20sin%20citas.md): auditoría de 23 capítulos sin cita historiográfica en los Libros I–IV, con líneas del OCR consolidado.

## 7. Tabla de autores

La [tabla principal](Tablas/Tabla%20de%20autores%20%28Libros%20I-V%29.md) está organizada por libro y capítulo. Sus columnas son:

| Columna | Contenido |
|---|---|
| `#` | Número global de la entrada |
| `Autor` | Autoridad citada |
| `Capítulo` | Capítulo dentro del libro correspondiente |
| `Cita normalizada` | Extracto OCR normalizado |
| `Contexto` | Función del testimonio en el argumento de Mariana |
| `Temática` | Clasificación del contenido |

## 8. Catálogos de referencia

| Catálogo | URL |
|---|---|
| Library of Congress | https://www.loc.gov |
| Biblioteca Nacional de España | https://www.bne.es |
| Biblioteca de Castilla-La Mancha | https://patrimoniodigital.castillalamancha.es |
| VIAF | https://viaf.org |
| USTC | https://ustc.ac.uk |
| Gateway to the German Early Books | https://gesamtkatalogderwiegendrucke.de |
| Catálogo Colectivo del Patrimonio Bibliográfico | https://bvpb.mcu.es |

### Bibliotecas digitales

| Biblioteca | URL |
|---|---|
| BNE Digital | https://bnedigital.bne.es |
| Gallica (Bibliothèque nationale de France) | https://gallica.bnf.fr |
| Biblioteca Virtual Miguel de Cervantes | https://www.cervantesvirtual.com |
| Internet Archive | https://archive.org |

## 9. Estado de la documentación

La tabla de autores es la fuente primaria del proyecto para el alcance I–V. Los apuntes y la auditoría de capítulos corresponden a I–IV; el catálogo de obras es un extracto auxiliar no exhaustivo de ese mismo alcance. Las referencias obsoletas a `Tabla de autores.md` y a `Tabla de capítulos.md` se han retirado de este README porque esos archivos ya no existen.

*Última actualización: 25 de septiembre de 2026*

[Repositorio en GitHub](https://github.com/RRCarlos/proyecto-autores)
