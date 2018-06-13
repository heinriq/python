# quake_log_parser
Analisador de Log baseado em um log real do jogo Quake

**Projeto roda em Python>=3.4**

## Instalção

Crie um ambiente virtual! (use ``virtualenvwrapper``):

```
$ mkvirtualenv quake_log_parser
```

Instale uns requisitos:

```
$ make requirements
```

## Rodas os teste

Cobertura de testes completa:

```
$ make test
```

Testar função ou classe especifica:

```
$ make test-matching test=TestTask1
```

## How to: Executar o código


### Ajuda!!

```
$ python run.py --help
```

### Rodar o modo verbose

```
$ python run.py -f games.log -v
```

### Rodar o Report Mode

```
$ python run.py -f games.log -r
```

### Mostrar no modo report as armas usadas no jogo

```
$ python run.py -f games.log -r -p
```

