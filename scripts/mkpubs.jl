using BibTeX
using Downloads


"""Return a normalized external URL for one bibliography entry."""
function entry_url(fields)
    doi = get(fields, "doi", nothing)
    if !isnothing(doi)
        doi_text = string(doi)
        return startswith(doi_text, "http") ? doi_text :
               "https://doi.org/$(doi_text)"
    end
    return get(fields, "url", nothing)
end


"""Create the Quarto markup and sorting metadata for one publication."""
function build_entry(citation_key, fields, replacement_rules)
    title = string(get(fields, "title", "Untitled publication"))
    year = string(get(fields, "year", "Undated"))
    numeric_year = something(tryparse(Int, year), -1)
    url = entry_url(fields)
    citation_line = isnothing(url) ? "@$(citation_key)" :
                    "@$(citation_key)  [Link]($(url))"
    abstract = get(fields, "abstract", nothing)
    abstract_block = ""
    if !isnothing(abstract) && !isempty(strip(string(abstract)))
        clean_abstract = replace(string(abstract), replacement_rules...)
        abstract_block = """

::: {.callout-note collapse="true"}
# Abstract

$(clean_abstract)
:::
"""
    end

    markup = """
## $(title)

$(citation_line)
$(abstract_block)
"""
    return (
        year=year,
        numeric_year=numeric_year,
        title=lowercase(title),
        markup=markup,
    )
end


"""Generate one styled publication archive from its exported BibTeX."""
function generate_category(category, base_url, replacement_rules)
    bib_path = joinpath(
        "content",
        "pubs",
        "$(lowercase(category.filename)).bib",
    )
    source_url = "$(base_url)$(category.type_id)"
    Downloads.download(source_url, bib_path)

    bibliography = open(bib_path, "r") do file
        _, parsed_bibliography = parse_bibtex(read(file, String))
        parsed_bibliography
    end
    entries = [
        build_entry(key, fields, replacement_rules)
        for (key, fields) in bibliography
    ]
    sort!(entries, by=entry -> (-entry.numeric_year, entry.title))

    output = IOBuffer()
    write(
        output,
        """---
title: "$(category.title)"
subtitle: "$(category.subtitle)"
bibliography: $(basename(bib_path))
callout-icon: false
toc-depth: 1
body-classes: publication-list-page
nocite: |
  @*
---

""",
    )
    for year in unique(entry.year for entry in entries)
        write(output, "# $(year)\n\n")
        for entry in filter(item -> item.year == year, entries)
            write(output, entry.markup)
        end
    end
    qmd_path = joinpath("content", "pubs", "$(category.filename).qmd")
    output_text = rstrip(String(take!(output))) * "\n"
    write(qmd_path, output_text)
end


"""Update all publication categories from the SLIM bibliography service."""
function main()
    base_url = "https://slim.gatech.edu/biblio/export/bibtex" *
               "?f%5Bauthor%5D=1&f%5Btype%5D="
    categories = [
        (
            type_id=102,
            filename="Journals",
            title="Journals",
            subtitle="Peer-reviewed journal articles",
        ),
        (
            type_id=103,
            filename="Conferences",
            title="Conferences",
            subtitle="Conference papers and extended abstracts",
        ),
        (
            type_id=135,
            filename="Presentations",
            title="Presentations",
            subtitle="Invited talks, workshops, and conference presentations",
        ),
        (
            type_id=109,
            filename="TechReports",
            title="Technical Reports",
            subtitle="Reports, preprints, and other research outputs",
        ),
        (
            type_id=124,
            filename="Unpublished",
            title="Unpublished",
            subtitle="Unpublished manuscripts and research notes",
        ),
    ]
    replacement_rules = (
        "{ \\textquoteright }" => "'",
        "{ \\textquoteleft }" => "'",
        " , " => ", ",
        " ' s" => "'s",
        "{ \\textquotedblleft }" => "\"",
        "{ \\textquotedblright }" => "\"",
    )

    for category in categories
        generate_category(category, base_url, replacement_rules)
    end
end


main()
