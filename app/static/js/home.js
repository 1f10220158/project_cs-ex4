const main = document.getElementById('main');
const sidebar = document.getElementById('sidebar');

function openSidebar() {
main.classList.add('open');
sidebar.style.right = '0px';
}

function closeSidebar() {
main.classList.remove('open');
sidebar.style.right = '-250px';
}