# Searchify 
Searchify es un Sistema de Recuperación de Información (SRI). Cuenta con una base de datos  obtenida de ir_datasets, específicamente la biblioteca de ´Cranfield´, orientada al desarrollo de softwares de recuperación de información ya que proporciona información detallada sobre consultas y relevancia de documentos, lo que facilita la evaluación precisa del rendimiento del sistema desarrollado.



## Autores:

Claudia Alvarez Martínez

Roger Moreno Gutiérrez



## Tecnologías:

El funcionamiento del proyecto está basado en APIs, definidas en un servidor de **Django**, por lo que el lenguaje de programación fundamental en el backend es **python**, la interfaz gráfica es una *Single Page Application (SPA)* desarrollada en **React**, que utiliza el lenguaje **typescript**. En el directorio raíz del proyecto se encuentra el archivo `requirements.txt`, que contiene las dependencias fundamentales del servidor de Django, mientras que las dependencias de React están en `src/gui/package.json`. Para instalarlas se puede iniciar una terminal y:

Desde la carpeta raíz, para instalar las dependencias de Django:

```bash
pip install -r requirements.txt
```

Desde el directorio `.../src/gui`, para instalar las dependencias de React:

```bash
npm install
```



## Instrucciones de ejecución:

Una vez instaladas todas las dependencias, se puede ejecutar el proyecto, pero antes es necesario realizar un precómputo de los datos que ayuda a un manejo más eficiente de los datos en ejecución, para ello se ejecuta el archivo `setup.py` desde una terminal del sistema en el directorio`/src/code/`:

```bash
py setup.py
```

Luego de precomputar los datos, se pueden iniciar ambos servidores.

Para ello se ejecuta el servidor de Django desde `/src/code`, con el siguiente comando en la terminal:

```bash
py manage.py runserver
```

Y el servidor de React en un entorno de desarrollo desde `/src/gui`, con el comando en la terminal:

```bash
npm run dev
```

Una vez iniciados ambos servidores se puede acceder desde el navegador a la interfaz web por la dirección que se muestra en la terminal del servidor de React.

> Las acciones anteriores se resumieron en un archivo ejecutable en la raíz del proyecto. Para **Mac** o **Linux** el archivo `startup.sh` y para **Windows** `startup.bat`



## Enfoque teórico:

Para el desarrollo del proyecto se han implementado dos modelos de recuperación de información, el Modelo Booleano y el Modelo de Indexación de Semántica Latente (LSI).

Como principal motor de búsqueda a las consultas del usuario hemos utilizado el modelo LSI. Este se basa en que palabras usadas en el mismo contexto tienden a tener significados similares. El modelo extrae el contenido conceptual de un documento, busca emparejar por conceptos en lugar de por términos, permitiendo la recuperación de documentos relevantes basada en la similitud conceptual en lugar de coincidencias exactas de palabras. Este proceso implica mapear documentos y consultas en un espacio dimensional reducido asociado con conceptos, mejorando la recuperación de información. La técnica empleada para esto es la Descomposición en Valores Singulares (SVD) de la matriz de relación entre términos y documentos (TF-IDF).

La SVD permite reducir la complejidad de la información original, proporcionando una representación en un espacio reducido donde las similitudes semánticas son más evidentes. Esta descomposición da como resultado tres matrices: 

- $U$ captura las relaciones entre términos.
- $Σ$ destaca la importancia de los conceptos latentes
- $V^T$ describe las relaciones entre documentos.

Por otra parte, el modelo booleano se utiliza para establecer una comparativa con el modelo anterior a través de las métricas. Este se caracteriza por medir la similitud entre documentos y consultas basándose en la presencia o ausencia de términos, convirtiéndolo en un modelo muy estricto.

Las métricas utilizadas para la comparación entre los modelos fueron:

- $Precisión = \frac{R_R}{R}$ 
- $Recobrado = \frac{R_R}{R_R \cup N_R}$
- $F1 = \frac{2*Precisión*Recobrado}{Precisión + Recobrado}$ 
- $Proporción de fallo = \frac{R_I}{I}$

Donde: $R$ representa los documentos recuperados, $R_R$ los documentos recuperados que son relevantes, $N_R$ los no recuperados relevantes, $I$ los irrelevantes y $R_I$ los recuperados irrelevantes. 

Además, hemos incorporado una estrategia de expansión de consulta basada en sinónimos obtenidos a través de WordNet y NLTK. Para lograr esto, realizamos una desambiguación del contexto de nuestra consulta, permitiéndonos seleccionar de manera más precisa los sinónimos que mejor se adecuan al significado deseado. Esta estrategia busca mitigar las limitaciones de la coincidencia exacta de palabras, proporcionando una mayor capacidad para capturar la diversidad de términos relacionados con los conceptos de interés.
Cabe destacar que esta estrategia solo es utilizada en consultas propias del usuario y no en las consultas ya predefinidas. A pesar de que el modelo LSI ya aborda la similitud conceptual entre documentos y consultas al mapearlos en un espacio dimensional reducido, la inclusión de sinónimos adicionales mediante la expansión de consulta contribuye a enriquecer aún más la representación semántica. Este enfoque conjunto busca mejorar la precisión y exhaustividad de la recuperación de información al considerar tanto las relaciones semánticas latentes como las asociaciones léxicas más amplias.

## Consideraciones iniciales:

La interfaz de usuario cuenta con una barra de búsqueda para la entrada de consultas en lenguaje natural al sistema de recuperación. 

Como se ha mencionado anterirmente, los resultados mostrados a las búsquedas se procesan con el modelo LSI. 

En la barra de navegación se muestra un botón para acceder a las consultas que se encuentran en la base de datos *ir_datasets*. Estas consultas son las utilizadas en la evaluación de los modelos por medio de las métricas.



## Insuficiencias y mejoras:

Debido a la propia naturaleza del modelo booleano, hemos asumido que cuando una consulta en lenguaje natural, es procesada por este modelo, solo serán recuperados aquellos documentos en los que aparezcan todas las palabras de la consulta. Esto trae como consecuencia que al evaluar los resultados de búsqueda para dicho modelo, no se obtengan valores para las métricas, pues estas fracciones tienden a indefinirse ya que en la mayoría de los casos no se obtienen documentos recuperados. Para una mejor obtención de resultados sería una buena idea aplicar la expansión de consulta; esto permite flexibilizar la rigidez del modelo y ampliar la capacidad de capturar documentos relevantes que, de otra manera, podrían pasar desapercibidos debido a diferencias exactas en la elección de palabras.

Permitir mostrar resultados de la recuperación de información utilizando el modelo booleano.

