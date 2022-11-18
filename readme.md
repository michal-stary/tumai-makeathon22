# Do I cope with regulation? - tumai-makeathon22
This app created as a part of TUM.ai Makeathon 22 provides an AI-powered tool to assist AI startups' founders in ideation phase. By using recent NLP approaches such as GPT3, Deberta, or Sentence-transformers, it analyses the startup's description and determine whether it should be legally (based on upcoming EU AI regulation) considered as a high-risk application.   

Web demo deployed and hosted on Azure cloud on this [site](http://reg-score.germanywestcentral.azurecontainer.io:8080/). 

## How to run locally
    $ git clone https://github.com/michal-stary/tumai-makeathon22.git 
    
Save trained models into MY_MODEL_DIR folder. 
Models can be obtained by messaging the authors or by rerunning the training notebooks in research/michal folder. 


    $ cd tumai-makeathon22
    $ sudo docker build -f Dockerfile -t reg_score .
    $ docker run -p 8080:8080 -v MY_MODEL_DIR:/app/src/models reg_score

Open app in browser [http://localhost:8080](http://localhost:8080)
