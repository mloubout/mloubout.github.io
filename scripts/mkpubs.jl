using BibTeX

base="https://slim.gatech.edu/biblio/export/bibtex?f%5Bauthor%5D=1&f%5Btype%5D="

keys = [102, 103, 135, 103, 124]
types = ["Journals", "Conferences", "Presentations", "TechReports", "Unpublished"]


rules = Dict("{ \\textquoteright }"=> "'", "{ \\textquoteleft }"=> "'", " , "=> ", ", " ' s"=> "' s",
             "{ \\textquotedblleft }"=>"\"", "{ \\textquotedblright }"=>"\"")

for (k, t) in zip(keys, types)
    bibname = "$(lowercase(t)).bib"
    download("$(base)$k", "./content/pubs/$(bibname)")

    _, b = open("./content/pubs/$(bibname)", "r") do file
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
    entries = [] 
    for (k, v) in b
        abstract = get(v, "abstract", nothing)
        if isnothing(abstract)
            continue
        end
        abstract = replace(abstract, rules...)
        url = try
            doi = v["doi"]
            "https://doi.org/$(doi)"
        catch KeyError
            get(v, "url", nothing)
        end
        link = isnothing(url) ? "" : "[Link]($(url))"
        entry = """
## $(v["title"])

@$(k)  $(link)

::: {.callout-note collapse="true"}
# Abstract

$(abstract)
:::

"""
        push!(entries, (get(v, "year", 0), entry))
    end

    # Sort by year
    sort!(entries, by=first, rev=true)
    
    years = unique(first.(entries))
    split = [[e for e in entries if e[1] == y] for y in years]

    for (y, s) in zip(years, split)
        content = "$(content) \n# $(y) \n"
        for e in s
            content = "$(content) \n$(e[2])"
        end
    end

    write("content/pubs/$(t).qmd", content)
end

