
function Avatar() {
    // Get the first name from the database
    const firstName = UserRepo.get_fname();
  
    // Use the first name to generate the avatar URL
    const url = `https://avatars.dicebear.com/api/avataaars/${firstName}?size=50&style=circle.svg`;
  
    // Update the avatar image
    avatar.src = url;
  }

window.addEventListener('load', Avatar);