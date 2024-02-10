from NodeGraphQt import BaseNode, BackdropNode, GroupNode

# create a node class object inherited from BaseNode.
class ActionNode(GroupNode):
    """
    A group node class for actions.
    """

    # unique node identifier domain.
    __identifier__ = 'github.actions'

    # initial default node name.
    NODE_NAME = 'Action Node'

    def __init__(self):
        super(ActionNode, self).__init__()
        
# create a node class object inherited from BaseNode.
class StepNode(BaseNode):
    """
    A base node class for steps.
    """

    # unique node identifier domain.
    __identifier__ = 'github.actions'

    # initial default node name.
    NODE_NAME = 'Step Node'

    def __init__(self):
        super(StepNode, self).__init__()

# create a node class object inherited from BaseNode.
class JobNode(BackdropNode):
    """
    A backdrop node class for jobs.
    """

    # unique node identifier domain.
    __identifier__ = 'github.actions'

    # initial default node name.
    NODE_NAME = 'Job Node'

    def __init__(self):
        super(JobNode, self).__init__()

# create a node class object inherited from BackdropNode.
class WorkflowNode(BackdropNode):
    """
    A backdrop node class for workflows.
    """

    # unique node identifier domain.
    __identifier__ = 'github.actions'

    # initial default node name.
    NODE_NAME = 'Workflow Node'

    def __init__(self):
        super(WorkflowNode, self).__init__()