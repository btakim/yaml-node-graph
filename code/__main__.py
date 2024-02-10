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

    # create nodes
    graph.create_node('github.actions.WorkflowNode', name="Pipeline", color="#4b4b4b")

    return graph

if __name__ == '__main__':

    # load YAML file
    yaml_file_path = Path(__file__).parent / 'input/example.yaml'
    yaml_data = yaml.load_yaml(yaml_file_path)

    # handle SIGINT to make the app terminate on CTRL+C
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

    # create Qt application
    app = QApplication([])

    # create node graph from yaml
    graph = build_nodegraph_from_yaml(yaml_data)

    # show the node graph widget
    graph.widget.show()

    app.exec_()
    # sys.exit(app.exec_())
