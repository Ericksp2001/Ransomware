# Ransomware demo (Fernet) — `Encrypt.py` / `Decrypt.py`

> **Aviso importante (legal / ético):**  
> Este repositorio **es solo para uso educativo y de investigación en entornos controlados** (máquinas virtuales aisladas, laboratorios de pruebas). No lo uses ni lo distribuyas en sistemas en producción ni contra sistemas de terceras personas sin su consentimiento explícito. El desarrollo, distribución o ejecución de ransomware en sistemas sin autorización es ilegal y puede tener consecuencias penales.

---

## Índice

1. [Resumen del proyecto](#resumen-del-proyecto)  
2. [Requisitos y configuración](#requisitos-y-configuración)  
   1. [Instalación de dependencias](#instalación-de-dependencias)  
   2. [Preparar entorno de prueba (opcional)](#preparar-entorno-de-prueba-opcional)  
3. [Estructura de archivos](#estructura-de-archivos)  
4. [Descripción de `Encrypt.py`](#descripción-de-encryptpy)  
   1. [Funcionamiento general](#funcionamiento-general)  
   2. [Puntos clave del código](#puntos-clave-del-código)  
5. [Descripción de `Decrypt.py`](#descripción-de-decryptpy)  
   1. [Funcionamiento general](#funcionamiento-general-1)  
   2. [Puntos clave del código](#puntos-clave-del-código-1)  
6. [Flujo / Arquitectura del ejemplo](#flujo--arquitectura-del-ejemplo)  
7. [Uso (ejemplos)](#uso-ejemplos)  
8. [Notas de seguridad y buenas prácticas](#notas-de-seguridad-y-buenas-prácticas)  
9. [Licencia y responsabilidad](#licencia-y-responsabilidad)

---

## Resumen del proyecto

Este repositorio contiene documentación y scripts de ejemplo (`Encrypt.py` y `Decrypt.py`) que **demuestran de forma controlada el mecanismo básico de un ransomware** usando cifrado simétrico **Fernet** de la librería `cryptography` de Python.

**Nivel y alcance:**  
Este proyecto es **de nivel básico y meramente ilustrativo**. Está pensado para comprender el flujo técnico mínimo (generación de clave, cifrado de archivos, nota de rescate, y descifrado con la misma clave). **El nivel es tan básico** que muchos antivirus/antimalware modernos —por ejemplo, **Windows Defender**— **pueden detectar y eliminar el ejecutable o marcar los scripts** durante las pruebas. Este comportamiento es esperado: las soluciones de seguridad están diseñadas para bloquear y aislar este tipo de actividad.

- `Encrypt.py` — simula el proceso de ataque: genera una clave (`key.key`), cifra archivos en un directorio objetivo y deja una nota de rescate (`readme.txt`).
- `Decrypt.py` — simula la recuperación: lee la clave de `key.key`, elimina la nota y descifra los archivos.
- Algoritmo: **Fernet** (cifrado simétrico autenticado — AES-128 + HMAC-SHA256).

**Nota:** en este ejemplo la clave `key.key` se conserva para pruebas y recuperación. En un ataque real la clave no estaría disponible para la víctima.

---

## Requisitos y configuración

### Instalación de dependencias

```bash
# Recomendado: usa un entorno virtual (venv)
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows

# Instalar cryptography
pip install cryptography
```

### Preparar entorno de prueba (opcional)

Para pruebas locales según el ejemplo original:

1. Crear un directorio de pruebas (ejemplo en Windows):
   ```
   C:\Users\<usuario>\Desktop\Ataque\Primera prueba
   ```
2. Colocar algunos archivos de prueba (documentos, imágenes, etc.) en `Primera prueba`.

> Recomendación: realiza las pruebas **únicamente** en una máquina virtual o entorno aislado. No intentes desactivar o eludir las protecciones del antivirus en sistemas personales o de terceros.

---

## Estructura de archivos

- `Encrypt.py` — script que genera la clave y cifra archivos.
- `Decrypt.py` — script que lee la clave y descifra archivos.
- `key.key` — (generado por `Encrypt.py`) contiene la clave Fernet en bytes.
- `readme.txt` — nota de rescate creada por `Encrypt.py` en el directorio objetivo (simulación).

---

## Descripción de `Encrypt.py`

### Funcionamiento general

`Encrypt.py` simula la fase de ataque:

1. Genera una clave Fernet y la guarda en `key.key`.
2. Construye la lista de rutas a los archivos en el directorio objetivo.
3. Cifra cada archivo y sobrescribe su contenido con los datos cifrados.
4. Crea una nota de rescate `readme.txt` en el directorio objetivo con instrucciones.

**Ruta objetivo de ejemplo (Windows):**

```
C:\Users\<nombre_usuario>\Desktop\Ataque\Primera prueba
```

### Puntos clave del código

- **Importaciones:** `from cryptography.fernet import Fernet`, `os`, `getpass`.
- **`generarkey()`** — genera y escribe `key.key` (bytes).
- **`retornarkey()`** — lee `key.key` y devuelve la clave en bytes.
- **`encrypt(items, key)`** — instancia `Fernet(key)`; para cada archivo: lee bytes, cifra con `encrypt()` y sobrescribe.
- **Bloque principal:** obtiene el nombre de usuario con `getpass.getuser()`, construye rutas absolutas, ejecuta `generarkey()` + `retornarkey()` y llama a `encrypt()`. Finalmente crea `readme.txt`.

---

## Descripción de `Decrypt.py`

### Funcionamiento general

`Decrypt.py` simula la fase de recuperación:

1. Lee la clave de `key.key`.
2. Elimina la nota `readme.txt` (simulando que ya no es necesaria).
3. Enumera los archivos cifrados y los descifra, sobrescribiendo con el contenido original.

### Puntos clave del código

- **Importaciones:** `from cryptography.fernet import Fernet`, `os`, `getpass`.
- **`retornarkey()`** — lee y devuelve la clave desde `key.key`.
- **`decrypt(items, key)`** — instancia `Fernet(key)`; para cada archivo cifrado: lee bytes, descifra con `decrypt()` y sobrescribe con los datos descifrados.
- **Bloque principal:** define ruta objetivo (mismo directorio que `Encrypt.py`), elimina `readme.txt`, lista archivos, recupera la clave y ejecuta `decrypt()`.

---

## Flujo / Arquitectura del ejemplo

1. **Ejecución de `Encrypt.py`** — preparación e inicio del "ataque".
2. **Generación de clave** — `key.key` creada y almacenada localmente.
3. **Cifrado** — todos los archivos en el directorio objetivo son cifrados con la clave.
4. **Demanda de rescate** — se crea `readme.txt` con instrucciones.
5. **Recuperación** — con la clave (`key.key`) se puede recuperar todo ejecutando `Decrypt.py`.
6. **Descifrado** — `Decrypt.py` restaura los archivos.

---

## Uso (ejemplos)

### Ejecutar encrypt (prueba)

```bash
python Encrypt.py
```

- Genera `key.key` en el directorio del script.
- Cifra archivos en la ruta objetivo definida por el script.
- Crea `readme.txt` con la nota de rescate (simulada).

> **Advertencia práctica:** dado que el proyecto reproduce patrones de comportamiento detectables, **es probable que soluciones como Windows Defender identifiquen los binarios o scripts relacionados y los cuarentenicen/elimininen** durante las pruebas. Esto es normal y esperado: no intentes desactivar las protecciones del sistema en equipos reales. Si necesitas realizar pruebas más complejas por motivos de investigación defensiva, hazlo en entornos controlados y siguiendo políticas éticas y legales.

### Ejecutar decrypt (prueba)

```bash
python Decrypt.py
```

- Lee `key.key` (debe existir y ser la misma creada por `Encrypt.py`).
- Elimina `readme.txt`.
- Descifra los archivos en la ruta objetivo.

---

## Notas de seguridad y buenas prácticas

- **Nivel básico:** este repositorio es intencionalmente básico y didáctico; no pretende representar las técnicas avanzadas que usan actores reales.  
- **Entorno aislado:** realiza todas las pruebas en máquinas virtuales o entornos aislados sin acceso a redes o recursos compartidos.  
- **No usar en sistemas reales o de terceros.** El código representa comportamiento malicioso si se usa fuera de un laboratorio controlado.  
- **No intentes evadir antivirus:** no proporcione ni siga instrucciones para deshabilitar o evadir sistemas de detección. Si Windows Defender o tu antivirus elimina los ficheros, ese resultado confirma que las medidas funcionan correctamente.  
- **Auditoría y defensa:** utiliza este ejemplo únicamente con fines de aprendizaje defensivo — detectar, mitigar y responder ante ransomware.  
- **Respaldos:** asegúrate de contar con copias de seguridad antes de realizar cualquier prueba, incluso en entornos de laboratorio.

