### Docker Environment

To run the Docker container, ensure that you have docker desktop installed on your computer. You may do so [here](https://www.docker.com/get-started/). 

If you are using mac and docker isn't recognized in visual studio code or your terminal after you already installed the app then you need to add it to your PATH. First, try to see if your terminal picks up docker:

```
docker info
```

If it is unrecognized, You can add it to your path with the following command:

```
echo 'export PATH="/Applications/Docker.app/Contents/Resources/bin:$PATH"' >> ~/.zprofile
source ~/.zprofile
```

1) Open the project in VSCode

2) Click ```CMD + Shift + P``` and then choose the option that says "Dev Containers: Rebuild and Reopen in Container"

3) if you do not see the option from step 2, you need to download the extension for running docker dev containers. Here are the extensions on VSCode:

    - [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
    - [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker)