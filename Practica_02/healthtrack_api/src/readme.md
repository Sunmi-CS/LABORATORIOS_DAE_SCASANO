# HealthTrack API

API REST desarrollada con **Django** y **Django REST Framework (DRF)** para la gestión de **Pacientes** y **Doctores**.  
Cada paciente está asignado a un doctor, y la aplicación permite realizar todas las operaciones CRUD mediante endpoints, incluyendo búsqueda por nombre o diagnóstico.


Sunmi Casaño Suarez
---

## Tecnologías Usadas

- **Python 3.10+**
- **Django 5**
- **Django REST Framework (DRF)**
- **SQLite** (base de datos por defecto)
- **cURL / Postman** para pruebas de los endpoints

---

## Instalación y Ejecución del Servidor

### Clonar el repositorio
```bash
git clone https://github.com/Sunmi-CS/LABORATORIOS_DAE_SCASANO/tree/main/Practica_02/healthtrack_api
cd healthtrack_api

http://127.0.0.1:8000/api/patients/
http://127.0.0.1:8000/api/patients/3/
http://127.0.0.1:8000/api/patients/?search=luis

http://127.0.0.1:8000/api/doctors/
http://127.0.0.1:8000/api/doctors/2/
http://127.0.0.1:8000/api/doctors/?search=CARDIOLOGIA
