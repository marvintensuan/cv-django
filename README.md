# Curriculum Vitae Django Project

## Overview

_My very own professional website which I can customize at my whim._

__Tech Stack__: Django, Google Cloud Platform (Cloud Run, Cloud SQL, Cloud Storage, Secrets Manager), PostgreSQL, HTML, CSS, Bootstrap

This is for my [CV website](https://www.marvintensuan.com). For my portfolio, visit https://marvintensuan.github.io.

## Django on Cloud Run

Initial build for this website is heavily guided by [__Katie McLaughlin (@glasnt)__'s Google codelab](https://codelabs.developers.google.com/codelabs/cloud-run-django/). Anyone who would follow instructions in this codelab should be able to build a working Django project with a default landing page.

I have modified the project with the help of [__Coding For Entrepreneur__'s Django Course](https://www.youtube.com/watch?v=F5mRW0jo-U4) as well as the of [__Official Django docs__](https://docs.djangoproject.com/en/3.1/).

## Beyond the codelab

Some key tasks for after finishing the codelab:

- Mapping custom domain
- Modifying Django Project (creating models, creating migration files, registering to admin site) and [related issue](https://stackoverflow.com/questions/6893988/app-or-model-not-showing-up-in-django-admin).
- Setting up Cloud SQL Proxy.

## History

2020-11-03 &mdash; transferred domain from Squarespace to GoDaddy.

2020-11-08 &mdash; created repo `marvintensuan.github.io`.

2020-11-18 &mdash; on repo `marvintensuan.github.io`, diverted the use of `master` branch from `gh-pages`. [See commit 6885ef7](https://github.com/marvintensuan/marvintensuan.github.io/commit/6885ef7014063b3c7b0fb32d6d5f1545cf578e85).

2020-11-22 &mdash; started my Google Cloud Platform Free Trial.

2020-12-07 &mdash; finally mapped my domain from GoDaddy to Cloud Run.

2020-12-22 &mdash; converted from vanilla CSS to Bootstrap CDN.

2020-12-27 &mdash; created this GitHub repository `cv-django`. Former repo will be repurposed to instead host portfolio. This repository will contain actual files from the Cloud Run container.

2020-12-30 &mdash; manually updated database. [See commit d24bd90
](https://github.com/marvintensuan/marvintensuan.github.io/commit/d24bd90d5cc493a91b2c30a30ca2a898175342ba).

2021-01-03 &mdash; converted to Bootsrap 4.

2021-02-03 &mdash; started Flask app. [See commit 9264491
](https://github.com/marvintensuan/cv-django/commit/9264491c73cb7be338337bc162bd46c7ab24aa3e#diff-255d345f1b134dc6c02f4113e913d16662d5b5a6fca7c3c8c58f0156954fcaaa)

2021-02-07 &mdash; deployed Flask app. [URL](https://cv-flask-img-nwpr6gpcxa-de.a.run.app/) | [commit 6c5f336](https://github.com/marvintensuan/cv-django/commit/6c5f3366957cab83d058537ceb883aed981053a5)