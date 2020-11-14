# examples
Examples of various scripts

Chapter - Ansible
Содержит примеры play-books для Ansible.
1. install_prometheus
    ├── hosts - (Пример с именем сервера на котором разворачивал сервис.)
    └── prometheus.yml (Play-book развертки Prometheus на любом хосте к которому у нас есть доступ по ssh.)
  Перейти в директорию в которую положили два файла hosts и prometheus.yml, в файл хост внести имя хоста, на котором хотим развернуть сервис. Предварительно перед запуском необходимо отредактировать файл prometheus.yml
  hosts: (вписать имя своего хоста)
  vars: (изменить значения переменных на свое усмотрение)
  Например:
  - service_prom: (указать желаемое имя сервиса)
  - vprom: (указать необходимую версию - которую можно узнать на сайте https://prometheus.io)
  - user_prom: (указать пользователя от имени которого будет запускаться и работать сервис)
  Пример запуска  $ ansible-playbook prometheus.yml -i host
