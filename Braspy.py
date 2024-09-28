import builtins
import math
import os
import sys

traducoes = {
    'print': 'imprimir',
    'input': 'entrada',
    'len': 'tamanho',
    'range': 'intervalo',
    'str': 'texto',
    'int': 'inteiro',
    'float': 'flutuante',
    'bool': 'booleano',
    'list': 'lista',
    'dict': 'dicionario',
    'set': 'conjunto',
    'tuple': 'tupla',
    'append': 'adicionar',
    'remove': 'remover',
    'pop': 'remover_ultimo',
    'sort': 'ordenar',
    'reverse': 'inverter',
    'copy': 'copiar',
    'update': 'atualizar',
    'keys': 'chaves',
    'values': 'valores',
    'items': 'itens',
    'open': 'abrir',
    'close': 'fechar',
    'read': 'ler',
    'write': 'escrever',
    'sum': 'soma',
    'max': 'maximo',
    'min': 'minimo',
    'abs': 'absoluto',
    'round': 'arredondar',
    'pow': 'potencia',
    'exec': 'executar',
    'eval': 'avaliar',
    'type': 'tipo',
    'isinstance': 'ehinstancia',
    'sorted': 'ordenado',
    'filter': 'filtrar',
    'map': 'mapear',
    'zip': 'zipar',
    'enumerate': 'enumerar',
    'reversed': 'invertido',
    'format': 'formatar',
    'split': 'dividir',
    'join': 'juntar',
    'strip': 'limpar',
    'replace': 'substituir',
    'upper': 'maiusculo',
    'lower': 'minusculo',
    'find': 'encontrar',
    'startswith': 'comeca_com',
    'endswith': 'termina_com',
    'isdigit': 'ehdigito',
    'isalpha': 'ehletra',
    'isalnum': 'ehalnum',
    'isspace': 'ehespaco',
    'os': 'so',
    'sys': 'sistema',
    'math': 'matematica',
    'sqrt': 'raiz_quadrada',
    'log': 'logaritmo',
    'cos': 'cosseno',
    'sin': 'seno',
    'tan': 'tangente',
    'pi': 'pi',
    'if': 'se',
    'else': 'senao',
    'elif': 'senaose',
    'for': 'para',
    'while': 'enquanto',
    'break': 'parar',
    'continue': 'continuar',
    'return': 'retornar',
    'in': 'em',
    'True': 'Verdadeiro',
    'False': 'Falso',
    'None': 'Nenhum',
    'and': 'e',
    'or': 'ou',
    'not': 'nao',
    '=': 'igual',
    '<': 'menor_que',
    '>': 'maior_que',
    '<=': 'menor_ou_igual',
    '>=': 'maior_ou_igual',
    '==': 'igual_a',
    '!=': 'diferente_de',
}

def traduzir(func):
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        if func_name in traducoes:
            print(f"Braspy: Função '{traducoes[func_name]}' chamada.")
        return func(*args, **kwargs)
    return wrapper

def traduzir_lambda(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

builtins.imprimir = traduzir(builtins.print)
builtins.entrada = traduzir(builtins.input)
builtins.tamanho = traduzir(len)
builtins.intervalo = traduzir(range)
builtins.texto = traduzir(str)
builtins.inteiro = traduzir(int)
builtins.flutuante = traduzir(float)
builtins.booleano = traduzir(bool)
builtins.lista = traduzir(list)
builtins.dicionario = traduzir(dict)
builtins.conjunto = traduzir(set)
builtins.tupla = traduzir(tuple)

builtins.adicionar = traduzir_lambda(lambda x, item: x.append(item))
builtins.remover = traduzir_lambda(lambda x, item: x.remove(item))
builtins.remover_ultimo = traduzir_lambda(lambda x: x.pop())
builtins.ordenar = traduzir_lambda(lambda x: x.sort())
builtins.inverter = traduzir_lambda(lambda x: x.reverse())
builtins.copiar = traduzir_lambda(lambda x: x.copy())
builtins.atualizar = traduzir_lambda(lambda x, y: x.update(y))
builtins.chaves = traduzir_lambda(lambda x: x.keys())
builtins.valores = traduzir_lambda(lambda x: x.values())
builtins.itens = traduzir_lambda(lambda x: x.items())

builtins.abrir = traduzir(open)
builtins.fechar = traduzir_lambda(lambda file: file.close())
builtins.ler = traduzir_lambda(lambda file: file.read())
builtins.escrever = traduzir_lambda(lambda file, content: file.write(content))

builtins.soma = traduzir(sum)
builtins.maximo = traduzir(max)
builtins.minimo = traduzir(min)
builtins.absoluto = traduzir(abs)
builtins.arredondar = traduzir(round)
builtins.potencia = traduzir(pow)

builtins.executar = traduzir(exec)
builtins.avaliar = traduzir(eval)
builtins.tipo = traduzir(type)
builtins.ehinstancia = traduzir(isinstance)
builtins.ordenado = traduzir(sorted)
builtins.filtrar = traduzir(filter)
builtins.mapear = traduzir(map)
builtins.zipar = traduzir(zip)
builtins.enumerar = traduzir(enumerate)
builtins.invertido = traduzir(reversed)

builtins.formatar = traduzir_lambda(lambda s, *args, **kwargs: s.format(*args, **kwargs))
builtins.dividir = traduzir_lambda(lambda s, sep=None: s.split(sep))
builtins.juntar = traduzir_lambda(lambda sep, iterable: sep.join(iterable))
builtins.limpar = traduzir_lambda(lambda s: s.strip())
builtins.substituir = traduzir_lambda(lambda s, old, new: s.replace(old, new))
builtins.maiusculo = traduzir_lambda(lambda s: s.upper())
builtins.minusculo = traduzir_lambda(lambda s: s.lower())
builtins.encontrar = traduzir_lambda(lambda s, sub: s.find(sub))
builtins.comeca_com = traduzir_lambda(lambda s, prefix: s.startswith(prefix))
builtins.termina_com = traduzir_lambda(lambda s, suffix: s.endswith(suffix))
builtins.ehdigito = traduzir_lambda(lambda s: s.isdigit())
builtins.ehletra = traduzir_lambda(lambda s: s.isalpha())
builtins.ehalnum = traduzir_lambda(lambda s: s.isalnum())
builtins.ehespaco = traduzir_lambda(lambda s: s.isspace())

builtins.so = traduzir_lambda(lambda: os)
builtins.sistema = traduzir_lambda(lambda: sys)
builtins.matematica = traduzir_lambda(lambda: math)
builtins.raiz_quadrada = traduzir(math.sqrt)
builtins.logaritmo = traduzir(math.log)
builtins.cosseno = traduzir(math.cos)
builtins.seno = traduzir(math.sin)
builtins.tangente = traduzir(math.tan)
builtins.pi = traduzir(lambda: math.pi)