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