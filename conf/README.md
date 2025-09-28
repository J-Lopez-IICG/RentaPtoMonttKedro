## Instructions

### Configuración de `msedgedriver.exe`

Para que el proyecto pueda realizar web scraping, es necesario descargar el controlador para Microsoft Edge.

1.  **Verifica tu versión de Microsoft Edge**: Abre Edge, ve a `Configuración` > `Acerca de Microsoft Edge` y anota el número de la versión.
2.  **Descarga el controlador**: Ve a la [página oficial de Microsoft Edge Driver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) y descarga la versión que corresponda a tu navegador.
3.  **Ubica el archivo**: Descomprime el archivo y coloca `msedgedriver.exe` dentro de la carpeta `driver/` en la raíz del proyecto. El código está configurado para buscar el driver en esta ubicación, por lo que no necesitas añadir la ruta en los archivos de configuración.