const counter = document.getElementById('counter')
const addBtn = document.querySelector('.counter-plus')
const removeBtn = document.querySelector('.counter-minus')
const asyncBtn = document.querySelector('.counter-async')
const themeBtn = document.querySelector('.theme')

let state = 0

function render() {
    counter.textContent = state.toString()
}
render()

addBtn.addEventListener('click', ()=>{
    state++
    render()
})

removeBtn.addEventListener('click', ()=>{
    state--
    render()
})

asyncBtn.addEventListener('click', ()=>{
    setTimeout(()=>{
        state++
        render()
    },1000)
})

themeBtn.addEventListener('click', ()=>{
    document.body.classList.toggle('black')
})
