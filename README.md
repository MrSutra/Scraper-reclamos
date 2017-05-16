# Scraper-reclamos

Se debe instalar previamente Scrapy:

```
$ pip install scrapy
```

Para correr el scraper

```
$ scrapy crawl reclamos
```

se puede añadir la opción -o para guardar los datos en un archivo y la opción FEED_EXPORT_ENCODING para que la salida tenga un encode en especial. De preferencia utilizar utf-8. Ej:

```
$ scrapy crawl reclamos -o output.json -s FEED_EXPORT_ENCODING='utf-8'
```

para correr el scraper de forma menos verbosa

```
$ scrapy crawl reclamos -s LOG_ENABLED=False
```
