# Scraper-reclamos

Se debe instalar previamente Scrapy:

```
$ pip install scrapy
```

Para correr el scraper

```
$ scrapy crawl reclamos
```

se puede añadir la opción -o para guardar los datos en un archivo. Ej:

```
$ scrapy crawl reclamos -o output.json
```

para correr el scraper de forma menos verbosa

```
$ scrapy crawl reclamos -s LOG_ENABLED=False
```
