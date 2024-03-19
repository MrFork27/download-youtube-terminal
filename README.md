# download-youtube-terminal
Terminal para descargar vídeos y audios de vídeos a partir de YouTube.

## Instalación

Para instalar todas las librerías a partir del fichero `requirements.txt`:

```shell
pip install -r requirements.txt
```

## Uso

```shell
usage: [-h] [-u URL]

Command line application to download youtube video and audios.

options:
 -h, --help                       Show this help message and exit
 -a [URL], --audio [URL]          Download audio video and exit
 -v [URL], --video [URL]          Download video and exit
```

## Ejemplo de uso

Para descargar el audio de un vídeo de YouTube cuya URL es `https://www.youtube.com/watch?v=XFkzRNyygfk`:

```shell
python src/main.py -a https://www.youtube.com/watch?v=XFkzRNyygfk

python src/main.py --audio https://www.youtube.com/watch?v=XFkzRNyygfk
```

> El audio se descargará en la carpeta /music

Para descargar un vídeo de YouTube cuya URL es `https://www.youtube.com/watch?v=XFkzRNyygfk`:

```shell
python src/main.py -v https://www.youtube.com/watch?v=XFkzRNyygfk

python src/main.py --video https://www.youtube.com/watch?v=XFkzRNyygfk
```

> El vídeo se descargará en la carpeta /video

## Testing

- Ejecuta las pruebas del fichero test:

```shell
python -m unittest test
```

- Ejecuta las pruebas del ficheor test en modo verbose:

```shell
python -m unittest -v test
```

- Ejecuta las pruebas de todos los ficheros llamados `test*.py`:

```shell
python -m unittest discover
```

- Ejecuta las pruebas de todos los ficheros llamados `test*.py` que se encuentran en el directorio `tests`:

```shell
python -m unittest discover -s tests
```

- Ejecuta las pruebas de todos los ficheros llamados `test*.py` que se encuentran en el subdirectorio `src/`:

```shell
python -m unittest discover -s tests -t src
```

### Referencias

- [Testing](https://realpython.com/python-testing/)
- [urllib.error.URLError en Mac](https://stackoverflow.com/questions/68275857/urllib-error-urlerror-urlopen-error-ssl-certificate-verify-failed-certifica)
