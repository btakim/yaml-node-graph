from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
from pathlib import Path
import signal

# import library for nodes, node_graph and yaml
from libs import nodes as nd
from libs import node_graph as ng
from libs import yaml

def build_nodegraph_from_yaml(yaml_data):

    # create node graph controller
    graph = ng.WorkflowNodeGraph()

    # registered library nodes
    graph.register_node(nd.WorkflowNode)
    graph.register_node(nd.JobNode)
    graph.register_node(nd.StepNode)
    graph.register_node(nd.ActionNode)

    # get all jobs
    list_of_jobs = list(yaml_data['jobs'])
    list_of_jobs_step_nodes = []
    print(list_of_jobs)

    # iterate over each job
    j = 0
    for job in list_of_jobs:

        # get all steps of a job
        list_of_steps = []
        list_of_steps = yaml_data['jobs'][job]['steps']
        list_of_step_nodes = []
        
        # iterate each step / step action
        i=0
        for i in range(len(list_of_steps)):

            # check if it is a step action or step
            if 'uses' in list_of_steps[i].keys():
                node_type = 'Action'
            else:
                node_type = 'Step'

            # get name and type
            name_step = 'Job-'+str(j+1) + ' ' + node_type + " " + str(i+1)
            node_name_step = 'github.actions.' + node_type + 'Node'

            # create step or action node and display the yaml file
            nd_step = graph.create_node(node_name_step, name=name_step)
            text_display = yaml.dict_to_yaml_text(list_of_steps[i])
            nd_step.add_text_batch_input( name='text_display', text=text_display, tab='widgets')
            list_of_step_nodes.append(nd_step)

            # if there are more than one steps in a job connect them to each other
            if i > 0:
                list_of_step_nodes[i-1].outputs()['out'].connect_to(nd_step.inputs()['in'])
            # if there are more than one job connect last and first step if they depend on each other
            elif j > 0 and 'needs' in yaml_data['jobs'][job].keys():
                for k in range(j):
                    if list_of_jobs[k] in yaml_data['jobs'][job]['needs']:
                        list_of_jobs_step_nodes[k][-1].outputs()['out'].connect_to(nd_step.inputs()['in'])

        j = j + 1
        # save list of step nodes
        list_of_jobs_step_nodes.append(list_of_step_nodes)

    # auto layout base nodes
    graph.auto_layout_nodes()

    # init list of job nodes
    list_of_job_nodes = []
    
    # create job nodes
    i=0
    for job in list_of_jobs:
        nd_job = graph.create_node('github.actions.JobNode', name='Job-'+str(i+1)+' '+job)
        nd_job.wrap_nodes(list_of_jobs_step_nodes[i])
        list_of_job_nodes.append(nd_job)
        i = i + 1

    # create workflow node
    nd_workflow = graph.create_node('github.actions.WorkflowNode', name='Workflow '+yaml_data['name'], color="#4b4b4b")
    # wrap job nodes
    nd_workflow.wrap_nodes(list_of_job_nodes)

    # fit nodes to the viewer
    graph.clear_selection()
    graph.fit_to_selection()

    return graph

if __name__ == '__main__':

    # load YAML file
    yaml_file_path = Path(__file__).parent / 'input/example.yaml'
    yaml_data = yaml.load_yaml(yaml_file_path)
    print(yaml_data)

    # handle SIGINT to make the app terminate on CTRL+C
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    # create Qt application
    app = QApplication([])

    # create node graph from yaml
    graph = build_nodegraph_from_yaml(yaml_data)

    # show the node graph widget
    graph.widget.resize(1100, 800)
    graph.widget.show()

    app.exec_()
    # sys.exit(app.exec_())
