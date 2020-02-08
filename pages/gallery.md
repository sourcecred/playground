---
layout: gallery
title: Gallery
description: A collection of posts, organized by year
permalink: /gallery/
---

{% include scrolltop.html %}
<section class="gallery">
  <div class="row" id="message"></div> 
    <div class="row">
      <ul>{% for meme in site.data.gallery %}
	<li><a data-title="{{ meme.alt }}" target="_blank" href="{% if meme.url %}{{ meme.url }}{% else %}#item{{ forloop.count }}{% endif %}">
       <img class="meme" src="{% if meme.image %}{{ site.url }}{{ site.baseurl }}/assets/gallery/{{ meme.image }}{% else %}{{ meme.external }}{% endif %}" alt="{{ meme.alt }}">
        </a>
       </li>{% endfor %}
       </ul>
   </div>
</section>

