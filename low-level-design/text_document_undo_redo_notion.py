"""

We would like to build a **`TextDocument`** class that supports basic insertion and deletion operations of plain text with some basic undo-redo functionality.

Here is the expected structure for the operations:

/**
 * To start, we'll implement two types of operations we'd like to implement:
 * 1) InsertAtEndOperation: this will allow a user to append a string to the end
 *    of the document.
 * 2) DeleteFromEndOperation: this will allow a user to delete the last n chars
 *    from the document.
 */
type InsertAtEndOperation = {
    type: "insertAtEnd",
    charsToInsert: string
}

type DeleteFromEndOperation = {
    type: "deleteFromEnd",
    numCharsToDelete: number
}

type Operation = InsertAtEndOperation | DeleteFromEndOperation


Here's the structure for the TextDocument class we would like to build. We would like to implement the following 4 methods:

/**
 * Applies the given operation to the document.
 */
applyOperation(op: Operation): void {}

/**
 * Undoes the last operation that was applied to the document. If there
 * is no operation to undo, then do nothing.
 */
undoLast(): void {}

/**
 * Redoes the last operation that was undone to the document. If there
 * is no operation to redo, then do nothing.
 */
redoLast(): void {}

/**
 * Return the current content of the document as a string.
 */
getCurrentContent(): string {}

Below, we also have some test cases in Typescript to demonstrate the expected behavior.

const DEBUG_logCurrentContent = (doc: TextDocument) => {
    console.log(`Current content is: ${doc.getCurrentContent()}`)
}

const doc = new TextDocument()
DEBUG_logCurrentContent(doc) // should print ""

doc.applyOperation({ type: "insertAtEnd", charsToInsert: "hello" })
DEBUG_logCurrentContent(doc) // should print "hello"

doc.applyOperation({ type: "insertAtEnd", charsToInsert: "world" })
DEBUG_logCurrentContent(doc) // should print "helloworld"

doc.applyOperation({ type: "deleteFromEnd", numCharsToDelete: 5 })
DEBUG_logCurrentContent(doc) // should print "hello"

doc.undoLast()
DEBUG_logCurrentContent(doc) // should print "helloworld"

doc.redoLast()
DEBUG_logCurrentContent(doc) // should print "hello"

- **[execution time limit] 4 seconds (py3)**
- **[memory limit] 2g**

"""



"""
---------------------------------------

Thiinking through the problem:

---------------------------------------

insert -> hello
undo_stack -> [, '', insert, hello]

pop from undo and add op to redo:
redo_stack -> [(insert, 'hello') ]

delete -> 5 -> ''
document_string = "helloworldshruti"
undo -> [insert "hello", insert "world", delete 5 "world"]
helloworld


redo
 

"""


class Operation:
    def apply(self, content) -> str:
        pass


class InsertAtEndOperation(Operation):
    def __init__(self, chars_to_insert: str):
        self.chars_to_insert = chars_to_insert
        
    def apply(self, content) -> str:
        return content + self.chars_to_insert
        

class DeleteFromEndOperation(Operation):
    def __init__(self, num_chars_to_delete: int):
        self.num_chars_to_delete = num_chars_to_delete
        
    def apply(self, content) -> str:
        return content[:-1*(self.num_chars_to_delete)]

class TextDocument:
    def __init__(self) -> None:
        self.content = ""
        self.undo_stack = []
        self.redo_stack = []

    def apply_operation(self, op: Operation) -> None:
        
        if isinstance(op, InsertAtEndOperation):
            self.undo_stack.append((op, op.chars_to_insert))
        else:
            self.undo_stack.append((op, op.num_chars_to_delete, self.content[-1*(op.num_chars_to_delete):]))
            
        self.content = op.apply(self.content)

    def undo_last(self) -> None:
        if not self.undo_stack:
            return
        
        if isinstance(self.undo_stack[-1][0], InsertAtEndOperation):
            action, chars = self.undo_stack.pop()
            self.apply_operation(DeleteFromEndOperation(len(chars)))
            self.redo_stack.append((action, chars))
        elif isinstance(self.undo_stack[-1][0], DeleteFromEndOperation):
            action, num, chars = self.undo_stack.pop()
            self.apply_operation(InsertAtEndOperation(chars))
            self.redo_stack.append((action, num, chars))
        

    def redo_last(self) -> None:
        if not self.redo_stack:
            return
        if isinstance(self.redo_stack[-1][0], InsertAtEndOperation):
            action, chars = self.redo_stack.pop()
            self.apply_operation(InsertAtEndOperation(chars))
        elif isinstance(self.redo_stack[-1][0], DeleteFromEndOperation):
            action, num, chars = self.redo_stack.pop()
            self.apply_operation(DeleteFromEndOperation(num))

    def get_current_content(self) -> str:
        return self.content
        
def test_simple_undo_redo():
    doc = TextDocument()
    assert doc.get_current_content() == ""

    doc.apply_operation(InsertAtEndOperation("hello"))
    assert doc.get_current_content() == "hello"

    doc.apply_operation(InsertAtEndOperation("world"))
    assert doc.get_current_content() == "helloworld"

    doc.apply_operation(DeleteFromEndOperation(5))
    assert doc.get_current_content() == "hello"

    doc.undo_last()
    assert doc.get_current_content() == "helloworld"

    doc.redo_last()
    assert doc.get_current_content() == "hello"
    
    print("test_simple_undo_redo passes")

test_simple_undo_redo()



