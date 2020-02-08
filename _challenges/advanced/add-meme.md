---
layout: challenge
title: "Meme Contribution"
author: "@vsoch"
date: 2020-02-07 1:20:00
resources:
 - name: SourceCred Documentation
   url: github.com/sourcecred/docs/
 - name: SourceCred
   url: github.com/sourcecred/sourcecred
 - name: SourceCred Discord
   url: https://sourcecred.io/discord-invite
 - name: SourceCred Discourse
   url: https://discourse.sourcecred.io/
---

<br>

For this challenge, you should add a meme to the gallery by way of adding
an entry to the <a href="https://github.com/sourcecred/playground/blob/master/_data/meme.yml)
data file">meme.yml</a> data file.

<br>

 - **image**: the filename in the "assets/gallery" folder. This is a relative path! We store images on the server as hosting external content is likely to result in eventual 404 (not found).
 - **url**: a meaningful url associated with the meme. In the example above, the meme is a joke about skipping testing, and so the link goes to a page with testing best practices. If you choose, you can even write an [associated post]({{ site.url }}{{ site.baseurl }}/challenge/intermediate/add-written-post/) (another challenge) to make your contribution more interesting.
 - **alt** is used as the "alernate" for the image (what is shown if the browser can't render the image) but also what we should when a user mouses over the image. This should be a short, meaningful description that describes both the meme and hints at the content at the associated url.

<br>

Use the links below to help with your introduction
to GitHub and git, and to interact with others in the community if you have any
questions.
