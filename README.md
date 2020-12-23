# STTWebApp
 Web Application that uses the tool "Vosk" to transcribe audios to texts in portuguese

 ---
 
 ## Enviroment
Python 3.8.5

```bash
pip install -r requirements.txt
```

## Running

```bash
flask run #runs app
```
Open in a Web browser
Website: http://localhost:5000


## Structure
```bash
─Transcrição de áudio
│   ├───app
│   ├───blueprints
│   │   └───__pycache__
│   ├───ext
│   │   └───__pycache__
│   ├───static
│   │   ├───css
│   │   └───images
│   ├───STT
│   │   └───Vosk
│   ├───templates
│   └───__pycache__
└───model
    └───ivector
```
