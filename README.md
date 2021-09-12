# Techtrends

[![Deploy artifact to hub.docker.com](https://github.com/guillermo-ampie/techtrends/actions/workflows/techtrends-dockerhub.yml/badge.svg)](https://github.com/guillermo-ampie/techtrends/actions/workflows/techtrends-dockerhub.yml)

## Project Overview

This project showcases the use of several CI/CD tools and Cloud services applied to automate the deployment of a sample Flask application (provided) into a Kubernetes cluster

### Introduction

This project "operationalize" a sample [Flask](https://flask.palletsprojects.com/) application [TechTrends](./techtrends/app.py) deployed into a [Kubernetes](https://kubernetes.io/)(K8S) cluster built with [K3S](https://k3s.io/).

The [TechTrends](./techtrends)  applications is a monolithic app, that is containerized using [Docker](https://www.docker.com/) and deployed into a Kubernetes cluster; which is installed in a [Vagrant Box](https://www.vagrantup.com/) (this virtual machine uses [OpenSUSE](https://www.opensuse.org/))

#### CI/CD Approach

Using a CI pipeline and CD tools, all the steps to build and deploy the application in the Kubernetes cluster are fully automated.

## CI/CD Tools and Cloud Services

1. A pipeline deployed in [GitHub Actions](https://github.com/features/actions) builds the container image and deploys it to [DockerHub](https://hub.docker.com/)

2. Then, using [ArgoCD](https://argoproj.github.io/cd) the app is deployed into two namespaces in the Kubernetes cluster:
    * [Helm](https://helm.sh/) is used to write the application configuration templates

### GitHub Actions Variables

You need to setup the following variables in your GitHub repo to configure your GitHub Actions pipeline:

* DOCKERHUB_USERNAME: your Docker hub username
* [DOCKERHUB_TOKEN](https://www.docker.com/blog/docker-hub-new-personal-access-tokens/): to authenticate into DockerHub

## Main Files

* Several Makefiles are provides for your convenience for specific groups of tasks:

  * To manage the Vagrant Box: [./Makefile.vagrant](./Makefile.vagrant)

  * To setup/install the python environment for local: development, test, and Docker management: [./Makefile](Makefile)

  * To install all the dependencies in the Vagrant Box (OpenSUSE): [./suse_box/Makefile](./suse_box/Makefile)

  * To manually deploy all the Kubernetes resources in the Vagrant Box: [./kubernetes/Makefile](./kubernetes/Makefile)

  * To deploy the application using ArgoCD: [./argocd/Makefile](./argocd/Makefile)

* GitHub Actions configuration file: [techtrends-dockerhub.yml](.github/workflows/techtrends-dockerhub.yml)

* ArgoCD application definition files: [helm-techtrends-prod.yaml](argocd/helm-techtrends-prod.yaml), [helm-techtrends-staging.yaml](argocd/helm-techtrends-staging.yaml)

* Helm Chart and related files: [Chart.yaml](helm/Chart.yaml) and [helm files](helm)

* Kubernetes declarative files: [kubernetes](kubernetes)

* TechTrends application: [techtrends](techtrends)

* Container definition file: [Dockerfile](Dockerfile)

* Vagrant Box definition file: [Vagrantfile](Vagrantfile)
