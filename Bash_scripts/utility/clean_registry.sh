#!/usr/bin/env bash
# Логирование действий скрипта в syslog
exec > >(logger  -p local0.notice -t `basename "$0"`)
exec 2> >(logger  -p local0.error -t `basename "$0"`)
# Скрипт очистки локального Docker-registry развернутого в контейнере.
# Для работы скрипта необходимо передать два парамметра:
# $1 - project
# $2 - branch

project="$1"
branch="$2"
url_repo="https://registry_url.ru"

delete_list=$(curl -X GET ${url_repo}/v2/${progect}/tags/list | json_pp | grep ${branch} | sed -n "/[/,/]/p" | sed -r "s/[ ,\"]//g")

for l in ${delete_list[@]}; do
  manifests=$(curl -v --silent -H "Accept: application/vnd.docker.distribution.manifest.v2+json" -X GET "${url_repo}/v2/${progect}/manifests/${l}" 2>&1 | grep docker-content-digest | awk '{print$3}' | sed -r "s/sha256://")
  var_manifests=$(printf ${manifests} | sed -r "s/\r//")
  cmd_delete=$(curl -X DELETE "$url_repo/v2/$progect/manifests/sha256:$var_manifests")
done

#  docker exec -it registry.dev.smartseeds.ru bin/registry garbage-collect /etc/docker/registry/config.yml
