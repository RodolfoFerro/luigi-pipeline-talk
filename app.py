# ==============================================================
# Author: Rodoflo Ferro
# Twitter: @rodo_ferro
#
# ABOUT COPYING OR USING PARTIAL INFORMATION:
# This script has been originally created by Rodolfo Ferro.
# Any explicit usage of this script or its contents is granted
# according to the license provided and its conditions.
# ==============================================================

# -*- coding: utf-8 -*-

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import streamlit as st
import pandas as pd
import numpy as np


# Sidebar
st.sidebar.title("Parámetros de imputación")
st.sidebar.markdown(
    """
    Puedes utilizar el selector de esta barra para cambiar en tiempo real
    los valores de imputación para los datos, al seleccionar el método de
    imputación.
    """
)

imputers = ['mean', 'median', 'most_frequent']
imputer_selector = st.sidebar.selectbox(
    "Selecciona el método de imputación:",
    imputers
)

# Load data
data = pd.read_csv('data/datos_ventas.csv')

# Intro section
st.title("Exploración de datos y preprocesamiento")
st.write(
    """
    Bienvenid@ a este sencillo ejemplo que ejecuta algunos procesos previos
    al modelado de la información. Dichos procesos involucran transformaciones,
    limpieza y llenado de datos faltantes para tener un conjunto de datos que
    pueda ser modelado.
    """
)

# Data loading
st.header("Cargando los datos")
st.markdown(
    """
    A continuación cargamos los datos (originales) a utilizar. Dichos datos pueden ser
    encontrados en la carpeta de datos como `data/datos_ventas.csv`.

    > **Nota:** Los datos y el código fuente de esta aplicación web pueden ser encontrados
    > en el repositorio de GitHub 
    > [https://github.com/RodolfoFerro/luigi-pipeline-talk](https://github.com/RodolfoFerro/luigi-pipeline-talk).

    Los datos pueden ser cargados utilizando pandas con las líneas:
    ```python
    import pandas as pd

    data = pd.read_csv('data/datos_ventas.csv')
    ```

    > **Nota:** Para desplegar los datos en pantalla, puedes llamar directamente a la variable
    > desde una celda si usas Jupyter Notebooks/Lab o Google Colab o imprimir los datos con
    > la función `print`.
    > ```python
    > # Desde un notebook
    > data
    > # Desde un script
    > print(data)
    > ```

    Al desplegar los datos deberías ver una tabla como la siguiente:
    """
)
st.dataframe(data)
st.markdown(
    """
    Posterior al despliegue, podemos identificar las variables dependientes de las
    independientes. Notemos que las variables de `PAIS`, `EDAD` y `SALARIO` las
    consideraremos como independientes y las utilizaremos para predecir la variable
    dependiente `COMPRA`.
    """
)

# Data imputation
st.header("Imputación y _encoding_ de datos")
st.markdown(
    """
    Como se mencionó en la sesión, de la tabla de datos que hemos desplegado, podemos
    observar algunas características, como el hecho de que hay algunos campos vacíos
    (`NaN`'s), o que tenemos variables categóricas. Esto lo arreglaremos con procesos
    de imputación y codificación de datos.
    """
)

st.subheader("Imputación de datos")
st.markdown(
    """
    Para la imputación de datos podemos redefinir los campos necesarios (que estén
    vacíos) agregando un valor numérico; para ello, existen distintas estrategias,
    pues se pueden agregar valores definidos por la media, mediana, moda o alguna
    constante.

    Este proceso de imputación se puede realizar directamente con Python utilizando
    el paquete `sklearn` como sigue:

    ```python
    from sklearn.impute import SimpleImputer
    import numpy as np

    imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
    imputer = imputer.fit(data.iloc[:, 1:3])
    data.iloc[:, 1:3] = imputer.transform(data.iloc[:, 1:3])
    ```

    Para el parámetro `strategy` puedes seleccionar de la barra lateral izquierda
    algún otro método y comparar los diferentes resultados. Podrás apreciar en tiempo
    real los cambios de manera directa sobre la tabla de valores. El parámetro
    `strategy` de tu código en el objeto `SimpleImputer` puede recibir los valores
    `mean`, `median` y `most_frequent` (o incluso una constante).

    > **Nota:** Fijé la barra del lado izquierdo para que posteriormente puedas
    > seguir modificando los valores del imputador y que veas cómo varían los datos
    > incluso en el reescalamiento.
    """
)

imputer = SimpleImputer(missing_values=np.nan, strategy=imputer_selector)
imputer = imputer.fit(data.iloc[:, 1:3])
data.iloc[:, 1:3] = imputer.transform(data.iloc[:, 1:3])
st.dataframe(data)

st.subheader("_Encoding_ de datos")
st.markdown(
    """
    Para el _encoding_ o codificación de valores categóricos a valores numéricos
    podemos utilizar varias aproximaciones. Para los valores de `PAIS`, los primero
    que haremos será convertir los valores de las etiquetas a valores numéricos
    (como un identificador entero), para psoteriormente usar la transformación
    de _one-hot encoding_ y convertirlos a vectores unitarios (con una representación
    del elemento por posición). Para conservar los datos originales y ver cómo se
    asignan categorías numéricas por nombre de país, crearé una nueva columna llamada
    `LABEL_ENCODING` y la reordenaré para que quede a la derecha de la columna `PAIS`.

    Este proceso de _encoding_ se puede realizar directamente con Python utilizando
    el paquete `sklearn` como sigue:

    ```python
    from sklearn.preprocessing import LabelEncoder

    label_encoder = LabelEncoder()
    data['LABEL_ENCODING'] = label_encoder.fit_transform(data.iloc[:, 0])
    data = data[['PAIS', 'LABEL_ENCODING', 'EDAD', 'SALARIO', 'COMPRA']]
    ```

    Notemos en el código que se ha agregado una nueva columna y se ha reordenado para
    aparecer junto a la columna `PAIS`.
    """
)
label_encoder = LabelEncoder()
data['LABEL_ENCODING'] = label_encoder.fit_transform(data.iloc[:, 0])
data = data[['PAIS', 'LABEL_ENCODING', 'EDAD', 'SALARIO', 'COMPRA']]
st.dataframe(data)

st.markdown(
    """
    Podemos observar cómo se han asignado los valores, sin embargo, como se mencionó en
    la sesión, es necesario transformar ahora dichos valores a representaciones que
    tengan un peso equitativo. Para ello utilizaremos un _one-hot encoding_.

    Este proceso de _encoding_ se puede realizar directamente con Python utilizando
    el paquete `sklearn` como sigue:

    ```python
    from sklearn.preprocessing import OneHotEncoder

    onehot_encoder = OneHotEncoder()
    onehot = onehot_encoder.fit_transform(data[['LABEL_ENCODING']]).toarray()
    ```

    Una vez que tengamos los datos transformados, podemos ver el resultado de la
    transformación, donde la columna `0` corresponde al valor de Alemania, la
    columna `1` al valor de España y `2` al valor de Francia.
    """
)
onehot_encoder = OneHotEncoder()
onehot = onehot_encoder.fit_transform(data[['LABEL_ENCODING']]).toarray()
st.dataframe(onehot)

st.markdown(
    """
    Esta última matriz de valores puede ser integrada la tabla de datos originales,
    para obtener la tabla de datos con variables independientes definitiva que podremos
    utilizar para crear un modelo de _machine learning_. Sólo faltará transformar la
    variable dependiente (a predecir) y reescalar los datos.

    Además, reordenamos las columnas para tener un mejor control e identificación
    visual de las variables.

    ```python
    data['ALEMANIA'] = onehot[:, 0]
    data['ESPANA'] = onehot[:, 1]
    data['FRANCIA'] = onehot[:, 2]
    data = data[['PAIS', 'LABEL_ENCODING', 'ALEMANIA', 'ESPANA', 'FRANCIA', 'EDAD', 'SALARIO', 'COMPRA']]
    """
)
data['ALEMANIA'] = onehot[:, 0]
data['ESPANA'] = onehot[:, 1]
data['FRANCIA'] = onehot[:, 2]
data = data[['PAIS', 'LABEL_ENCODING', 'ALEMANIA', 'ESPANA', 'FRANCIA', 'EDAD', 'SALARIO', 'COMPRA']]
st.dataframe(data)

st.subheader("Variable dependiente")
st.markdown(
    """
    Para la variable dependiente repetiremos el proceso de transformación de etiquetas.

    ```python
    dep_label_encoder = LabelEncoder()
    data['COMPRA'] = dep_label_encoder.fit_transform(data.iloc[:, 3])
    ```

    Esto cambiará los valores de la columna `COMPRA` de `Yes`/`No` a valores `1`/`0`, como
    se puede apreciar en la tabla de datos actualizada.
    """
)
dep_label_encoder = LabelEncoder()
data['COMPRA'] = dep_label_encoder.fit_transform(data.iloc[:, 3])
st.dataframe(data)

st.header("Escalamiento de datos")
st.markdown(
    """
    Hasta este punto, estamos muy cerca de concluir el proceso de limpieza y transformación
    de datos, puesto que ya sólo necesitamos realizar un reescalamiento de las variables
    independientes a través de un proceso de normalización o estandarización (significa
    que utilizamos la media y la varianza para transformar los datos para que ahora
    tengan una distribución normal, de ahí el nombre de _normalizar_). 
    
    Esto podemos realizarlo de manera sencilla, nuevamente, utilizando `sklearn`.

    ```python
    from sklearn.preprocessing import StandardScaler

    scaler = StandardScaler()
    data.iloc[:, 2:7] = scaler.fit_transform(data.iloc[:, 2:7])
    ```

    Y de esta manera obtenemos los datos finales, limpios y transformados.
    """
)
scaler = StandardScaler()
data.iloc[:, 2:7] = scaler.fit_transform(data.iloc[:, 2:7])
st.dataframe(data)

st.markdown(
    """
    En caso de querer extraer sólo las variables independientes y dependiente
    para usar en un modelo, podemos realizarlo de manera muy sencilla, sólo basta
    seleccionar las columnas que queremos para cada caso.

    ```python
    x = data[['ALEMANIA', 'ESPANA', 'FRANCIA', 'EDAD', 'SALARIO']].values
    y = data[['COMPRA']].values
    ```

    Así, podemos ver que tenemos en una variable `x` a la matriz con datos
    independientes:
    """
)
x = data[['ALEMANIA', 'ESPANA', 'FRANCIA', 'EDAD', 'SALARIO']].values
st.dataframe(x)

st.markdown(
    """
    Y a la variable `y` (dependiente) como la lista con la variable a
    predecir en el modelo.
    """
)
y = data[['COMPRA']].values
st.dataframe(y)

# Data modelling
st.header("Modelado de datos")
st.markdown(
    """
    Se puede modelar de manera sencilla utilizando una máquina de soporte
    vectorial (SVM) con el siguiente código:

    ```python
    from sklearn.svm import SVC

    clf = svm.SVC(kernel='rbf')
    clf.fit(x, y)
    ```

    Una vez entrenado el modelo, puedes predecir nuevos valores.

    ```python
    clf.predict([[1.5275, -0.6547, -0.8165, 1.6308, 1.7521]])
    # array(['No'], dtype=object)
    ```
    """
)
