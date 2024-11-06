from aws_cdk import App
from infrastructure.stackA.stackA_stack import StackA
from infrastructure.stackB.stackB_stack import StackB

app = App()

StackA(app, "StackA")
StackB(app, "StackB")

app.synth() 