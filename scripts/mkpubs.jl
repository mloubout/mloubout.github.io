using BibTeX

base="https://slim.gatech.edu/biblio/export/bibtex?f%5Bauthor%5D=1&f%5Btype%5D="

keys = [102, 103, 135, 103, 124]
types = ["Journals", "Conferences", "Presentations", "TechReports", "Unpublished"]


rules = Dict("{ \\textquoteright }"=> "'", "{ \\textquoteleft }"=> "'", " , "=> ", ", " ' s"=> "' s",
             "{ \\textquotedblleft }"=>"\"", "{ \\textquotedblright }"=>"\"")

for (k, t) in zip(keys, types)
    bibname = "$(lowercase(t)).bib"
    download("$(base)$k", "./pubs/$(bibname)")

    _, b = open("./pubs/$(bibname)", "r") do file
        parse_bibtex(read(file, String))
    end
    content = """
---
title: "$(t)"
bibliography: $(bibname)
callout-icon: false
nocite: |
  @*
---

"""
    for (k, v) in b
        abstract = get(v, "abstract", nothing)
        if isnothing(abstract)
            continue
        end
        abstract = replace(abstract, rules...)
        url = get(v, "doi", get(v, "url", nothing))
        link = isnothing(url) ? "" : "[Link]($(url))"
        entry = """
## $(v["title"])

@$(k)  $(link)

::: {.callout-note collapse="true"}
# Abstract

$(abstract)
:::

"""
        content = "$(content)$(entry)"
    end
    write("pubs/$(t).qmd", content)
end

