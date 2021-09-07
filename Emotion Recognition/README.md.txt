### Steps to run the program

#### Install pytorch
`pip install pytorch` or `conda install -c pytorch pytorch` for *Anaconda*

#### Install torchvision
`pip install torchvision` or `conda install -c pytorch torchvision` for *Anaconda*

#### Install Facial Emotion Recognition
`pip install facial-emotion-recognition`

#### Configuring Torch for CPU
Open the file **/serialization.py** from  `./site-package/torch/serialization.py`

Change: 
`def load(f, map_location=None, pickle_module=pickle, **pickle_load_args):` 
to 
`def load(f, map_location='cpu', pickle_module=pickle, **pickle_load_args):`

#### Run the Program and experiment with the algorithm!