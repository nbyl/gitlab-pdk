# local pipeline development

## Vorrausetzungen

* skopeo
* minishift

## Projekt vorbereiten

* minikube/minishift starten
* Projekt für pipeship erstellen oder auschecken
* pipeline.yaml per Symlink reinlinken: `ln -s  ../ideal-standard-becken/pipeline.yaml .gitlab-ci.yml`

## Images lokal bereitstellen

* herunterladen in Verzeichnis mit skopeo
* in lokalen Docker Daemon kopieren mit skopeo

## Jobs lokal ausführen

* `pdk run build_container_image`
  * KUBECONFIG setzen
  * ~/.kube/config mounten
  * Variablen für Artifactory überschreiben
  * pull-policy never
