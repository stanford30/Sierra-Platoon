// console.log('hello world');
const list = document.querySelector('.list');
const listItems = document.querySelectorAll('li');
const addItem = document.querySelector('.add-item');
const todoText = document.querySelector('.todo-text');
// console.log(list.closest('li'));
function toggleStrike() {
  this.classList.toggle('strike');
}
listItems.forEach((item) => {
  item.onclick = toggleStrike;
});

addItem.addEventListener('submit', (e) => {
  e.preventDefault();
  // console.log(todoText.value);
  const li = document.createElement('li');
  li.textContent = todoText.value;
  li.onclick = toggleStrike;
  list.appendChild(li);
  todoText.value = '';
});
// const li = document.createElement('li');
// li.textContent = 'fourth item';
// li.onclick = toggleStrike;
// list.appendChild(li);
// addItem.addEventListener('keyup', (e) => {
//   console.log(e.key);
// });
// console.log(listItems);
