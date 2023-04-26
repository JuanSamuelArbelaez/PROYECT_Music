class UndoRedoManager:
    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def do_operation(self, operation):
        operation()
        self.undo_stack.append(operation)
        self.redo_stack.clear()

    def undo(self):
        if not self.undo_stack:
            return
        operation = self.undo_stack.pop()
        operation.undo()
        self.redo_stack.append(operation)

    def redo(self):
        if not self.redo_stack:
            return
        operation = self.redo_stack.pop()
        operation()
        self.undo_stack.append(operation)
