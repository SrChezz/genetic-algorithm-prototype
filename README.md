# Timetable: Automatización de Horarios con Algoritmos Genéticos

Este documento describe nuestro proyecto _Timetable, un sistema de generación automatizada de horarios que utiliza **algoritmos genéticos, implementado en **Python_.

---

## El Problema

Crear un horario de clases es un problema _NP-hard. Los algoritmos de búsqueda heurística pueden encontrar soluciones óptimas para casos simples, pero para escenarios complejos con muchas restricciones, encontrar una buena solución puede ser muy lento o incluso imposible. Aquí es donde entran en juego los \*\*algoritmos genéticos_.

---

## Contexto de Nuestro Proyecto

Nuestro proyecto _Timetable_ aborda la generación de horarios en un _contexto universitario_, donde se deben considerar múltiples restricciones:

- _Disponibilidad de profesores_:  
  Los profesores tienen horarios limitados y no pueden estar en dos lugares a la vez.

- _Disponibilidad de estudiantes_:  
  Los grupos de estudiantes también tienen otras clases y actividades.

- _Asignación de aulas_:  
  Las aulas tienen capacidades diferentes y algunas cuentan con recursos especiales como computadoras (laboratorios).

- _Requisitos de los cursos_:  
  Algunos cursos pueden requerir aulas con características específicas.

---

## La Solución: Adaptando el Prototipo a Nuestro Contexto

El prototipo utiliza un archivo de configuración (.cfg) para definir los objetos y sus relaciones. Este formato se adapta fácilmente a nuestro proyecto.

### Archivo de Configuración (.cfg)

#### Tipos de Objetos:

- #profesor: Describe un profesor.
- #curso: Describe un curso.
- #aula: Describe un aula.
- #grupo: Describe un grupo de estudiantes.
- #clase: Describe una clase y la vincula con un profesor, un curso y un grupo de estudiantes.

---

### Atributos de los Objetos:

#### _#profesor_

- id (numérico, obligatorio): ID del profesor.
- nombre (texto, obligatorio): Nombre del profesor.

#### _#curso_

- id (numérico, obligatorio): ID del curso.
- nombre (texto, obligatorio): Nombre del curso.

#### _#aula_

- nombre (texto, obligatorio): Nombre del aula.
- capacidad (numérico, obligatorio): Número de asientos en el aula.
- laboratorio (booleano, opcional): Indica si el aula es un laboratorio (tiene computadoras). Si no se especifica, el valor predeterminado es false.

#### _#grupo_

- id (numérico, obligatorio): ID del grupo de estudiantes.
- nombre (texto, obligatorio): Nombre del grupo de estudiantes.
- tamaño (numérico, obligatorio): Número de estudiantes en el grupo.

#### _#clase_

- profesor (numérico, obligatorio): ID de un profesor; vincula un profesor a una clase.
- curso (numérico, obligatorio): ID de un curso; vincula un curso a una clase.
- grupo (numérico, obligatorio): ID de un grupo de estudiantes; vincula el grupo de estudiantes a una clase. Cada clase puede estar vinculada a varios grupos de estudiantes.
- duracion (numérico, opcional): Duración de la clase (en horas). Si no se especifica, el valor predeterminado es 1.
- laboratorio (booleano, opcional): Indica si la clase requiere computadoras en un aula. Si no se especifica, el valor predeterminado es false.

---

### Ejemplo de Archivo de Configuración:

```cfg
#profesor
    id = 1
    nombre = Dr. Juan Pérez
#end

#curso
    id = 1
    nombre = Inteligencia Artificial
#end

#aula
    nombre = A101
    capacidad = 30
    laboratorio = true
#end

#grupo
    id = 1
    nombre = IA-2023-1
    tamaño = 25
#end

#clase
    profesor = 1
    curso = 1
    grupo = 1
    duracion = 2
    laboratorio = true
#end
```
# genetic-algorithm-prototype
