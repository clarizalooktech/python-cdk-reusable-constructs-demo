import aws_cdk as cdk
from infrastructure.stackA.stackA_stack import StackA
from infrastructure.stackB.stackB_stack import StackB

app = cdk.App()

StackA(app, "StackA")
StackB(app, "StackB")

app.synth()