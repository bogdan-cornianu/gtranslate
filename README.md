# gtranslate

## Installation
`sudo python3 setup.py develop`

## Running the unit tests
`sudo python3 setup.py test`

## Usage
Start the daemon  
`gtd`  
  
To translate the sentences from a file(one sentence per line) to italian  
`gtranslate -f translate.txt -l it`  
  
Sample output  
```
Translating, please wait...
Buona sera
Buongiorno
Tag dei ragazzi
Arrivederci
```  
  
For more options  
`gtranslate --help`
