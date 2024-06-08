CopyHero
========
<a href="https://copyhero.net"><img height="80px" width="80px" src="images/favicon.png"
align="left" hspace="10" vspace="6"></a>

**CopyHero Open Source Version** based on [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR), can easily copy text from images. It is easy to integrate into the website or software through Javascript SDK.It's completely **free**.

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


Requirements
------------
  * Python version 3.9 (or greater)
  * Mongo version 7.0.9 (or greater)
  * PaddleOCR 2.7.1 (or greater)

Deployment
----------
CopyHero now supports bleeding-edge installations. The easiest way to
install the software and track updates is to clone the public repository.
Create a folder on you web server (using whatever method makes sense for
you) and cd into it. Then clone the repository (the folder must be empty!):

    git clone https://github.com/CopyHero/CopyHero

And deploy the code into somewhere in your server's www root folder, for
instance

    cd CopyHero
    python3 -m venv ./venv
    ./venv/.bin/pip install -r ./requirements.txt


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
