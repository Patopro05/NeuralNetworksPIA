# ***NeuralNetworksPIA***
## **Entrenamiento de una Red Neuronal**
___Producto Integrador de Aprendizaje para la materia Redes Neuronales.___  
El objetivo de este trabajo es el de proponer una red neuronal de cualquier tipo de arquitectura para la resolución de un problema que involucre un conjunto de datos arbitrariamente seleccionados. En este sentido, la propuesta consiste en el desarrollo de una interfaz minimalista capaz de recibir archivos de **imágenes** de resonancia magnética (MRI) de cerebros de pacientes con **4 diferentes** grados de demencia originados por la enfermedad de Alzheimer y procesarlos para identificar y **clasificar** a qué etapa de la demencia corresponde[^1].


| Nombre | Matricula |
| :----------- | :-----------: |
| Fernando Patricio Gutiérrez González | 2010356 |
| Carlos Alberto Saucedo Ríos | 1968121 |
| Mariangeles Sofía Rodríguez Uzcategui | 2132315 |

Docente: Dr. Tomás Eloy Salais Fierro.

``Ciudad Universitaria, San Nicolás de los Garza, Nuevo León. A 12 de abril del 2026.``


## **Instrucciones de uso:**
1. **Abrir terminal/VS Code**: Abra una terminal limpia en su computadora y escriba el siguiente comando para descargarse la carpeta del proyecto contenida en el repositorio:  
```git clone https://github.com/TuUsuario/NeuralNetworksPIA.git```

2. **Entrar al proyecto**: Escriba ```cd NeuralNetworksPIA```  para entrar a la carpeta que acaba de descargar.
(Al abrir la carpeta, verá la app.py, el script train.py, el modelo modelo_alzheimer.h5, y la carpeta TestingImages).

3. **Preparar el entorno**:  Cree y active un entorno virtual (recomendado) para evitar conflictos con otras librerías en su sistema ejecutando en la terminal: 
```python -m venv venv``` 
Una vez creado, actívelo dependiendo de su sistema operativo: En Windows: ```.\venv\Scripts\activate.bat``` En Mac/Linux: ```source venv/bin/activate```

3. **Instalar dependencias**: Con el entorno activado, instale las librerías requeridas para la interfaz y la red neuronal ejecutando en la terminal:
```pip install -r requirements.txt```

4. **Abrir aplicación**: Para poder abrir la aplicación y hacer pruebas con las imágenes contenidas en la carpeta ```TestingImages```, escriba en la terminal:
```streamlit run app.py```

6. **Probar modelo**: Automáticamente, se le abrirá una pestaña en el navegador predeterminado con la interfaz de la aplicación.En la aplicación, dará clic al botón de "Subir imagen". Se abrirá su explorador de archivos. Navegue dentro de la carpeta ```TestingImages/```, y seleccione una imagen al azar.  
La red neuronal le dará el diagnóstico y el porcentaje de confianza en pantalla. Repita este paso cuantas veces sea necesario.

## **Enlaces externos**
+ Kaggle:
+ Reporte:
+ Presentación:
+ Repositorio: 
+ Python:
+ Git:
+ Visual Studio Code:

[^1]: Disclaimer: La precisión clínica de este proyecto decae conforme el dataset utilizado para el entrenamiento de la red neuronal sea modificado de su versión original. Este software se realizó con fines educativos en materia del funcionamiento de las redes neuronales y la arquitectura moderna de los algoritmos de aprendizaje computacional; este software no debe usarse con fines clínicos, diagnóstico y/o monitoreo de patologías neuronales en pacientes que hayan realizado pruebas de Imagen de Resonancia Magnética (MRI).