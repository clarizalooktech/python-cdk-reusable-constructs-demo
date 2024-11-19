import aws_cdk as cdk
from infrastructure.stackA.stackA_stack import StackA
from infrastructure.stackB.stackB_stack import StackB

app = cdk.App()

stack_a = StackA(app, "StackA")
stack_b = StackB(app, "StackB")

app.synth()