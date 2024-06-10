CopyHero
========
<a href="https://copyhero.net"><img height="80px" width="80px" src="images/favicon.webp"
align="left" hspace="10" vspace="6"></a>

**CopyHero Open Source Version** can easily copy text from images. It is easy to integrate into the website or software through Javascript SDK.CopyHero's OCR is based on [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR).It's completely **free**.

How CopyHero works for you
--------------------------
If your website or software users are the following, it is recommended to integrate CopyHero.

1. Website or software for students and educators: extract text from textbooks, handouts, PPT and other images to facilitate note organization and study research.

1. Website or software for researchers and scholars: extract text from papers, documents, and book scans to facilitate quick citation and organization of materials.

1. Website or software for office workers: quickly extract text for editing and analysis when processing image files such as charts, reports, and contracts.

1. Website or software for developers and programmers: extract code snippets or text content from screenshots, documents, and design drawings to improve work efficiency.

1. Website or software for freelancers and content creators: extract text from various image materials for creation, translation, writing, and content editing.

1. Website or software for people with visual impairments: extract text from images and convert them into text formats that can be recognized by screen readers to improve the convenience of information acquisition.

1. Website or software for language learners: extract text from foreign language text in images to facilitate translation and language learning.

1. Website or software for practitioners in the legal and financial industries: extract text from scanned copies of contracts, agreements, financial statements, etc. to improve work efficiency and accuracy.


## 1 Deploy CopyHero Server

There are two modes for deploying CopyHero Server, namely docker deployment and source code deployment. Choose one according to the situation.

### 1.1 via Docker

### 1.1.1 Requirements
------------
  * docker 20.0 (or greater)
  * docker-compose 1.29.2 (or greater)
  * [How to install docker & docker-compose](https://docs.docker.com/engine/install/ubuntu/)

### 1.1.2 Install CopyHero

    git clone https://github.com/CopyHero/CopyHero
    cd CopyHero
    docker-compose up -d

### 1.1.3 Check if it is correct

    wget http://127.0.0.1:8899/info

## 1.2 via Code

CopyHero now supports bleeding-edge installations. The easiest way to
install the software and track updates is to clone the public repository.
Create a folder on you web server (using whatever method makes sense for
you) and cd into it. Then clone the repository (the folder must be empty!):

## 1.2.1 Requirements
------------
  * Python version 3.8 (or greater)
  * Mongo version 7.0.9 (or greater) [How to install MongoDB](https://www.mongodb.com/docs/manual/installation/)
  * PaddleOCR 2.7.1 (or greater)

### 1.2.2 Install CopyHero

    git clone https://github.com/CopyHero/CopyHero

And deploy the code into somewhere in your server's www root folder, for
instance

    cd CopyHero
    python3 -m venv ./venv
    ./venv/bin/pip install -r ./requirements.txt

### 1.2.3 Install PaddlePaddle (GPU)

- If you have CUDA 11 installed on your machine, please run the following command to install

  ```bash
  ./venv/bin/pip install paddlepaddle-gpu
  ```

### 1.2.4 Start CopyHero
```bash
nohup ./venv/bin/uvicorn app.main:app --host 0.0.0.0 --port 8899 &
```

### 1.2.5 Check if it is correct

    wget http://127.0.0.1:8899/info

## 2 A Guide to Setting Up HTTPS on Port 8899
If you know how to map port 8899 to https, please ignore the following content.
The following is an example of Nginx to illustrate the whole process.
### 2.1 Obtain an SSL/TLS Certificate
To secure your service with HTTPS, you need an SSL/TLS certificate. You can obtain one from a Certificate Authority (CA) like [Let's Encrypt](https://letsencrypt.org/), which provides them for free.
### 2.2 Install Nginx(Ubuntu)
If not already installed, you need to install Nginx on your server. You can do this using your operating system's package manager. For example, on Ubuntu, you would use:
``` shell
    sudo apt update
    sudo apt install nginx
```
### 2.3 Configure Nginx
Create a new configuration file in the /etc/nginx/sites-available/ directory. You can name it after your domain, such as yourdomain.conf, and then link it to the sites-enabled directory.
### 2.4 Edit the Configuration File
Open your newly created configuration file in a text editor and configure it to handle HTTPS requests and proxy them to your HTTP service on port 8899.
Here's a sample configuration that demonstrates how to set up the HTTPS proxy:

    server {
        listen 443 ssl;
        server_name yourdomain.com;
        client_max_body_size 5M; #fix 413 Request Entity Too Large error
        ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
        ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;

        location / {
            proxy_pass http://localhost:8899;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection 'upgrade';
            proxy_set_header Host $host;
            proxy_cache_bypass $http_upgrade;
        }
    }

    server {
        listen 80;
        server_name yourdomain.com;
        return 301 https://$server_name$request_uri;
    }
### 2.5 Enable the Nginx Site
  Enable your site by linking it from sites-available to sites-enabled:

    sudo ln -s /etc/nginx/sites-available/yourdomain.conf /etc/nginx/sites-enabled/
### 2.6 Test Nginx Configuration
  Before restarting Nginx, it's a good idea to test your configuration for syntax errors:

    sudo nginx -t
### 2.7 Restart Nginx
  If the configuration test is successful, restart Nginx to apply the changes:

    sudo nginx -s reload


## 3 Connect CopyHero to your website using a JavaScript code snippet
  Please replace yourdomain.com with your actual domain name.
  ``` javascript
    <!-- Start of CopyHero (app.copyhero.net) code -->
    <script>
      (function (d, t) {
      if (!window.$copyHero) {
        const g = d.createElement(t);
        const s = d.getElementsByTagName(t)[0];
        g.src = "https://app.copyhero.net/sdk.js";
        g.defer = true;
        g.async = true;
        s.parentNode.insertBefore(g, s);
        g.onload = () => {
          window.copyHeroSDK.run({
            apiHost:"https://yourdomain.com"
          });
        };
      }
    })(document, "script");
  </script>
  <!-- End of CopyHero code -->
  ```
Help
----
Visit the [Documentation](https://docs.copyhero.net/).

Contributing
------------
Create your own fork of the project and use
[git-flow](https://github.com/nvie/gitflow) to create a new feature. Once
the feature is published in your fork, send a pull request to begin the
conversation of integrating your new feature into CopyHero.


License
-------
CopyHero is released under the GPL2 license. See the included LICENSE.txt
file for the gory details of the General Public License.

CopyHero is supported by several magical open source projects including:

  * [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
  * [Mongo](https://github.com/mongodb/mongo)
