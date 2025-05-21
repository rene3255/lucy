# Definición del problema
- En muchos sectores de la sociedad, especialmente entre personas jóvenes o sin acceso a servicios financieros tradicionales, existe una **baja cultura del ahorro**. Los métodos tradicionales de ahorro (cuentas bancarias, inversiones bursátiles) no siempre son accesibles, comprensibles o atractivos. Como resultado, muchas personas no desarrollan **hábitos financieros sostenibles**, lo que limita sus oportunidades de crecimiento y seguridad económica. A su vez, prácticas como la numismática o la colección de metales no ferrosos, con valor intrínseco y potencial de apreciación, permanecen subutilizadas como alternativas viables de ahorro y diversificación de capital.
# Objetivo general 
- Promover la colección de objetos numismáticos y metales no ferrosos como una forma alternativa de ahorro y diversificación del capital, incentivando la cultura financiera y el hábito de ahorro en sectores de la población con acceso limitado a herramientas financieras tradicionales.

# Objetivos específicos
- 1.- Educar e incentivar a los usuarios acerca del valor del ahorro en especie mediante contenidos, experiencias y comunidades digitales centradas en monedas, billetes y metales no ferrosos.

- 2.- Facilitar la organización y registro digital de colecciones de forma simple e intuitiva, promoviendo el sentido de propiedad y seguimiento del crecimiento de sus activos físicos.

- 3.- Desarrollar funcionalidades básicas de mercado y comunidad para conectar a los **usuarios** con eventos, intercambios y referencias de valor, ampliando las posibilidades de interacción y aprendizaje colectivo.

![Principales hitos](https://drive.google.com/uc?export=view&id=1_XYcaQYM7PQy5MIDj5lypB2lzE2MXzhN)

# Historias de Usuario

## 1.1 Visualización educativa básica
- Como usuario nuevo sin experiencia, quiero acceder a la información introductoria sobre ahorro en metales, monedas y billetes, para comprender sus ventajas y empezar una colección informada.
### Criterios de Aceptación
- Sección educativa visible desde la landing page.
- Incluye artículos o videos introductorios
- Contenido disponible sin necesidad de registro

## 1.2 Segmentación por tipo de usuario
- Como nuevo usuario, quiero identificarme como aficionado, coleccionista o profesional, para recibir contenido y funciones adaptadas a mi nivel de experiencia.
### Criterios de Aceptación
- 1.- Opción de seleccionar el tipo de usuario al registrarse.
- 2.- La interfaz muestra contenido según la elección.
- 3.- Posibilidad de actualizar el rol desde el perfil.

# Instalación del proyecto Lucy
## Requisitos 
- Python 3.10 o superior
- Git instalado
- Se recomienda un entorno virtual (como venv o virtualenv)
- Pip actualizado

## 1 Clonar el repositorio
- SSH protocol
- `git@github.com:rene3255/lucy.git`
- HTTPS 
- `https://github.com/rene3255/lucy.git`
Una vez clonado el proyecto moverse al folder lucy
## 2 Crear entorno virtual
- `python3 -m venv env --prompt=Lucy`
- Activa el entorno virtual
- `source env/bin/activate`
- en Windows:
    `venv/Script/activate`
## 3 Instalar dependencias
- `pip install -r requirements.txt`
## 4 Configurar variables de entorno
- Crear un archivo .env (archivo oculto)en la raíz del proyecto y agregar las variables necesarias por ejemplo: 
    - DEBUG=True
    - SECRET_KEY=tu_clave_secreta
    - DATABASE_URL=sqlite:///db.sqlite3
## 5 Migrar la base de datos
- `python manage.py migrate`
## 6 Crear un usuario administrador
- python manage.py runserver
  
- Abre tu navegador y visita: http://localhost:8000
  
