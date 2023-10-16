GISTS API proxy
=========

Build an API, test it, and package it into a container
-------------------
* Build a simple HTTP API in any general purpose programming language
  that interacts with the GitHub API and responds to requests 
  on /<USER> with a complete list of the user’s publicly available Gists.
* Create an automated test to validate that the API works. An example 
  user to use as test data is `octocat`.
* Package the API into a docker container that listens for requests
  on port `8080`. You do not need to publish the resulting container 
  image in any container registry, but we are expecting the Dockerfile
  in the submission.
* The solution may optionally provide other functionality or tests 
  but the above must be implemented.

Instruction
---------
A makefile is provided to run the tests and build the docker container

`make test`

`make docker-build`

`make docker-run`
