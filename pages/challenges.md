---
title: Challenges
permalink: /challenges/
---

<div class="container">
  {% for challenge in site.challenges %}
    <div class="card row" style="padding-top:20px">
      <a href="{{ site.url }}{{ site.baseurl }}{{ challenge.url }}">{{ challenge.title }}</a>
      {% include challenge-badge.html %}
   </div>
  {% endfor %}
</div>

