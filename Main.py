#!/usr/bin/env python
# *-* coding:utf-8 *-*

import htmlgen
from htmlgen import Route, HTMLContent

html = HTMLContent()
rout = Route()

# Criando paginas com HTMLContent
html.create("html", lang="pt-BR") # Inicia com a tag html
# Como o método retorna a propria classe
# podesse continuar a criação e implementação
# dos componentes continuamente
html.create("head").create("title").innerHTML("Page Generator").close()
html.close() # como a linha de cima já fechou a tag "title", esse cloco fecha a tag "head"

# Caso tenha acentos na palavra, é viavem inserir uma string unicode
html.create("body").create("h1").innerHTML(u"Aplicação feito com ").create("span",style="color: green;").innerHTML("HTMLGen").close().close().close()

# Este comando fecha todas as tags ainda abertas
html.end_page()

# Para retornar a pagina, basta digitar get_page
print "Pagina criada com HTMLGen"
print html.get_page()
print "------------------------------------"

# Recolhendo paginas com Route
# É preciso passar o nome da pagina, caminho e um apelido
rout.new_route("pagina_teste.html","html/","pagina")

print "Pagina recolhida por Route"
# O apelido será usado para carregar a pagina nesse block
print rout.call("pagina")
