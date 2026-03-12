# Pandas: Una guía extensa

## ¿Qué es pandas?
Pandas es una biblioteca de Python especializada en el análisis y manipulación de datos, especialmente datos tabulares (como hojas de cálculo o bases de datos). Es ampliamente utilizada en ciencia de datos, análisis estadístico, ingeniería y desarrollo web.

## ¿Por qué usar pandas?
- Permite leer, transformar y analizar datos de manera eficiente.
- Facilita la limpieza de datos, filtrado, agrupación y visualización.
- Soporta múltiples formatos: CSV, Excel, SQL, JSON, etc.

## Conceptos clave
### DataFrame
El objeto principal de pandas es el DataFrame, una estructura de datos similar a una tabla de Excel o SQL.

```python
import pandas as pd
# Crear un DataFrame
mi_tabla = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Pedro'],
    'Edad': [23, 34, 29]
})
```

### Series
Una Series es una columna de datos, con etiquetas (índices).

```python
serie_edades = mi_tabla['Edad']
```

## Operaciones comunes
- **Lectura de datos:**
  - `pd.read_csv('archivo.csv')`
  - `pd.read_excel('archivo.xlsx')`
- **Filtrado:**
  - `mi_tabla[mi_tabla['Edad'] > 30]`
- **Agrupación:**
  - `mi_tabla.groupby('Nombre').mean()`
- **Transformación:**
  - `mi_tabla['Edad'] = mi_tabla['Edad'] + 1`
- **Visualización:**
  - Integración con matplotlib para gráficos.

## Ejemplo práctico
Supón que tienes una base de datos de encuestas en Django. Puedes extraer los datos, convertirlos a DataFrame y analizarlos:

```python
import pandas as pd
from .models import Encuesta
encuestas = Encuesta.objects.all()
df = pd.DataFrame(list(encuestas.values('fecha', 'satisfaccion')))
promedio = df['satisfaccion'].mean()
```

## Visualización de datos
Pandas se integra con matplotlib para crear gráficos:

```python
import matplotlib.pyplot as plt
conteo = df['satisfaccion'].value_counts()
conteo.plot(kind='bar')
plt.show()
```

## ¿Cómo funcionan las librerías en Python?
Una librería es un conjunto de funciones y clases que resuelven problemas específicos. Para usar una librería:
1. Se instala (por ejemplo, con pip).
2. Se importa en el código (`import pandas as pd`).
3. Se utilizan sus funciones y clases.

Las librerías permiten reutilizar código, ahorrar tiempo y evitar errores.

## Ventajas de pandas
- Sintaxis sencilla y poderosa.
- Gran comunidad y documentación.
- Compatible con otras librerías como numpy, matplotlib y scikit-learn.

## Recursos para aprender más
- [Documentación oficial de pandas](https://pandas.pydata.org/docs/)
- Tutoriales en YouTube y blogs.
- Libros como "Python for Data Analysis" de Wes McKinney.

---

Pandas es una herramienta fundamental para cualquier persona que trabaje con datos en Python. Te permite transformar, analizar y visualizar información de manera profesional y eficiente.
