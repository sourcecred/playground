---
layout: page
title: About
description: About the SourceCred Playground
permalink: /about/
---

<img class="center padded" src="{{ site.url }}{{ site.baseurl }}/assets/img/logo/logo.png">

Welcome to the SourceCred Playground! As we develop our [documentation](https://github.com/sourcecred/docs) around the community culture, and contributing, there is a strong
need for learning resources. One of these resources is learning to use GitHub.
While it's not essential to use GitHub to participate in SourceCred, it can
be a lot of fun, and this playground [repository](https://github.com/sourcecred/playground) 
and associated portal is provided to help you to learn.

### How does it work?

The playground is set up to provide you with a set of challenges. The number,
order, and detail of your contribution is up to you, however each will walk
you through:

 - forking and cloning the playground GitHub repository
 - checking out a new branch to work on your changes
 - committing, pushing, and opening a pull request
 - participating in your first review as a contributor!

### How do I get started?

Let's get you on your way to doing a challenge! You can browse the challenges below.
Please [reach out](#reach-out) if you need any help, or have any questions.

<br>

{% for challenge in site.challenges %}<div class="card">
<h4>{{ challenge.title }}</h4>
{{ challenge.content }}
</div>{% endfor %}

### Get in Contact

There are several ways to get in contact with the community to ask a question, or get
help on your journey ahead!

 - [Discourse](https://discourse.sourcecred.io/) is a place where you can write up a more thoughtful question.
 - [Discord](https://sourcecred.io/discord-invite) has a `#github-help` channel intended for this use case.
 - [Tweet](https://twitter.com/sourcecred) sourcecred to publicly correspond.
 - [GitHub Issues](https://github.com/sourcecred/playground/issues) is like a GitHub-centric forum for asking questions, and you can link directly to content of the playground repository.
