const form = document.querySelector(".add-todo-section form"),
errorText = form.querySelector(".error_text");
// clickBtn = form.querySelector(".flex-section .add");


form.onsubmit = (event) => {
    event.preventDefault()
    // item = document.getElementById("name").value;
    let formdata = new FormData(form)
    // console.log(item);
    // formdata.append('name', item) 
    // formdata.append('csrfmiddlewaretoken', '{{csrf_token}}');

    fetch("/", {
        method: "POST",
        body: formdata
    })
    .then((response) => response.json())
    .then((data) => {
        console.log("success", data)
        // alert(data['msg']);
        if(data == "success"){
            window.location.href = "/";
        } else {
            errorText.textContent = data;
            errorText.style.display = "block";
        }
    })
    .catch((error) => console.log(error))
}


// select the button for clicking
const btnClickPopover = document.querySelectorAll("#popover");
const items = document.querySelector(".added-items");


btnClickPopover.forEach((btn) => {
    btn.onclick = (e) => {
       let item_id = e.target.value;
       let ids = item_id.toString();
       if(confirm("Are you sure that you want to delete the todo?")) {
        items.classList.add("actives");
        fetch(`/?delete=${item_id}`, {
            method: "GET",
            })
            .then((response) => response.json())
            .then((data) => {
                console.log("Success:", data);
                window.location.href="/";
            })
            .catch((error) => {
                console.error( error);
            });
       }
    }
})


const btnPopover = document.querySelector(".popover-form");
const formContent = document.querySelector(".form-content");

// Btnpopover function
btnPopover.onclick = (e) => {
    if(e.target.classList.contains("btn")){
        formContent.style.display = "block";
        items.classList.toggle("actives");
    }
}

const btnPopover2 = document.querySelector(".popover-form2");
const formContent2 = document.querySelector(".form-content2");

btnPopover2.onclick = (e) => {
    console.log("clicked...");
    if(e.target.classList.contains("btn")){
        formContent2.style.display = "block";
    } else {
        formContent2.style.display = "none";
    }
}


// Closing buttons
const formContentClose = document.querySelector(".form-content");
const btnClose1 = document.querySelector(".close");

btnClose1.onclick = (e) => {
    if(e.target.classList.contains("close")) {
        formContentClose.style.display = "none";
        formContent2.style.display = "none";
        items.classList.remove("actives")
    }
}


const formContentClose2 = document.querySelector(".form-content2");
const btnClos2 = document.querySelector(".close2");

btnClos2.onclick = (e) => {
    if(e.target.classList.contains("close2")) {
        formContentClose2.style.display = "none";
    }
}

// Todo Scripts
const btndone = document.querySelectorAll("#done");
const itemTodo = document.querySelectorAll(".todo");

btndone.onclick = (e) => {
    console.log("Done..");
}