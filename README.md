# download-youtube-terminal
Terminal para descargar audios a partir de vídeos de YouTube

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

### Referencia

- https://realpython.com/python-testing/

## urllib.error.URLError en Mac

- https://stackoverflow.com/questions/68275857/urllib-error-urlerror-urlopen-error-ssl-certificate-verify-failed-certifica
