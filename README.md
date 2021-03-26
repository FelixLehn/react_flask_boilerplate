# Set Up Development and Production Environment for the application
Zum Installieren und Ausführen der Applikation sind folgende Voraussetzungen zu treffen: 
- Installieren von Docker und docker command 
- Installation von git und git command 

## Development environment
Das Aufsetzen der Development Umgebung ist durch docker-compose vereinfacht worden. 

Installationsschritte:
1. Den Git-Branch master pullen: 
```
git clone https://code.eu.idealo.com/scm/condev/import-hub.git
```
2. 
```
docker-compose -f docker-compose-dev.yml up --build 
```


und fertig. Öffne den Browser und erhalte mit folgenden Urls die Komponenten: 

| Url | Description |
| --------| :--------:|
| localhost:3000| Frontend |
| localhost:5000| Backend Api with the url as /api |
| localhost:8080| Airflow Komponente |
| localhost:5555| Airflow Flower Komponente|
| localhost:8080/health| health check der docker container von Airflow| 

Um mit den Datenbanken der Applikation in Verbindung zu treten ist eine DataGrip Connection eingerichtet. Dafür müssen folgende Schritte eingehalten werden: 

1. Schritt
Installiere das Docker Package für DataGrip https://www.jetbrains.com/help/datagrip/docker.html
2. Erstelle eine Connection zu einer PostgresDatenbank mit folgenden Komponenten: 

| Attribut | Wert|
| ------| ------|
| Host | 0.0.0.0| 
| Port | 5432| 
| User | postgres| 
| passsword | postgres|
| Tabelle | airflow |

Test die Connection und hoffe auf ein grünes Häckchen. 
Sobald die Connection eingerichtet ist, können die Datenbankeinträge über die Tabelle airflow eingesehen werden. 

## Production Environment
Das Aufsetzen der Production Umgebung ist durch docker-compose vereinfacht worden. Es müssen aber die Änderungen im Frontend separat erstellt werden, damit die Production Umgebung auf die neuen veränderten static-files zugreifen kann. 

Führe dafür folgendes aus:

```
cd frontend
npm run build 
```
Nachdem dies erfolgt ist, können die Container und Images wie gewohnt mit docker-compose aufgerufen werden.

```
docker-compose up airflow-init
docker-compose up
```

und fertig. Öffne den Browser und erhalte mit folgenden Urls die Komponenten: 

| Url | Description |
| --------| :--------:|
| localhost:5000| Frontend |
| localhost:5000| Backend Api with the url as /api |
| localhost:8080| Airflow Komponente |
| localhost:5555| Airflow Flower Komponente|
| localhost:8080/health| health check der docker container von Airflow| 

Um mit den Datenbanken der Applikation in Verbindung zu treten ist eine DataGrip Connection eingerichtet. Dafür müssen folgende Schritte eingehalten werden: 

1. Schritt
Installiere das Docker Package für DataGrip https://www.jetbrains.com/help/datagrip/docker.html
2. Erstelle eine Connection zu einer PostgresDatenbank mit folgenden Komponenten: 

| Attribut | Wert|
| ------| ------|
| Host | 0.0.0.0| 
| Port | 55002| 
| User | postgres| 
| passsword | postgres|
| Tabelle | airflow |

Test die Connection und hoffe auf ein grünes Häckchen. 
Sobald die Connection eingerichtet ist, können die Datenbankeinträge über die Tabelle airflow eingesehen werden. 

# Kubernetes
Setze ein Minikube Cluster mit namespace airflow auf.

```
minikube start
kubectl create namespace airflow 
```

## Airflow
Wir benutzen einen Helm-Chart für Airflow.

```
helm repo add airflow-stable https://airflow-helm.github.io/charts  
helm repo update  
helm show values airflow-stable/airflow > custom-values.yaml     
helm install airflow airflow-stable/airflow --namespace airflow --values ./custom-values.yaml
```
Überprüfe: 
````
kubectl get pods -n airflow
````

Wenn die airflow Komponenten erstellt wurden, kann man airflow mithilfe von minikube öffnen:

```
minikube service <airflow-web-service>
```

## Web-Komponenten erstellen

Führe folgenden Befehl aus:

```
kubectl apply -f kubernetes -n airflow 
```

Checke mithilfe 
```
kubectl get pods -n airflow
```

Erhalte Zugriff auf Komponenten 
```
minikube service <client-service>
```
