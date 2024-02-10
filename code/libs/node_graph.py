from NodeGraphQt import NodeGraph, PropertiesBinWidget
from PyQt5 import QtCore

class WorkflowNodeGraph(NodeGraph):
    """
    A node graph for workflow visualization
    """

    def __init__(self, parent=None):
        super(WorkflowNodeGraph, self).__init__(parent)

        # properties bin widget.
        self._prop_bin = PropertiesBinWidget(node_graph=self)
        self._prop_bin.setWindowFlags(QtCore.Qt.Tool)

        # wire signal.
        self.node_double_clicked.connect(self.display_prop_bin)

    def display_prop_bin(self, node):
        """
        function for displaying the properties bin when a node
        is double clicked
        """
        if not self._prop_bin.isVisible():
            self._prop_bin.show()