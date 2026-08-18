Objetivo de la práctica: Comprender la esencia de la ciencia de datos descubriendo patrones, correlaciones y anomalías de manera puramente visual y analítica, simulando el trabajo que los algoritmos de extracción realizarán más adelante en el curso.

Reglas del juego:

Desconexión total: Durante los próximos 30 minutos, las laptops, tablets y teléfonos celulares deben estar guardados. Solo se usará sus laptops para visualizar el dataset asignado
Contexto aislado: Las respuestas a las preguntas que se les plantean deben derivarse únicamente de los datos en el dataset asignado. No utilicen suposiciones externas ni conocimientos previos sobre la industria; los datos mandan.
Instrucciones por equipo:

Reconocimiento del terreno (5 minutos): Recibirán una muestra impresa de un conjunto de datos (dataset) real extraído de Kaggle. Antes de leer las preguntas, examinen las columnas (variables). Entiendan qué representa cada fila y qué tipo de información tienen frente a ustedes (texto, números enteros, fechas, categorías).
Extracción y debate (20 minutos): Lean las 3 preguntas asignadas a su dataset. Discutan en equipo y busquen la respuesta "arrastrando el lápiz": cuenten, agrupen visualmente, tachen o subrayen registros que les llamen la atención.
Justificación de hallazgos (5 minutos): Anoten sus respuestas definitivas. Es obligatorio incluir una breve justificación metodológica de cómo llegaron a esa conclusión (por ejemplo: "notamos visualmente que todos los registros con la categoría X tenían un valor mayor a Y en la columna Z").
Plenaria y entrega: Al agotar el tiempo, un representante de cada equipo tendrá un máximo de 2 minutos para explicarle al resto de la clase de qué trataban sus datos, cuál fue el hallazgo más interesante y entregar su hoja de respuestas.




Equipo 1
Google Play Store Apps: Acceso
Variables clave en la muestra: Nombre de la App, Categoría (Juegos, Productividad, etc.), Rating (1-5), Tamaño (MB), Instalaciones, Tipo (Gratis/Pago).
Preguntas para el equipo:
Agrupando las aplicaciones por "Categoría", ¿cuál de ellas concentra el mayor número de instalaciones totales en esta hoja?
Observen el "Rating" y el "Tamaño". ¿Existe alguna tendencia visual que indique que las aplicaciones más pesadas (mayor a 50MB) tienen mejores o peores calificaciones?
Si tuvieran que decidir lanzar una nueva aplicación hoy basándose solo en este papel, ¿en qué categoría la harían y por qué?


Equipo 2
Web Server Access Logs : Access link
Variables clave en la muestra: Timestamp (Hora), Método HTTP (GET, POST), Endpoint (/login, /home), Código de Estado (200, 404, 500), Tiempo de Respuesta (ms).
Preguntas para el equipo:
¿Cuál es el endpoint que genera la mayor cantidad de códigos de estado 500 (Errores de servidor)?
Calculen un promedio rápido "a ojo" del tiempo de respuesta. ¿Los métodos POST tardan consistentemente más que los métodos GET?
Identifiquen el lapso de tiempo (ej. 10:00 - 10:05) con mayor tráfico. ¿Qué porcentaje de las peticiones en esa "hora pico" resultaron en errores (404 o 500)?


Equipo 3
Video Game Sales: Link
Variables clave en la muestra: Nombre del Juego, Plataforma (PC, PS5, Xbox), Año de Lanzamiento, Género, Ventas Norteamérica (Millones), Ventas Japón (Millones).
Preguntas para el equipo:
Comparen las columnas de ventas entre Norteamérica y Japón. ¿Qué género domina claramente en cada región?
¿Hay alguna consola en esta muestra que dependa exclusivamente de un solo género para lograr sus ventas altas?
Encuentren el juego más antiguo y el más reciente de la hoja. ¿Cómo ha cambiado el volumen de ventas general entre esos dos años?


Equipo 4
Abandono de Clientes (Customer Churn - Telecom/Streaming): Enlace
Variables clave en la muestra: Edad del Cliente, Tipo de Plan (Básico/Premium), Meses Activo (Antigüedad), Problemas de Soporte Reportados, Canceló el Servicio (Sí/No).
Preguntas para el equipo:
Observando exclusivamente a los clientes en la columna "Canceló el Servicio" con valor "Sí", ¿qué patrón visual comparten la mayoría de ellos (ej. pertenecen a un plan específico o tienen cierta antigüedad)?
Comparen a los usuarios más antiguos (mayor cantidad de "Meses Activo") con los más nuevos. ¿Qué grupo tiende a tener más "Problemas de Soporte Reportados"?
Si la empresa les diera presupuesto para regalar un mes gratis y evitar futuras cancelaciones, ¿a qué perfil exacto de cliente se lo ofrecerían basándose en esta hoja?


Equipo 5
Precios de Bienes Raíces (House Prices): Enlaces
Variables clave en la muestra: Metros Cuadrados, Número de Habitaciones, Tiene Estacionamiento (Sí/No), Distancia al Centro de la Ciudad (km), Precio de Venta (USD).
Preguntas para el equipo:
A simple vista, ¿qué variable parece tener un impacto más directo y drástico en el "Precio de Venta": los "Metros Cuadrados" o la "Distancia al Centro de la Ciudad"?
Busquen dos propiedades que tengan el mismo "Número de Habitaciones" pero precios de venta muy diferentes. ¿Cuál de las otras variables explica lógicamente esa diferencia de costo?
Si un comprador llega con el presupuesto más bajo de toda la lista, ¿qué característica o comodidad tendrá que sacrificar inevitablemente según los patrones de esta muestra?