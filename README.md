### What is this repository for? ### 

This is a repo that contains the libraries and cdk constructs(s3 bucket at the moment) to deploy a cloud insfrastructure resources using Python CDK. 

* Individual cdk constructs 
- Constructs are placed into sub folders within the repo while calling it within the stack to deploy resources


#### Setup and Folder Structure 

``` root/ 
    ├── setup.py 
    ├── app.py 
    ├── cdk-constructs/ 
    │ ├── __init__.py 
    │ └── s3/ 
    │ ├── __init__.py 
    │ └── s3_bucket.py 
    └── infrastructure/ 
        ├── __init__.py 
        └── stackB/ 
            ├── __init__.py 
            └── stackA_stack.py 
        └── stackB/ 
            ├── __init__.py 
            └── stackB_stack.py 
``` 

To make this work with the project structure: 

1. Create a `setup.py` in your root directory for Python package management: 
``` 
from setuptools import setup, find_packages 

setup( 
    name="cdk-constructs", 
    version="0.1.0", 
    packages=find_packages(), 
    install_requires=[ 
        "aws-cdk-lib>=2.0.0", 
        "constructs>=10.0.0", 
    ], 
) 
``` 

2. Add `__init__.py` files in each directory to make them Python packages: 
``` 
touch cdk-constructs/__init__.py 
touch cdk-constructs/s3/__init__.py 
touch infrastructure/__init__.py 
touch infrastructure/stackA/__init__.py 
touch infrastructure/stackB/__init__.py 
```
3. Set up the Python environment: 
``` 
python3 -m venv .venv source .venv/bin/activate 
``` 

4. Install package in root folder 
``` 
pip install -e . 
``` 
5. Make sure imports work 
``` 
python -c "from cdk_constructs.s3.s3_bucket import CustomS3Bucket" 
``` 
6. If there are import errors, use relative imports: 
``` 
# In stackA_stack.py 
import sys 
import os 
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))) 

from cdk_constructs.s3.s3_bucket import CustomS3Bucket, S3BucketProps 
``` 
7. Create `cdk.json` file and place this: 
``` 
{ 
    "app": "python3 app.py" 
} 
```
8. Test synthesizing in root folder 
``` cdk synth ``` 

## TO USE THIS REPO 
1. Clone repo 
``` 
git clone 
``` 

2. Set up the Python environment: 
``` 
python3 -m venv .venv source .venv/bin/activate 
``` 

3. Install package in root folder 
``` 
pip install -e . 
``` 

4. Synthesize in root folder 
``` 
cdk synth 
``` 

##### Deployment 
* Deploy both stacks 
``` 
cdk deploy --all 
``` 

* Deploy specific stack 
``` 
cdk deploy StackA 
``` 
* Deploy multiple specific stacks 
``` 
cdk deploy StackA StackB 
```