# Techtrends

[![Deploy artifact to hub.docker.com](https://github.com/guillermo-ampie/techtrends/actions/workflows/techtrends-dockerhub.yml/badge.svg)](https://github.com/guillermo-ampie/techtrends/actions/workflows/techtrends-dockerhub.yml)

## Project Overview

This project showcases the use of several CI/CD tools and Cloud services employed to automate the deployment of a sample Flask application (provided) into a Kubernetes cluster.

## Introduction

This project operationalizes a sample [Flask](https://flask.palletsprojects.com/) application [TechTrends](./techtrends/app.py) deployed into a [Kubernetes](https://kubernetes.io/)(K8S) cluster built with [K3S](https://k3s.io/).

The [TechTrends](./techtrends)  applications is a monolithic app, that is containerized using [Docker](https://www.docker.com/) and deployed into a Kubernetes cluster. The K8S cluster is installed in a [Vagrant Box](https://www.vagrantup.com/) (this virtual machine uses [OpenSUSE](https://www.opensuse.org/)).

## CI/CD Approach

All the steps to build and deploy the application into the Kubernetes cluster are fully automated using a CI pipeline and CD tools.

### Project Workflow

1. A pipeline deployed in [GitHub Actions](https://github.com/features/actions) builds the container image and deploys it to [DockerHub](https://hub.docker.com/)

2. Then, using [ArgoCD](https://argoproj.github.io/cd) the app is deployed into two namespaces in the Kubernetes cluster:
    * [Helm](https://helm.sh/) is used to write the application configuration templates

## CI/CD Tools and Cloud Services

* [Docker](https://www.docker.com/) -  Platform as a service products that use OS-level virtualization to deliver software in packages called containers
* [Docker Hub](https://hub.docker.com) - Container images repository service
* [Kubernetes](https://kubernetes.io/) - System for automating deployment, scaling, and management of containerized applications
* [K3S](https://k3s.io/) -  Lightweight Kubernetes distribution
* [Vagrant](https://www.vagrantup.com/) - Tool for building and managing virtual machine environments
* [GitHub Actions](https://github.com/features/actions) - Cloud-based CI/CD service
* [ArgoCD](https://argoproj.github.io/cd) - GitOps Continuous Delivery tool for Kubernetes
* [Helm](https://helm.sh/) - Application package manager for Kubernetes

### GitHub Actions Variables

Set up the following variables in the GitHub repo to configure the GitHub Actions pipeline:

* DOCKERHUB_USERNAME: the Docker Hub username
* [DOCKERHUB_TOKEN](https://www.docker.com/blog/docker-hub-new-personal-access-tokens/): to authenticate into DockerHub

## Main Files

* Several Makefiles are provides as a convenience for specific groups of tasks:

  * To manage the Vagrant Box: [./Makefile.vagrant](./Makefile.vagrant)

  * To setup/install the python environment for local development, test, and also Docker management: [./Makefile](Makefile)

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
