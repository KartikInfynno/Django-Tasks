// Importing the default export
// import htmx from "htmx.org";
// Or importing the module namespace object
// import * as htmx from "htmx.org";
// Or importing a named export, but looking at the file I doubt you want this one
// import { htmx } from "htmx.org";


const toastElement = document.getElementById("toast")
const toastBody = document.getElementById("toast-body")

const toast = new bootstrap.Toast(toastElement, { delay: 2000 })
console.log("hello")
htmx.on("showMessage", (e) => {
  toastBody.innerText = e.detail.value
  toast.show()
})
