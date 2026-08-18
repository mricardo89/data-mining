Caso de Uso
Contexto del Sistema Actual:

Ustedes son el equipo de software de "CaféExpress", una cadena nacional de cafeterías. Tienen una aplicación móvil estándar donde los clientes pueden hacer pedidos por adelantado, pagar y dejar reseñas. Su base de datos actual registra sin problemas el histórico de ventas: qué usuario compró qué café, a qué hora y en qué sucursal.



El Nuevo Requerimiento del Cliente:

El gerente de operaciones se dio cuenta de que están perdiendo mucho dinero tirando comida que no se vende y perdiendo clientes por mal servicio. Les ha pedido agregar un módulo de inteligencia a la app con dos objetivos:

Predicción de Inventario: El sistema debe predecir cuántos "Croissants" y cuántos "Cafés Helados" se van a vender mañana en la sucursal Centro, para que el gerente sepa cuánto hornear.
Análisis de Reseñas: Cuando un cliente califica su pedido con 1 estrella, la app le permite subir una queja escrita en texto libre y adjuntar una fotografía (por ejemplo, de un café derramado o un pan quemado). El sistema debe analizar automáticamente estas evidencias para emitir un cupón de reembolso al instante sin intervención humana.




Retos a Resolver por Equipo
Con base en los conceptos vistos en clase, los equipos tendrán 20 minutos para debatir y plasmar en una hoja el diseño lógico de su solución:



Reto A: Auditoría de Fuentes de Información



Analicen la aplicación "CaféExpress" y clasifiquen las fuentes de datos que necesitarán para cumplir con el requerimiento del gerente:

¿Qué información de este problema es puramente Estructurada? (Mencionen al menos 3 columnas de su base de datos tradicional que usarían).
¿Qué información generada por la app es Semi-estructurada? (Ej. ¿Qué metadatos o formato usaría el celular del cliente para enviar el reporte de error al servidor?)
¿Qué información es No estructurada? (Identifiquen las fuentes crudas que requieren algoritmos complejos para entenderse).


Reto B: Mapeo del Proceso de Minería



Tracen un diagrama de los 5 pasos del Proceso KDD aplicados exclusivamente al problema del Análisis de Reseñas:

Selección: ¿De dónde extrae su backend las imágenes que van a ser procesadas hoy?
Preprocesamiento / Limpieza: Si los usuarios suben fotos oscuras, borrosas, gigantes o en diferentes formatos (PNG, JPG, HEIC), ¿qué tendría que hacer el código antes de que la IA intente "ver" el problema?
Transformación: ¿Cómo se estandariza esa imagen limpia para que un modelo matemático pueda procesarla?
Minería de Datos (Extracción): ¿Qué es lo que buscará el algoritmo en este paso?
Interpretación / Evaluación: ¿Cómo toma el backend ese resultado matemático y lo convierte en una acción útil para el usuario en la aplicación móvil?


Entregable: documento con las respuestas de lo solicitado.