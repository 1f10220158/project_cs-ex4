let openSidebarId = null; 

function toggleSidebar(id) {
  const sidebarContent = document.querySelector(`#sidebar-${id}`);
  
  if (sidebarContent.style.transform === 'translateX(0%)') {
    sidebarContent.style.transform = 'translateX(100%)';
  } else {
    sidebarContent.style.transform = 'translateX(0%)';
  }
}
