<center>
   <img src="assets/banner.png" width="100%">
</center>


![GitHub last commit](https://img.shields.io/github/last-commit/RodolfoFerro/luigi-pipeline-talk?style=for-the-badge) 
![GitHub repo size](https://img.shields.io/github/repo-size/RodolfoFerro/luigi-pipeline-talk?style=for-the-badge) 
![License](https://img.shields.io/github/license/RodolfoFerro/luigi-pipeline-talk?style=for-the-badge) <br>
[![Twitter](https://img.shields.io/twitter/follow/FerroRodolfo?label=Twitter&logo=twitter&style=for-the-badge)](https://twitter.com/rodo_ferro/) 
[![LinkedIn](https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555)](https://www.linkedin.com/in/rodolfoferro/) <br>
[![Slides](https://img.shields.io/static/v1?label=Slides&message=Google%20Slides&color=tomato&style=for-the-badge)](https://docs.google.com/presentation/d/e/2PACX-1vTUzVQPPTNGgkkhOQxjzQA94Hdx-zq6K0_J0mL4qwSJlSLti103gCEjbFMqIljs0p3Ep1f7XAm9WSem/pub?start=false&loop=false&delayms=3000)

Este repo ilustra un proceso sencillo de automatización de transformación y modelado de datos, a través de un pipeline utilizando Luigi.

#### Stack principal

- Python 3.7+
- Streamlit
- Scikit-learn
- Pandas
- Luigi


## Idea

El proceso completo es descrito en una app interactiva que encuentras en el script `app.py`. Checa los detalles de cómo levantar la app en la sección de cómo ejecutar los scripts.

## Setup

1. Crea un entorno virtual (te recomiendo usar `conda`):
   ```bash
   conda create --name data-pipes python=3.7
   ```
2. Activate the virtual environment:
   ```bash
   conda activate data-pipes
   ```
3. Install requirements:
   ```bash
   pip install -r requirements.txt
   ```


## Ejecuta los scripts

#### App interactiva

Para ejecutar la app interactiva, simplemente ejecuta el comando de Streamlit con el entorno virtual activado:
```bash
(data-pipes) streamlit run app.py
```

Esto abrirá un servidor local en: [`http://localhost:8501`](http://localhost:8501).

#### Pipeline de datos

Si deseas ejecutar una tarea en específico ,supongamos la `TareaX` que se encuentra en el script `tareas.py`, entonces ejecuta el comando:

```bash
PYTHONPATH=. luigi --module tareas TareaX --local-scheduler
```

¡Puedes extender el código y agregar las tareas que tú desees!
