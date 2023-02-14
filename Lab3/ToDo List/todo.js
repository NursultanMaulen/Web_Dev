const objList = [];

class todo_class{
    constructor(item) {
        this.ulElement = item;
    }

    add() {
        const todoInput = document.querySelector(".input-line").value;
        if (todoInput == "") {
            alert("Enter your task!");
        } else {
            const todoObject = {
                id: objList.length,
                todoText: todoInput,
                isDone: false,
            }
            objList.unshift(todoObject);
            this.display();
            document.querySelector(".input-line").value = '';
        }
    }

    done_undone(x) {
        const selectedTodoIndex = objList.findIndex((item)=> item.id == x);
        console.log(objList[selectedTodoIndex].isDone);
        objList[selectedTodoIndex].isDone == false ? objList[selectedTodoIndex].isDone = true : objList[selectedTodoIndex].isDone = false;
        this.display();
    }

    deleteElement(z) {
        const selectedDelIndex = objList.findIndex((item)=> item.id == z);

        objList.splice(selectedDelIndex,1);

        this.display();
    }

    display() {
        this.ulElement.innerHTML = "";

        objList.forEach((object_item) => {
            const liElement = document.createElement("li");
            const delBtn = document.createElement("i");

            liElement.innerText = object_item.todoText;
            liElement.setAttribute("data-id", object_item.id);

            delBtn.setAttribute("data-id", object_item.id);
            delBtn.classList.add("far", "fa-trash-alt");

            liElement.appendChild(delBtn);

            delBtn.addEventListener("click", function(e) {
                const deleteId = e.target.getAttribute("data-id");
                myTodoList.deleteElement(deleteId);
            })

            liElement.addEventListener("click", function(e) {
                const selectedId = e.target.getAttribute("data-id");
                myTodoList.done_undone(selectedId);
            })

            if (object_item.isDone) {
                liElement.classList.add("checked");
            }

            this.ulElement.appendChild(liElement);
        })

    }
}

const listSection = document.querySelector(".unlist");

myTodoList = new todo_class(listSection);


document.querySelector(".add-button").addEventListener("click", function() {
    myTodoList.add()
})

document.querySelector(".input-line").addEventListener("keydown", function(e) {
    if (e.keyCode == 13) {
        myTodoList.add()
    }
})