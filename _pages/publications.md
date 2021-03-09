---
layout: archive
title: "Publications"
permalink: /publications/
author_profile: true
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}
{% include toc %}

## PhD Thesis

{% for post in site.publications reversed %}
  {% if post.etype == 'mastersthesis' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}


## Articles

{% for post in site.publications reversed %}
  {% if post.etype == 'article' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Conferences

{% for post in site.publications reversed %}
  {% if post.etype == 'conference' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

## Miscelanous

{% for post in site.publications reversed %}
  {% if post.etype == 'presentation' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
  {% if post.etype == 'unpublished' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
  {% if post.etype == 'misc' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}

{% for post in site.publications reversed %}
  {% if post.etype == 'techreport' %}
    {% include archive-single.html %}
  {% endif %}
{% endfor %}