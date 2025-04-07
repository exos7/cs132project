<script lang="ts">
  // Action function to handle smooth scrolling
  function smoothScroll(node) {
    const handleClick = (event) => {
      // Prevent default anchor behavior
      event.preventDefault();
      
      // Get the target element ID from href attribute
      const targetId = node.getAttribute('href')?.substring(1);
      
      if (!targetId) {
        console.warn('No target specified for smooth scroll');
        return;
      }
      
      const targetElement = document.getElementById(targetId);
      
      if (!targetElement) {
        console.error(`Target element with id "${targetId}" not found`);
        return;
      }
      
      // Use the native scrollIntoView with smooth behavior
      targetElement.scrollIntoView({
        behavior: 'smooth',
        block: 'start',
        inline: 'nearest'
      });
    };
    
    // Add event listener
    node.addEventListener('click', handleClick);
    
    // Return cleanup function
    return {
      destroy() {
        node.removeEventListener('click', handleClick);
      }
    };
  }
</script>